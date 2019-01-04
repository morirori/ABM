from src.Utils.Helpers import find_closest_teammate, find_enemy_teammates, find_teammates, \
    calc_dist_between_agent_and_point, find_first_teammate
import random


def pass_ball(player):
        teammates = find_teammates(player, 400)
        free_teammates = [teammate for teammate in teammates if len(find_enemy_teammates(teammate, 100)) == 0]
        teammate = find_closest_teammate(player, free_teammates)
        player.ball.pass_(teammate)
        player.poses_ball = False
        teammate.poses_ball = True


def pass_ball_to_nearest(player):
    teammates = find_teammates(player, 400)
    teammate = find_closest_teammate(player, teammates)
    player.ball.pass_(teammate)
    player.poses_ball = False
    teammate.poses_ball = True


def pass_ball_to_attacker(player):
    teammates = find_teammates(player, 110)
    teammate = find_first_teammate(player, teammates)
    player.ball.pass_(teammate)
    player.poses_ball = False
    teammate.poses_ball = True


def shall_pass(player):
    radius = 100
    enemies = find_enemy_teammates(player, radius)
    if not player.tackling:
        if len(enemies) != 0:
            teammates = find_teammates(player, 400)
#           TRUE if exist teammate without enemies around
            temp = []
            for teammate in teammates:
                if len(find_enemy_teammates(teammate, 100)) == 0:
                    temp.append(teammate)
            return True if len(temp) != 0 else False
        else:
            return False


def shall_shoot(player):
    if player.host:
        distance_to_gate = calc_dist_between_agent_and_point(player, [player.pitch.size[0], player.pitch.size[1]])
    else:
        distance_to_gate = calc_dist_between_agent_and_point(player, [0, player.pitch.size[1]/2])
    return True if distance_to_gate <= 250 else False


def shoot_possibility_function(player):
    distance_to_gate = calc_dist_between_agent_and_point(player, [player.pitch.size[0], player.pitch.size[1]]) \
        if player.host else calc_dist_between_agent_and_point(player, [player.pitch.size[0], player.pitch.size[1]])

    normalized_distance = distance_to_gate/player.pitch.size[0]
    return (1 - normalized_distance) * 100 if 1 - normalized_distance > 0.2 else 0


def shoot(player):
    if player.host:
        player.ball.shoot(player.pitch.size[0], player.pitch.size[1]/2 + random.uniform(-150, 150))
    else:
        player.ball.shoot(0, player.pitch.size[1]/2 + random.uniform(-150, 150))

    player.poses_ball = False
