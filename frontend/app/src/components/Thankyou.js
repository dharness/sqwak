import React, { Component } from 'react';
import { connect } from 'react-redux';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import testTubeImg from './../assets/images/testtube.svg';


class Thankyou extends Component {

  constructor(props) {
    super(props);
    this.state = {
      isUploading: true,
      numberUploaded: 0
    };
  }

  uploadAmplitudes() {
    this.props.attempts.forEach(attempt => {
      var payload = {
        data: {
          amplitudes: attempt,
          label: this.props.label,
          gender: this.props.gender
        }
      };

      fetch(`//${process.env.REACT_APP_API_URL}/api/sounds`, {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
      .then((response) => {
        if (response.status === 200) {
          let isUploading = true;
          if (this.state.numberUploaded >= this.props.attempts.length -1) {
            isUploading = false;
          }
          this.setState({
            numberUploaded: this.state.numberUploaded + 1,
            isUploading
          });
        }
      })
      .catch(error => alert('Request failed', error));
    });
  }


  render() {
    return (
      <div>
        <div className="sqwak-labs-top-row">
          <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
        </div>
        <div className="sqwak-labs-middle-row">
          {(() => {
            if (this.state.isUploading) {
              return (
                <div>
                  <div className="sqwak-labs-countdown"> Uploading ... </div>
                  <div className="sqwak-labs-countdown"> {this.state.numberUploaded} / {this.props.attempts.length} </div>
                </div>
              )
            } else {
              return <img src={testTubeImg} className="sqwak-labs-thankyou-tube" role="presentation"/> 
            }
          })()}
        </div>
        <div className="sqwak-labs-bottom-row">
          <div className="sqwak-labs-buttom-bar sqwak-labs-button-group">
            <div 
              onClick={this.state.isUploading ? this.uploadAmplitudes.bind(this) : () => {window.location = '/'}} 
              className="sqwak-labs-square-button">
              {this.state.isUploading ? "Upload" : "Replay"}
            </div>
          </div>
        </div>
      </div>
    )
  } 
}

function mapStateToProps(state) {
  return {
    numberOfAttempts: state.testSubject.numberOfAttempts,
    attempts: state.testSubject.attempts,
    label: state.testSubject.label,
    gender: state.testSubject.gender
  }
}

export default connect(mapStateToProps)(Thankyou); 
