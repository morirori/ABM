from src.Abstracts.AbstractAgent import AbstractAgent
from math import sqrt
import random

from src.Utils.config import movement_config


def move_backward(player: AbstractAgent):
    if player.host:
        return [player.coordinates[0] - player.speed, player.coordinates[1]]
    else:
        return [player.coordinates[0] + player.speed, player.coordinates[1]]


def move_forward(player: AbstractAgent):
    if player.host:
        return [player.coordinates[0] + player.speed, player.coordinates[1]]
    else:
        return [player.coordinates[0] - player.speed, player.coordinates[1]]


def move_backward_towards_side_line(player: AbstractAgent):
    if player.host:
        return [player.coordinates[0] - player.speed, player.coordinates[1] - 0.5]\
            if player.coordinates[1] < int(player.pitch.size[1] / 2)\
            else [player.coordinates[0] - player.speed, player.coordinates[1] + 0.5]
    else:
        return [player.coordinates[0] + player.speed, player.coordinates[1] - 0.5] \
            if player.coordinates[1] < int(player.pitch.size[1] / 2) \
            else [player.coordinates[0] + player.speed, player.coordinates[1] + 0.5]


def move_backward_towards_middle_filed(player: AbstractAgent):
    if player.host:
        return [player.coordinates[0] - player.speed, player.coordinates[1] + 0.5]\
            if player.coordinates[1] < int(player.pitch.size[1] / 2)\
            else [player.coordinates[0] - player.speed, player.coordinates[1] - 0.5]
    else:
        return [player.coordinates[0] + player.speed, player.coordinates[1] + 0.5] \
            if player.coordinates[1] < int(player.pitch.size[1] / 2) \
            else [player.coordinates[0] + player.speed, player.coordinates[1] - 0.5]


def move_forward_towards_side_line(player: AbstractAgent):
    if player.host:
        return [player.coordinates[0] + player.speed, player.coordinates[1] - 0.5]\
            if player.coordinates[1] < int(player.pitch.size[1] / 2)\
            else [player.coordinates[0] + player.speed, player.coordinates[1] + 0.5]
    else:
        return [player.coordinates[0] - player.speed, player.coordinates[1] - 0.5] \
            if player.coordinates[1] < int(player.pitch.size[1] / 2) \
            else [player.coordinates[0] - player.speed, player.coordinates[1] + 0.5]


def move_forward_towards_middle_filed(player: AbstractAgent):
    if player.host:
        return [player.coordinates[0] + player.speed, player.coordinates[1] + 0.5]\
            if player.coordinates[1] < int(player.pitch.size[1] / 2)\
            else [player.coordinates[0] + player.speed, player.coordinates[1] - 0.5]
    else:
        return [player.coordinates[0] - player.speed, player.coordinates[1] + 0.5] \
            if player.coordinates[1] < int(player.pitch.size[1] / 2) \
            else [player.coordinates[0] - player.speed, player.coordinates[1] - 0.5]


def move_to_ball(player: AbstractAgent):
    angle = player.pitch.get_heading(player.coordinates, [player.ball.x, player.ball.y])
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    if dist > player.speed:
        coef = player.speed/dist
    else:
        coef = 1
    temp = [player.coordinates[0] + coef * angle[0], player.coordinates[1] + coef * angle[1]]
    return temp


def get_vector_to_point(player: AbstractAgent, coord):
    angle = player.pitch.get_heading(player.coordinates, [coord[0], coord[1]])
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    coef = player.speed/dist if dist > player.speed else 1
    return [player.coordinates[0] + coef*angle[0], player.coordinates[1] + coef*angle[1]]


def get_vector_from_ball_to_target_player(ball, player2: AbstractAgent):
    angle = player2.pitch.get_heading([ball.x, ball.y], player2.coordinates)
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    coef = 1/dist if dist > 1 else 1
    return [ball.x + coef*angle[0], ball.y + coef*angle[1]]


def get_vector_from_ball_to_target_point(ball, point: list):
    angle = ball.pitch.get_heading([ball.x, ball.y], point)
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    coef = 1/dist if dist > 1 else 1
    return [ball.x + coef*angle[0], ball.y + coef*angle[1]]


