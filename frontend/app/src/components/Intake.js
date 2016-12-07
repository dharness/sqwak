import React, { Component } from 'react';
import { connect } from 'react-redux';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import { browserHistory} from 'react-router';
import RadioButtons from './shared/RadioButtons';
import Dropdown from 'react-dropdown';


class Intake extends Component {

  goToPlayScreen() {
    const path = `/play`;
    browserHistory.push(path);
  }

  onGenderSelected(gender) {
    this.props.dispatch({
      type: 'SET_GENDER',
      gender
    });
  }

  onNumAttmptsSelected(numberOfAttempts) {
    this.props.dispatch({
      type: 'SET_NUMBER_OF_ATTEMPTS',
      numberOfAttempts
    });
  }
  
  onLabelSelected(label) {
    this.props.dispatch({
      type: 'SET_LABEL',
      label
    });
  }

  render() {
    return (
      <div>
        <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
        <div className="sqwak-labs-intake-form">
          <div className="sqwak-labs-intake-form-row">
            <div className="sqwak-labs-intake-userid"> { this.props.subjectId } </div>
          </div>
          <div className="sqwak-labs-intake-form-row">
            <div className="sqwak-labs-intake-radio">
              <label>gender</label>
              <RadioButtons options={['M', 'F', 'O']} onItemSelected={this.onGenderSelected.bind(this)}/>
            </div>
          </div>
          <div className="sqwak-labs-intake-form-row">
            <div className="sqwak-intake-label-dropdown">
              <Dropdown options={['shmiggity-shmaw']} onChange={this.onLabelSelected.bind(this)} value={'shmiggity-shmaw'} placeholder="Label" />
            </div>
          </div>
          <div className="sqwak-labs-intake-form-row">
            <div className="sqwak-labs-intake-radio">
              <label># of attempts</label>
              <RadioButtons options={[10, 30, 50]} onItemSelected={this.onNumAttmptsSelected.bind(this)}/>
            </div>
          </div>
        </div>
        <div onClick={this.goToPlayScreen.bind(this)} className="sqwak-labs-square-button">start</div>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    subjectId: state.testSubject.subjectId
  }
}

export default connect(mapStateToProps)(Intake);
