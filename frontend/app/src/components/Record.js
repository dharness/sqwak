import React, { Component } from 'react';
import { connect } from 'react-redux';
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
        recordingService.stopRecording().then((buffers) => this.addAttempt(buffers[0]))
      } else {
        this.setState({timeRemaining: this.state.timeRemaining - 100 });
      }
    }, 100 );
  }

  addAttempt(amplitudes) {
    this.props.dispatch({
      type: 'ADD_ATTEMPT',
      attempt: amplitudes
    });
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
        <div className="sqwak-labs-countdown"> {this.props.attempts.length} / {this.props.numberOfAttempts} </div>
        <img src={this.state.isRecording ? recordButtonActiveImg : recordButtonImg} className="sqwak-labs-round-button" role="presentation" onClick={this.startRecording.bind(this)}/>
        <div className="sqwak-labs-recording-timer">
          {this.getTime().seconds}:{this.getTime().milliseconds}
        </div>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    numberOfAttempts: state.testSubject.numberOfAttempts,
    attempts: state.testSubject.attempts
  }
}

export default connect(mapStateToProps)(Record);
