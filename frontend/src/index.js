import {draw} from './draw.js'
import {getMatchData, sendWorldData, updatePitchSize} from './match.js'
import {webSocketFactory} from './connectionFactory'

const playButton = document.getElementById('play');
const restartButton = document.getElementById("restart");
let started = false;
const canvas = document.getElementById('world');
const ctx = canvas.getContext('2d');
let websocketsClient = webSocketFactory.connect('ws://192.168.99.100:8090');

updatePitchSize(canvas, window.innerWidth, window.innerHeight);

window.onresize = (event) => {
  updatePitchSize(canvas, event.target.innerWidth, event.target.innerHeight);
  const data =  getMatchData(canvas, 'init');
  sendWorldData(websocketsClient, data);
};

websocketsClient.onmessage = (event) => {
    if (started === true) {
        const objects = JSON.parse(event.data);
        draw(canvas, ctx, objects);
    }
};

restartButton.onclick = (event) => {
  const data = getMatchData(canvas, 'init');
  sendWorldData(websocketsClient, data);
  started = false;
  playButton.textContent = "Start";

};

websocketsClient.onopen = (event) => {
  const data = getMatchData(canvas, 'init');
  sendWorldData(websocketsClient, data);
};

playButton.onclick = (event) => {
    if (started === false){
        started = true;
        playButton.textContent = "Pause";
        const data = getMatchData(canvas, 'start');
        sendWorldData(websocketsClient, data);
    }
    else{
        playButton.textContent = "Start";
        started = false;
        const data = getMatchData(canvas, 'pause');
        sendWorldData(websocketsClient, data);
    }

};


