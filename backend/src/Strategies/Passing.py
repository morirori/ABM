from src.Utils.Helpers import find_closest_teammate, find_enemy_teammates, find_teammates,\
    calc_dist_between_agent_and_point
import random


def pass_ball(player):
        teammates = find_teammates(player, 300)
        free_teammates = [teammate for teammate in teammates if len(find_enemy_teammates(teammate, 30)) == 0]
        teammate = find_closest_teammate(player, free_teammates)
        player.ball.pass_(teammate)
        player.poses_ball = False
        teammate.poses_ball = True


def shall_pass(player):
    radius = 30
    enemies = find_enemy_teammates(player, radius)
    if len(enemies) != 0:
        teammates = find_teammates(player, 300)
#           TRUE if exist teammate without enemies around
        temp = []
        for teammate in teammates:
            if len(find_enemy_teammates(teammate, 30)) == 0:
                temp.append(teammate)
        return True if len(temp) != 0 else False
    else:
        return False


def shall_shoot(player):
    print("mam pile", player.id)
    if player.host:
        distance_to_gate = calc_dist_between_agent_and_point(player, [player.pitch.size[0], player.pitch.size[1]])
    else:
        distance_to_gate = calc_dist_between_agent_and_point(player, [0, player.pitch.size[1]/2])

    print(distance_to_gate)
    print(0.3*player.pitch.size[0])
    return True if distance_to_gate <= 0.3*player.pitch.size[0] else False


def shoot(player):
    if player.host:
        player.ball.shoot(player.pitch.size[0], player.pitch.size[1]/2 + random.uniform(-20, 20))
    else:
        player.ball.shoot(0, player.pitch.size[1]/2 + random.uniform(-20, 20))

    player.poses_ball = False