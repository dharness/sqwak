import React, { Component } from 'react';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import recordButtonImg  from './../assets/images/record-button-normal.svg';
import recordButtonActiveImg from './../assets/images/record-button-active.svg';
import recordingService from './../services/recordingService.js';

class Record extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      recordButtonImage: recordButtonImg,
      isRecording: false
    }
  }

  startRecording() {
    if (!this.state.isRecording) {
      recordingService.recordFor(3.5 * 1000).then((buffers) => {
        console.log(buffers);
        this.setState({ isRecording: false });
      });
      this.setState({ isRecording: true });
    }
  }

  componentDidMount() {
    recordingService.init();
  }

  render() {
    return (
      <div>
        <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
        <img src={this.state.isRecording ? recordButtonActiveImg : recordButtonImg} className="sqwak-labs-round-button" role="presentation" onClick={this.startRecording.bind(this)}/>
      </div>
    );
  }
}

export default Record;