def find_defensive_coordinates(player):
    coors = {2: (int(0.9*player.pitch.size[0]),  0.3*int(player.pitch.size[1])),
             3: (int(0.9 * player.pitch.size[0]), 0.45 * int(player.pitch.size[1])),
             4: (int(0.9 * player.pitch.size[0]), 0.55 * int(player.pitch.size[1])),
             5: (int(0.9 * player.pitch.size[0]), 0.65 * int(player.pitch.size[1])),
             6: (int(0.8 * player.pitch.size[0]), 0.3 * int(player.pitch.size[1])),
             7: (int(0.8 * player.pitch.size[0]), 0.45 * int(player.pitch.size[1])),
             8: (int(0.8 * player.pitch.size[0]), 0.55 * int(player.pitch.size[1])),
             9: (int(0.8 * player.pitch.size[0]), 0.65 * int(player.pitch.size[1])),
             10: (int(0.70 * player.pitch.size[0]), 0.4 * int(player.pitch.size[1])),
             11: (int(0.70 * player.pitch.size[0]), 0.6 * int(player.pitch.size[1]))
             } if not player.host else\
            {2: (int(0.1*player.pitch.size[0]),  0.3*int(player.pitch.size[1])),
             3: (int(0.1 * player.pitch.size[0]), 0.45 * int(player.pitch.size[1])),
             4: (int(0.1 * player.pitch.size[0]), 0.55 * int(player.pitch.size[1])),
             5: (int(0.1 * player.pitch.size[0]), 0.65 * int(player.pitch.size[1])),
             6: (int(0.2 * player.pitch.size[0]), 0.3 * int(player.pitch.size[1])),
             7: (int(0.2 * player.pitch.size[0]), 0.45 * int(player.pitch.size[1])),
             8: (int(0.2 * player.pitch.size[0]), 0.55 * int(player.pitch.size[1])),
             9: (int(0.2 * player.pitch.size[0]), 0.65 * int(player.pitch.size[1])),
             10: (int(0.3 * player.pitch.size[0]), 0.4 * int(player.pitch.size[1])),
             11: (int(0.3 * player.pitch.size[0]), 0.6 * int(player.pitch.size[1]))
             }

    return [coors[player.id][0] + random.uniform(-movement_config["movement_noise"], movement_config["movement_noise"]),
            coors[player.id][1] + random.uniform(-movement_config["movement_noise"], movement_config["movement_noise"])]


def find_offensive_coordinates(player):
    coors = {2: (int(0.75 * player.pitch.size[0]), 0.15 * int(player.pitch.size[1])),
             3: (int(0.75 * player.pitch.size[0]), 0.35 * int(player.pitch.size[1])),
             4: (int(0.75 * player.pitch.size[0]), 0.65 * int(player.pitch.size[1])),
             5: (int(0.75 * player.pitch.size[0]), 0.88 * int(player.pitch.size[1])),
             6: (int(0.80 * player.pitch.size[0]), 0.10 * int(player.pitch.size[1])),
             7: (int(0.80 * player.pitch.size[0]), 0.40 * int(player.pitch.size[1])),
             8: (int(0.80 * player.pitch.size[0]), 0.65 * int(player.pitch.size[1])),
             9: (int(0.80 * player.pitch.size[0]), 0.80 * int(player.pitch.size[1])),
             10: (int(0.85 * player.pitch.size[0]), 0.4 * int(player.pitch.size[1])),
             11: (int(0.85 * player.pitch.size[0]), 0.8 * int(player.pitch.size[1]))
             } if player.host else \
        {2: (int(0.25 * player.pitch.size[0]), 0.15 * int(player.pitch.size[1])),
         3: (int(0.25 * player.pitch.size[0]), 0.35 * int(player.pitch.size[1])),
         4: (int(0.25 * player.pitch.size[0]), 0.65 * int(player.pitch.size[1])),
         5: (int(0.25 * player.pitch.size[0]), 0.88 * int(player.pitch.size[1])),
         6: (int(0.20 * player.pitch.size[0]), 0.10 * int(player.pitch.size[1])),
         7: (int(0.20 * player.pitch.size[0]), 0.40 * int(player.pitch.size[1])),
         8: (int(0.20 * player.pitch.size[0]), 0.65 * int(player.pitch.size[1])),
         9: (int(0.20 * player.pitch.size[0]), 0.80 * int(player.pitch.size[1])),
         10: (int(0.15 * player.pitch.size[0]), 0.4 * int(player.pitch.size[1])),
         11: (int(0.15 * player.pitch.size[0]), 0.8 * int(player.pitch.size[1]))
         }
    return [coors[player.id][0] + random.uniform(-movement_config["movement_noise"], movement_config["movement_noise"]),
            coors[player.id][1] + random.uniform(-movement_config["movement_noise"], movement_config["movement_noise"])]
