import { combineReducers } from 'redux'

const testSubject = (state = {}, action) => {
  switch(action.type) {
    case 'SET_SUBJECT_ID':
      return Object.assing({}, state, {subjectId: action.subjectId});
    case 'SET_LABEL':
      return Object.assign({}, state, {label: action.label});
    case 'SET_NUMBER_OF_ATTEMPTS':
      return Object.assign({}, state, {numberOfAttempts: action.numberOfAttempts});
    case 'SET_GENDER':
      return Object.assign({}, state, {gender: action.gender});
    case 'ADD_ATTEMPT':
      return Object.assign({}, state, {attempts: [...state.attempts, action.attempt]})
    default:
      return state;
  }
}

export default combineReducers({
  testSubject
})

