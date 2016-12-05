import React, { Component } from 'react';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import recordButtonImg  from './../assets/images/record-button-normal.svg';
import recordButtonActiveImg from './../assets/images/record-button-active.svg';
import recordingService from './../services/recordingService.js';

class Record extends Component {
  
  constructor(props) {
    super(props);
    this.sampleLength = 3.5;
    this.state = {
      recordButtonImage: recordButtonImg,
      isRecording: false,
      timeRemaining: this.sampleLength * 1000
    }
  }

  tick() {
    this.setState({timeRemaining: this.state.timeRemaining - 100 });
  }

  startCountdown() {
    this.countDownIntervalId = setInterval(() => this.tick(), 100 );
  }

  startRecording() {
    if (!this.state.isRecording) {
      this.startCountdown();
      recordingService.recordFor(this.sampleLength * 1000).then((buffers) => {
        clearInterval(this.countDownIntervalId);
        console.log(buffers);
        this.setState({ isRecording: false, timeRemaining: this.sampleLength * 1000 });
      });
      this.setState({ isRecording: true });
    }
  }

  getTime() {
    const timeString = this.state.timeRemaining.toString();
    const seconds = (this.state.timeRemaining >= 1000) ? timeString[0] : '0';
    const milliseconds = timeString[1] + timeString[2]
    return { seconds, milliseconds }
  }

  componentDidMount() {
    recordingService.init();
  }

  render() {
    return (
      <div>
        <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
        <img src={this.state.isRecording ? recordButtonActiveImg : recordButtonImg} className="sqwak-labs-round-button" role="presentation" onClick={this.startRecording.bind(this)}/>
        <div className="sqwak-labs-recording-timer">
          {this.getTime().seconds}:{this.getTime().milliseconds}
        </div>
      </div>
    );
  }
}

export default Record;
