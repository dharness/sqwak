import Recorder from './../lib/recorder.js';


var recordingService = {

  recordFor(timeLimit) {
    this.audioRecorder.clear();
    this.audioRecorder.record();
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        this.audioRecorder.getBuffers((buffers) => {
          this.audioRecorder.stop();
          resolve(buffers);
        });
      }, timeLimit);
    });
  },

  _gotStream(stream) {
    window.AudioContext = window.AudioContext || window.webkitAudioContext;
    var audioContext = new AudioContext();
    var inputPoint = audioContext.createGain();

    // Create an AudioNode from the stream.
    var realAudioInput = audioContext.createMediaStreamSource(stream);
    var audioInput = realAudioInput;
    audioInput.connect(inputPoint);

    var analyserNode = audioContext.createAnalyser();
    analyserNode.fftSize = 2048;
    inputPoint.connect( analyserNode );

   this.audioRecorder = new Recorder( inputPoint );
  },

  init() {
    if (!navigator.getUserMedia)
        navigator.getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia;
    if (!navigator.cancelAnimationFrame)
        navigator.cancelAnimationFrame = navigator.webkitCancelAnimationFrame || navigator.mozCancelAnimationFrame;
    if (!navigator.requestAnimationFrame)
        navigator.requestAnimationFrame = navigator.webkitRequestAnimationFrame || navigator.mozRequestAnimationFrame;

    navigator.getUserMedia({
      "audio": {
        "mandatory": {
          "googEchoCancellation": "false",
          "googAutoGainControl": "false",
          "googNoiseSuppression": "false",
          "googHighpassFilter": "false"
        },
        "optional": []
      },
    }, this._gotStream.bind(this), function(e) {
        alert('Error getting audio');
        console.log(e);
    });
  }
}

export default recordingService;
