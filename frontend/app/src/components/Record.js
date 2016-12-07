import React, { Component } from 'react';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import recordButtonImg  from './../assets/images/record-button-normal.svg';
import recordButtonActiveImg from './../assets/images/record-button-active.svg';
import recordingService from './../services/recordingService.js';
import { Link } from 'react-router'

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

  startCountdown() {
    this.countDownIntervalId = setInterval(() => {
      if (this.state.timeRemaining <= 0) {
        this.stopRecording();
      } else {
        this.setState({timeRemaining: this.state.timeRemaining - 100 });
      }
    }, 100 );
  }

  startRecording() {
    if (!this.state.isRecording) {
      this.startCountdown();
      recordingService.startRecording();
      this.setState({ isRecording: true });
    }
  }

  stopRecording() {
    this.setState({ isRecording: false, timeRemaining: this.sampleLength * 1000 });
    clearInterval(this.countDownIntervalId);
  }

  getTime() {
    let timeString = this.state.timeRemaining.toString();
    const padLength = (4 - timeString.length) || 0;
    const padding = new Array(padLength).fill("0").join("");
    timeString = padding + timeString;
    return {
      seconds: timeString[0], 
      milliseconds: timeString[1] + timeString[2]
    }
  }

  componentDidMount() {
    recordingService.init();
  }

  render() {
    return (
      <div>
        <Link to={'/'}>
          <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
        </Link>
        <img src={this.state.isRecording ? recordButtonActiveImg : recordButtonImg} className="sqwak-labs-round-button" role="presentation" onClick={this.startRecording.bind(this)}/>
        <div className="sqwak-labs-recording-timer">
          {this.getTime().seconds}:{this.getTime().milliseconds}
        </div>
      </div>
    );
  }
}

export default Record;
