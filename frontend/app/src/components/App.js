import React, { Component } from 'react';
import { Router, Route, browserHistory } from 'react-router'
import './../styles/App.css';
import Play from './Play'
import Record from './Record'

class App extends Component {
  render() {
    return (
      <Router history={browserHistory}>
        <Route path="/" component={Play} />
        <Route path="/record" component={Record} />
      </Router>
    );
  }
}

export default App;
