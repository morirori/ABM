from src.Abstracts.AbstractAgent import AbstractAgent
from src.Models import OffensiveAgent
from math import sqrt
from src.Utils.Tags import StrategiesTag


def sign(a):
    return 1 - 2 * (a <= 0)

def get_vector_to_point(player: AbstractAgent, coord):
    angle = player.pitch.get_heading(player.coordinates, [coord[0], coord[1]])
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    if dist > player.speed:
        coef = player.speed/dist
    else:
        coef = 1
    temp = [player.coordinates[0] + coef*angle[0], player.coordinates[1] + coef*angle[1]]

    return temp

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


def move_away(pl1, pl2):
    angle = pl1.pitch.get_heading(pl1.coordinates, pl2.coordinates)
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    if dist > 5:
        coef = 0.5 / dist
    else:
        coef = 0
    temp = [pl1.coordinates[0] + abs(coef * angle[0]), pl1.coordinates[1] - coef * angle[1]]
    return temp


def vec_away(player: OffensiveAgent):
    vectors = []
    for neighbour in player.pitch.get_neighbors(tuple(player.__coordinates), 100):
        if neighbour != player.ball and neighbour != player:
            angle = player.pitch.get_heading(neighbour.coordinates, player.coordinates)
            dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
            if dist > 5:
                coef = 20 / dist
            else:
                coef = 4

            if abs(angle[0]) >= 1 and abs(angle[1]) >= 1:
                div = abs(angle[0]) / abs(angle[1])
                vectors.append([sign(angle[0]) * div * coef/sqrt(div+1), sign(angle[1]) * coef/sqrt(div+1)])
            elif abs(angle[0]) <= 1 and abs(angle[1]) <= 1:
                vectors.append([sqrt(coef), sqrt(coef)])
            elif abs(angle[1]) <= 1:
                vectors.append([sign(angle[0]) * coef, 0])
            else:
                vectors.append([0, sign(angle[1]) * coef])

            vectors.append([coef * angle[0], coef * angle[1]])
    if vectors:
        return map(sum, zip(*vectors))
    return [0, 0]


def vec_to_ball(player: OffensiveAgent):
    angle = player.pitch.get_heading(player.coordinates, (player.ball.x, player.ball.y))
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    if dist > 5:
        coef = 20 / dist
    else:
        coef = 4

    if abs(angle[0]) >= 1 and abs(angle[1]) >= 1:
        div = abs(angle[0]) / abs(angle[1])
        return [sign(angle[0]) * div * coef / sqrt(div + 1), sign(angle[1]) * coef / sqrt(div + 1)]
    elif abs(angle[0]) <= 1 and abs(angle[1]) <= 1:
        return [sqrt(coef), sqrt(coef)]
    elif abs(angle[1]) <= 1:
        return [sign(angle[0]) * coef, 0]
    else:
        return [0, sign(angle[1]) * coef]

##################
# general best coordinates for each player
##################

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
        return get_vector_to_point(player, (int(player.pitch.size[0] * 0.85), int(player.pitch.size[1]/8 * 7)))

    elif player.id == 10 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] * 0.85), int(player.pitch.size[1]/2 + 20)))
    elif player.id == 11 and player.host:
        return get_vector_to_point(player, (int(player.pitch.size[0] * 0.85), int(player.pitch.size[1]/2 - 20)))

    elif player.id == 3 and  not player.host:
        return get_vector_to_point(player, (4*int(player.pitch.size[0] / 5), int(2*player.pitch.size[1] / 6)))
    elif player.id == 4 and not player.host:
        return get_vector_to_point(player, (4*int(player.pitch.size[0] / 5), int(4*player.pitch.size[1] / 6)))

    else:
        return player.coordinates


#####################
# Ball movements
#####################


def shoot(ball: AbstractAgent):
    angle = ball.pitch.get_heading((ball.x, ball.y), (ball.pitch.size[0], ball.y))
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    if dist > 5:
        coef = 0.7/dist
    else:
        coef = 0
    ball.direction = coef*angle[0], coef*angle[1]


def pass_to(pl1, pl2):
    angle = pl1.pitch.get_heading(pl1.coordinates, pl2.coordinates)
    dist = sqrt(angle[0] ** 2 + angle[1] ** 2)
    if dist > 5:
        coef = 0.5 / dist
    else:
        coef = 0
    pl1.ball.direction = coef * angle[0], coef * angle[1]
