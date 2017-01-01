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
var sampleLength = 3.0;


function gotBuffers( buffers ) {
    var amplitudes =  Array.prototype.slice.call(buffers[0]);
    uploadAmplitudes(amplitudes);
    document.querySelector('#attempt-count').innerHTML = ++recIndex; 
}

function uploadAmplitudes(amplitudes) {
    var payload = { data: {  amplitudes, label: "TEST_DATA" } };
    fetch('/sounds', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
    .catch(error => console.error('Request failed', error));
}

function startRecording( e ) {
    if (!audioRecorder)
        return;
    if (!e.classList.contains("recording")) {
        e.classList.add("recording");
        audioRecorder.clear();
        audioRecorder.record();
        window.setTimeout(() => {
            stopRecording(e);
        }, sampleLength * 1000)
    }
}

function stopRecording( e ) {
    audioRecorder.stop();
    e.classList.remove("recording");
    audioRecorder.getBuffers( gotBuffers );
}

function gotStream(stream) {
    inputPoint = audioContext.createGain();
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
