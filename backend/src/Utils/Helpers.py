from src.Models.Ball import Ball
import math


def calc_dist_between_agents(agent1, agent2):
    return math.sqrt(math.pow(agent1.coordinates[0] - agent2.coordinates[0], 2)
                     + math.pow(agent1.coordinates[1] - agent2.coordinates[1], 2))


def calc_dist_between_agent_and_ball(ball, agent):
    return math.sqrt(math.pow(ball.x - agent.coordinates[0], 2)
                     + math.pow(ball.y - agent.coordinates[1], 2))


def calc_dist_between_agent_and_point(agent, point):
    return math.sqrt(math.pow(agent.coordinates[0] - point[0], 2)
                     + math.pow(agent.coordinates[1] - point[1], 2))


def find_closest_teammate(player1, teammates: list):
    smallest_dist = 9999999999
    to_return = None
    for teammate in teammates:
        temp = calc_dist_between_agents(player1, teammate)
        if temp < smallest_dist:
            smallest_dist = temp
            to_return = teammate
    print(to_return)
    return to_return


def find_enemy_teammates(player, radius):
        neighbours = player.pitch.get_neighbors(tuple(player.coordinates), radius)
        return [neighbour for neighbour in neighbours
                if not isinstance(neighbour, Ball) and neighbour.host != player.host]


def find_teammates(player, radius):
        neighbours = player.pitch.get_neighbors(tuple(player.coordinates), radius)
        return [neighbour for neighbour in neighbours
                if not isinstance(neighbour, Ball) and neighbour.host == player.host]


def has_ball(player):
    neighbours = find_enemy_teammates(player, 30)
    teammates = find_teammates(player, 30)
    enemy_with_ball = [neighbour for neighbour in neighbours if neighbour.poses_ball]
    teammates_with_ball = [teammate for teammate in teammates if teammate.poses_ball]
    distance_to_ball = calc_dist_between_agent_and_ball(player.ball, player)

    if player.poses_ball:
        return True
    elif distance_to_ball <= 10 and len(enemy_with_ball) == 0 \
            and len(teammates_with_ball) == 0 and not player.ball.action == "passing":
        player.poses_ball = True
        return True
    return False


def is_coords_valid(player, new_coords):
    return True if 0 <= new_coords[0] <= player.pitch.size[0] and 0 <= new_coords[1] <= player.pitch.size[1]\
        else False


def find_first_teammate(player, teammates: list):
    if player.host:
        return find_first_teammate_if_host(player, teammates)
    else:
        return find_first_teammate_if_not_host(player, teammates)


def find_first_teammate_if_host(player, teammates: list):
    dist = 0
    to_return = None
    for teammate in teammates:
        if teammate.coordinates[0] > dist:
            dist = teammate.coordinates[0]
            to_return = teammate

    return to_return if to_return.coordinates[0] > player.coordinates[0] else player


def find_first_teammate_if_not_host(player, teammates: list):
    dist = player.pitch.size[0]
    to_return = None
    for teammate in teammates:
        if teammate.coordinates[0] < dist:
            dist = teammate.coordinates[0]
            to_return = teammate
    return to_return if to_return.coordinates[0] < player.coordinates[0] else player
