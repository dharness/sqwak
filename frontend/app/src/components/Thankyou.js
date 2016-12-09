import React, { Component } from 'react';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import testTubeImg from './../assets/images/testtube.svg';


class Thankyou extends Component {

  render() {
    return (
      <div>
        <div className="sqwak-labs-top-row">
          <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
        </div>
        <div className="sqwak-labs-middle-row">
          <img src={testTubeImg} className="sqwak-labs-thankyou-tube" role="presentation"/>
        </div>
        <div className="sqwak-labs-bottom-row">
          <div className="sqwak-labs-buttom-bar sqwak-labs-button-group">
            <div onClick={() => {window.location = '/'}} className="sqwak-labs-square-button">Retry</div>
          </div>
        </div>
      </div>
    )
  } 
}

export default Thankyou
