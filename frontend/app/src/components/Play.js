import React, { Component } from 'react';
import sqwakLabsLogo from './../assets/images/sqwak-labs-mobile.svg';
import playButtonImg from './../assets/images/play-button.svg';
import pauseButtonImg from './../assets/images/pause-button.svg';
import originalShmaw  from './../assets/audio/original-shmaw.wav';
import './../styles/App.css';

class Play extends Component {

  constructor(props) {
    super(props);
    this.state = {
     playButtonImage: playButtonImg 
    };
  }

  componentDidMount() {
    this.audioPlayer.addEventListener('ended', () => {
      this.pauseSound();
    });
  }

  toggleSoundPlaying() {
    if (this.audioPlayer.paused) {
      this.playSound();
    } else {
      this.pauseSound();
    }
  }

  pauseSound() {
    this.audioPlayer.pause();
    this.setState({playButtonImage: playButtonImg}); 
  }

  playSound() {
    this.audioPlayer.currentTime = 0;
    this.audioPlayer.play();
    this.setState({playButtonImage: pauseButtonImg});
  }

  render() {
    return (
        <div>
          <audio controls ref={(e)=> {this.audioPlayer = e}} style={{display: 'none'}}>
            <source src={originalShmaw}/>
          </audio>
          <img src={sqwakLabsLogo} className="sqwak-labs-logo" role="presentation"/>
          <img src={this.state.playButtonImage} className="sqwak-labs-play-button" role="presentation" onClick={this.toggleSoundPlaying.bind(this)}/>
          {/* <div onclick="window.location = '/labs/record'" className="sqwak-labs-square-button">Try it</div> */}
        </div>
    );
  }
}

export default Play;
