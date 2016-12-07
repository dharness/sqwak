import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { applyMiddleware, createStore } from 'redux';
import createLogger from 'redux-logger';
import reducers from './reducers';
import App from './components/App';
import './styles/index.css';
import './styles/labs.css';


const logger = createLogger();

const initialState = {
  testSubject: {
    subjectId: (''+Math.random()).split('.')[1] 
  }
};

let store = createStore(
  reducers,
  initialState,
  applyMiddleware(logger)
);

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
