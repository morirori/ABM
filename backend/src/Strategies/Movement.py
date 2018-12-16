from src.Abstracts.AbstractAgent import AbstractAgent
from math import sqrt

def move_forward(player: AbstractAgent):
    temp = []

    temp.append(player.coordinates[0] + player.speed)
    temp.append(player.coordinates[1])
    return temp

def move_to_ball(player: AbstractAgent):
    angle = player.pitch.get_heading(player.coordinates, [player.ball.x, player.ball.y])
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    coef = player.speed/dist
    temp = []
    temp.append(player.coordinates[0] + coef*angle[0])
    temp.append(player.coordinates[1] + coef*angle[1])

    return temp

