from src.Abstracts.AbstractAgent import AbstractAgent


def move_forward(player: AbstractAgent):
    temp = player.coordinates
    player.coordinates[0] = temp[0] + 0.1
    player.coordinates[1] = temp[1]
