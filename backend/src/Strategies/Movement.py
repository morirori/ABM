from src.Abstracts.AbstractAgent import AbstractAgent
from math import sqrt
from src.Utils.Tags import StrategiesTag


def move_forward(player: AbstractAgent):
    temp = []

    temp.append(player.coordinates[0] + player.speed)
    temp.append(player.coordinates[1])
    return temp

def move_to_ball(player: AbstractAgent):
    angle = player.pitch.get_heading(player.coordinates, [player.ball.x, player.ball.y])
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    if dist > player.speed:
        coef = player.speed/dist
    else:
        coef = 1
    temp = []
    temp.append(player.coordinates[0] + coef*angle[0])
    temp.append(player.coordinates[1] + coef*angle[1])
    return temp


def get_vector_to_point(player: AbstractAgent, coord):
    angle = player.pitch.get_heading(player.coordinates, [coord[0], coord[1]])
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    if dist > player.speed:
        coef = player.speed/dist
    else:
        coef = 1
    temp = [player.coordinates[0] + coef*angle[0], player.coordinates[1] + coef*angle[1]]

    return temp


def find_opt_coord(player: AbstractAgent):
    if player.id == 2 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] / 2),  int(player.pitch.size[1] / 8)))
    elif player.id == 3 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] / 3), int(player.pitch.size[1] / 3)))
    elif player.id == 4 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] / 3), int(player.pitch.size[1]*2/ 3)))
    elif player.id == 5 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] / 2), int(player.pitch.size[1]*7/ 8)))
    elif player.id == 6 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] * 0.85), int(player.pitch.size[1] / 8)))
    elif player.id == 7 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] * 0.75), int(player.pitch.size[1] / 3)))
    elif player.id == 8 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] * 0.75), int(player.pitch.size[1]*2/ 3)))
    elif player.id == 9 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] * 0.85), int(player.pitch.size[1]/2 - 20)))
    elif player.id == 10 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] * 0.85), int(player.pitch.size[1]/2 + 20)))
    else:
        return player.coordinates

