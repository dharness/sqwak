import React, { Component } from 'react';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import testTubeImg from './../assets/images/testtube.svg';
import { browserHistory } from 'react-router'


class Thankyou extends Component {

  goToIntake() {
    const path = '/'
    //browserHistory.push(path)
    window.location = '/'
}

  render() {
    return (
      <div>
        <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
        <img src={testTubeImg} className="sqwak-labs-thankyou-tube" role="presentation"/>
        <div className="sqwak-labs-buttom-bar sqwak-labs-button-group">
          <div onClick={this.goToIntake.bind(this)} className="sqwak-labs-square-button">Retry</div>
        </div>
      </div>
    )
  } 
}

export default Thankyou
