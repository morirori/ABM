from src.Utils.Helpers import find_closest_teammate, find_enemy_teammates, find_teammates, \
    calc_dist_between_agent_and_point, find_first_teammate
from src.Utils.config import passing_config, shooting_config

import random


def pass_ball(player):
        teammates = find_teammates(player, passing_config["teammates_around_radius"])
        free_teammates = [teammate for teammate in teammates if
                          len(find_enemy_teammates(teammate, passing_config["candidate_enemy_around_radius"])) == 0
                          and teammate.id != player.id]
        teammate = find_closest_teammate(player, free_teammates)
        player.ball.pass_(teammate)
        player.poses_ball = False
        teammate.poses_ball = True


def pass_ball_to_nearest(player):
    teammates = find_teammates(player, passing_config["teammates_around_radius"])
    teammate = find_closest_teammate(player, teammates)
    player.ball.pass_(teammate)
    player.poses_ball = False
    teammate.poses_ball = True


def pass_ball_to_attacker(player):
    teammates = find_teammates(player, passing_config["teammates_around_radius"])
    teammate = find_first_teammate(player, teammates)
    player.ball.pass_(teammate)
    player.poses_ball = False
    teammate.poses_ball = True


def shall_pass(player):
    enemies = find_enemy_teammates(player, passing_config["enemy_around_radius"])
    if not player.tackling:
        if len(enemies) != 0:
            teammates = find_teammates(player, passing_config["teammates_around_radius"])
#           TRUE if exist teammate without enemies around
            temp = []
            for teammate in teammates:
                if len(find_enemy_teammates(teammate, passing_config["candidate_enemy_around_radius"])) == 0\
                        and teammate.id != player.id:
                    temp.append(teammate)
            return True if len(temp) != 0 else False
        else:
            return False


def shall_shoot(player):
    if player.host:
        distance_to_gate = calc_dist_between_agent_and_point(player, [player.pitch.size[0], player.pitch.size[1]])
    else:
        distance_to_gate = calc_dist_between_agent_and_point(player, [0, player.pitch.size[1]/2])
    return True if distance_to_gate <= shooting_config["minimum_shooting_distance"] else False


def shoot_possibility_function(player):
    distance_to_gate = calc_dist_between_agent_and_point(player, [player.pitch.size[0], player.pitch.size[1]]) \
        if player.host else calc_dist_between_agent_and_point(player, [player.pitch.size[0], player.pitch.size[1]])

    normalized_distance = distance_to_gate/player.pitch.size[0]
    print((1 - normalized_distance)*100)
    return (1 - normalized_distance) * 100 if 1 - normalized_distance > 0.2 else 0


def shoot(player):
    if player.host:
        player.ball.shoot(player.pitch.size[0], player.pitch.size[1]/2 +
                          random.uniform(-shooting_config["shooting_accuracy"], shooting_config["shooting_accuracy"]))
    else:
        player.ball.shoot(0, player.pitch.size[1]/2 + random.uniform(-shooting_config["shooting_accuracy"], shooting_config["shooting_accuracy"]))

    player.poses_ball = False
