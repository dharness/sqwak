import React, { Component } from 'react';

class RadioButtons extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      selectedOption: 0
    };
  }

  onItemSelected(e, i) {
    this.setState({selectedOption: i});
    this.props.onItemSelected && this.props.onItemSelected(e, i);
  }

  render() {
    return (
      <div className="sqwak-labs-radio-button-group">
        {this.props.options.map((e, i) => {
          return (
            <div className={"sqwak-labs-radio-button" + (this.state.selectedOption === i ? " active" : "")} 
              key={i} 
              onClick={() => {this.onItemSelected(e, i)}}>{e}
            </div>)
        })}
      </div>
    );
  }
}

export default RadioButtons;
