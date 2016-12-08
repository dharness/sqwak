import React, { Component } from 'react';
import { Router, Route, browserHistory } from 'react-router'
import './../styles/App.css';
import Play from './Play'
import Record from './Record'
import Intake from './Intake'
import Thankyou from './Thankyou'

class App extends Component {
  render() {
    return (
      <Router history={browserHistory}>
        <Route path="/" component={Intake} />
        <Route path="/play" component={Play} />
        <Route path="/record" component={Record} />
        <Route path="/thankyou" component={Thankyou} />
      </Router>
    );
  }
}

export default App;
