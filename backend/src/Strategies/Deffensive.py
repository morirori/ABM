from src.Abstracts.AbstractAgent import  AbstractAgent
from src.Strategies.Movement import get_vector_to_point
import random

from src.Utils.Helpers import calc_dist_between_agent_and_point, find_enemy_teammates, calc_dist_between_agents
from src.Utils.Tags import StrategiesTag


def can_tackle(player):
    enemies = find_enemy_teammates(player, 60)
    enemy_with_ball = [enemy for enemy in enemies if enemy.poses_ball]
    if len(enemy_with_ball) != 0:
        print("plaeyt," , player.id, "atakuje", enemy_with_ball[0].id)
        return True
    return False


def tackle(defender: AbstractAgent):
    enemies = find_enemy_teammates(defender, 110)
    enemy_with_ball = [enemy for enemy in enemies if enemy.poses_ball][0]

    rand = random.uniform(0, 10)
    enemy_with_ball.tackling = True
    defender.tackling = True
    enemy_with_ball_cors = [enemy_with_ball.coordinates[0] + 5, enemy_with_ball.coordinates[1]] if enemy_with_ball.host \
        else [enemy_with_ball.coordinates[0] - 5, enemy_with_ball.coordinates[1]]
    defender.coordinates = get_vector_to_point(defender, enemy_with_ball_cors)

    print("plaeyt]f]as,", defender.id, "atakuje", enemy_with_ball.id)
    if calc_dist_between_agents(defender, enemy_with_ball) < 10:
        print("pojedynek")
        #atacker won
        if rand < 7:
            defender.stop = True
            defender.stop_counter = 0
            enemy_with_ball.tackling = False
            defender.tackling = False

        else:
            #TODO CHANGE STRATEGY FOR ALL TEAMMATES
            enemy_with_ball.stop = True
            enemy_with_ball.stop_counter = 0
            defender.change_strategy(StrategiesTag.OFFENSIVE)
            defender.poses_ball = True
            enemy_with_ball.tackling = False
            defender.tackling = False
            enemy_with_ball.change_strategy(StrategiesTag.DEFENSIVE)
            enemy_with_ball.poses_ball = False
