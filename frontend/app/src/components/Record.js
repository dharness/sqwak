import React, { Component } from 'react';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import recordButtonImg  from './../assets/images/record-button-normal.svg';
import recordButtonActiveImg from './../assets/images/record-button-active.svg';


class Record extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      recordButtonImage: recordButtonImg
    }
  }

  startRecording() {
    this.setState({
      recordButtonImage: recordButtonActiveImg 
    });
  }


  render() {
    return (
      <div>
        <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
        <img src={this.state.recordButtonImage} className="sqwak-labs-round-button" role="presentation" onClick={this.startRecording.bind(this)}/>
      </div>
    );
  }
}

export default Record;
