export var webSocketFactory = {
  connectionTries: 3,
  connect: function(url) {
    var ws = new WebSocket(url);
    ws.addEventListener("error", e => {
        if (e.target.readyState === 3) {
            this.connectionTries--;

        if (this.connectionTries > 0) {
          setTimeout(() => this.connect(url), 5000);
        } else {
          throw new Error("Maximum number of connection trials has been reached");
        }
      }
    });
    return ws
  }
};
