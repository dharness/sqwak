window.AudioContext = window.AudioContext || window.webkitAudioContext;

var audioContext = new AudioContext();
var audioInput = null,
    realAudioInput = null,
    inputPoint = null,
    audioRecorder = null;
var rafID = null;
var analyserContext = null;
var canvasWidth, canvasHeight;
var recIndex = 0;


function gotBuffers( buffers ) {
    // the ONLY time gotBuffers is called is right after a new recording is completed - 
    // so here's where we should set up the download.
    var amplitudes =  Array.prototype.slice.call(buffers[0]);
    uploadAmplitudes(amplitudes);
    document.querySelector('#attempt-count').innerHTML = ++recIndex; 
    // audioRecorder.exportWAV( doneEncoding );
}

function uploadAmplitudes(amplitudes) {
    var data = {
        data: { 
            amplitudes,
            label: "TEST_DATA"
        }
    };
    fetch('/sounds', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        console.log(response);
        response.json()
    })
    .then(result =>  console.log(result) )
    .catch(error => console.log('Request failed', error));
}

function doneEncoding( blob ) {
    Recorder.setupDownload( blob, "myRecording" + ((recIndex<10)?"0":"") + recIndex + ".wav" );
    recIndex++;
}

function toggleRecording( e ) {
    if (e.classList.contains("recording")) {
        stopRecording(e);
    } else {
        startRecording(e);
    }
}

function startRecording( e ) {
    // start recording
    if (!audioRecorder)
        return;
    if (!e.classList.contains("recording")) {
        e.classList.add("recording");
        audioRecorder.clear();
        audioRecorder.record();
        window.setTimeout(() => {
            stopRecording(e);
        }, 5000)
    }
}

function stopRecording( e ) {
    // stop recording
    audioRecorder.stop();
    e.classList.remove("recording");
    audioRecorder.getBuffers( gotBuffers );
}

function gotStream(stream) {
    inputPoint = audioContext.createGain();

    // Create an AudioNode from the stream.
    realAudioInput = audioContext.createMediaStreamSource(stream);
    audioInput = realAudioInput;
    audioInput.connect(inputPoint);

    analyserNode = audioContext.createAnalyser();
    analyserNode.fftSize = 2048;
    inputPoint.connect( analyserNode );

    audioRecorder = new Recorder( inputPoint );
}

function initAudio() {
        if (!navigator.getUserMedia)
            navigator.getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia;
        if (!navigator.cancelAnimationFrame)
            navigator.cancelAnimationFrame = navigator.webkitCancelAnimationFrame || navigator.mozCancelAnimationFrame;
        if (!navigator.requestAnimationFrame)
            navigator.requestAnimationFrame = navigator.webkitRequestAnimationFrame || navigator.mozRequestAnimationFrame;

    navigator.getUserMedia(
        {
            "audio": {
                "mandatory": {
                    "googEchoCancellation": "false",
                    "googAutoGainControl": "false",
                    "googNoiseSuppression": "false",
                    "googHighpassFilter": "false"
                },
                "optional": []
            },
        }, gotStream, function(e) {
            alert('Error getting audio');
            console.log(e);
        });
}

window.addEventListener('load', initAudio );
