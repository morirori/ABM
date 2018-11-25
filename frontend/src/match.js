export function getMatchData(canvas, command = 'init') {
  return {
    "x": canvas.width,
    "y": canvas.height,
    "command": command
  };
}

export function sendWorldData(websocketsClient, worldData) {
  websocketsClient.send(JSON.stringify(worldData));
}

export function updatePitchSize(canvas, window_width, window_height) {
    canvas.width = window_width;
    canvas.height = 0.8*window_height;
}
