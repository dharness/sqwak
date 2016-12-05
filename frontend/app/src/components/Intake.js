import React, { Component } from 'react';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import { browserHistory} from 'react-router';
import RadioButtons from './shared/RadioButtons';
import Dropdown from 'react-dropdown';

class Intake extends Component {

  goToPlayScreen() {
    const path = `/play`
    browserHistory.push(path)
  }

  onGenderSelected(gender) {
    console.log("gender is ", gender)
  }

  onNumAttmptsSelected(numAttempts) {
    console.log("number of attempts is ", numAttempts)
  }
  
  onLabelSelected(label) {
    console.log(label);
  }

  render() {
    return (
      <div>
        <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
        <div className="sqwak-labs-intake-form">
          <div className="sqwak-labs-intake-form-row">
            <div className="sqwak-labs-intake-userid"> abcd1293nnf993j39jj </div>
          </div>
          <div className="sqwak-labs-intake-form-row">
            <div className="sqwak-labs-intake-radio">
              <label>gender</label>
              <RadioButtons options={['M', 'F', 'O']} onItemSelected={this.onGenderSelected}/>
            </div>
          </div>
          <div className="sqwak-labs-intake-form-row">
            <div className="sqwak-intake-label-dropdown">
              <Dropdown options={['shmiggity-shmaw']} onChange={this.onLabelSelected} value={'shmiggity-shmaw'} placeholder="Label" />
            </div>
          </div>
          <div className="sqwak-labs-intake-form-row">
            <div className="sqwak-labs-intake-radio">
              <label># of attempts</label>
              <RadioButtons options={[10, 30, 50]} onItemSelected={this.onNumAttmptsSelected}/>
            </div>
          </div>
        </div>
        <div onClick={this.goToPlayScreen.bind(this)} className="sqwak-labs-square-button">start</div>
      </div>
    );
  }
}

export default Intake;
