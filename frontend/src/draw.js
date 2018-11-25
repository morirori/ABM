export function draw(canvas, context, objects) {
    context.clearRect(0, 0, canvas.width, canvas.height);
    drawPitch(canvas,context);
    drawBall(canvas, context, objects["ball"]);
    drawPlayers(canvas, context, objects);
}

export function drawBall(canvas, context, objects) {
  context.beginPath();
  context.arc(objects.x, objects.y , 5, 0, 2 * Math.PI);
  context.fillStyle = "#ffff00";
  context.fill();
  context.closePath();
}

export function drawPlayers(canvas, context, objects) {
    const cols = {
        "team_away": "#800000",
        "team_home": "#0000FF",
    };

    objects["team_away"].forEach((player) =>drawPlayer(canvas, context, player, cols["team_away"]));
    objects["team_home"].forEach((player) =>drawPlayer(canvas, context, player, cols["team_home"]));
}

function drawPlayer(canvas, context, player, colour) {
  context.beginPath();
  context.arc(player.x, player.y , 5, 0, 2 * Math.PI);
  context.fillStyle = colour;
  context.fill();
  context.closePath();
}

export function drawPitch(canvas, context) {
    context.beginPath();
    context.rect(0,0, canvas.width, canvas.height);
    context.fillStyle = "#060";
    context.fill();
    context.lineWidth = 0.5;
    context.strokeStyle = "#FFF";
    context.stroke();
    context.closePath();
    context.fillStyle = "#FFF";

      // Mid line
    context.beginPath();
    context.moveTo(canvas.width / 2, 0);
    context.lineTo(canvas.width / 2, canvas.height);
    context.stroke();
    context.closePath();

      //Mid circle
    context.beginPath();
    context.arc(canvas.width / 2, canvas.height / 2, 0.09*canvas.width, 0, 2*Math.PI, false);
    context.stroke();
    context.closePath();
      //Mid point
    context.beginPath();
    context.arc(canvas.width / 2, canvas.height / 2, 1, 0, 2*Math.PI, false);
    context.fill();
    context.closePath();

      //Home penalty box
    context.beginPath();
    context.rect(0, canvas.height*0.23, canvas.width*0.15, 0.57*canvas.height);
    context.stroke();
    context.closePath();

      //Home goal box
    context.beginPath();
    context.rect(0, 0.38*canvas.height, 0.07*canvas.width, 0.25*canvas.height);
    context.stroke();
    context.closePath();

      //Home goal
    context.beginPath();
    context.moveTo(1, 0.45*canvas.height);
    context.lineTo(1, 0.55*canvas.height);
    context.lineWidth = 1.5;
    context.stroke();
    context.closePath();
    context.lineWidth = 0.5;

      //Home penalty point
    context.beginPath();
    context.arc(0.11*canvas.width, canvas.height / 2, 1, 0, 2*Math.PI, true);
    context.fill();
    context.closePath();

      //Home half circle
    context.beginPath();
    context.arc(0.11*canvas.width, canvas.height / 2, 0.09*canvas.width, 0.36*Math.PI, 1.65*Math.PI,true);
    context.stroke();
    context.closePath();

      //Away penalty box
    context.beginPath();
    context.rect(canvas.width*0.85, canvas.height*0.23, canvas.width*0.15, 0.57*canvas.height);
    context.stroke();
    context.closePath();

      //Away goal box
    context.beginPath();
    context.rect(canvas.width*0.93,0.38*canvas.height, 0.07*canvas.width, 0.25*canvas.height);
    context.stroke();
    context.closePath();

      //Away goal
    context.beginPath();
    context.moveTo(canvas.width-1, 0.45*canvas.height);
    context.lineTo(canvas.width-1, 0.55*canvas.height);
    context.lineWidth = 1.5;
    context.stroke();
    context.closePath();
    context.lineWidth = 0.5;

      //Away penalty point
    context.beginPath();
    context.arc(0.89*canvas.width, canvas.height / 2, 1, 0, 2*Math.PI, true);
    context.fill();
    context.closePath();

      //Away half circle
    context.beginPath();
    context.arc(0.89*canvas.width, canvas.height / 2, 0.09*canvas.width, 0.66*Math.PI, 1.35*Math.PI,false);
    context.stroke();
    context.closePath();

      //Home L corner
    context.beginPath();
    context.arc(0, 0, 8, 0, 0.5*Math.PI, false);
    context.stroke();
    context.closePath();
      //Home R corner
    context.beginPath();
    context.arc(0, canvas.height, 8, 0, 2*Math.PI, true);
    context.stroke();
    context.closePath();
      //Away R corner
    context.beginPath();
    context.arc(canvas.width, 0, 8, 0.5*Math.PI, Math.PI, false);
    context.stroke();
    context.closePath();
      //Away L corner
    context.beginPath();
    context.arc(canvas.width, canvas.height, 8, Math.PI, 1.5*Math.PI, false);
    context.stroke();
    context.closePath();
}
