from src.Strategies.Deffensive import  can_tackle, tackle
from src.Strategies.Offensive import pass_ball, shall_pass, shall_shoot, shoot, shoot_possibility_function, \
    pass_ball_to_nearest, pass_ball_to_attacker
from src.Utils.Tags import StrategiesTag
from src.Utils.Helpers import find_enemy_teammates, has_ball, is_coords_valid, calc_dist_between_agent_and_point, \
    find_teammates
from src.Strategies.Movement import *
from src.Models.GoalKeeperAgent import GoalKeeperAgent

import random
import src.Strategies.Movement


class OffensiveAgent(AbstractAgent):

    COUNTER_MAX_VALUE = 20

    def __init__(self, idx, coordinates, speed, strategy, role, model, pitch, ball, host):
        super().__init__(idx, model)
        self.__coordinates = coordinates
        self.__speed = speed
        self.__strategy = strategy
        self.__role = role
        self.__id = idx
        self.__pitch = pitch
        self.__stop = False
        self.__ball = ball
        self.tackling = False
        self.host = host
        self.__pitch.place_agent(self, self.coordinates)
        self.__poses_ball = False
        self.__counter = {"value": 90, "vector": []}
        self.__counter_max_value = 90
        self.stop_counter = 0
        self.__stop_counter_max_value = 50

    def step(self):
        if self.stop:
            self.increment_stop_counter()

        elif self.__strategy == StrategiesTag.OFFENSIVE and not self.stop:
            if self.__has_ball():
                self.perform_action_with_ball()
            else:
                self.perform_action_without_ball()
        elif self.__strategy == StrategiesTag.DEFENSIVE and not self.stop:
            self.defend()

        self.pitch.move_agent(self, self.__coordinates)

    def perform_action_without_ball(self):
        num = random.uniform(0, 10)
        if num <= 9.5:
            self.__coordinates = self.move()
        else:
            pass

    def increment_stop_counter(self):
        if self.stop_counter == self.__stop_counter_max_value:
            self.stop_counter = 0
        else:
            self.stop_counter += 1

    def perform_action_with_ball(self):
        num = random.uniform(0, 100)
        if self.__shall_shoot() and self.__shall_pass():
            print("moge strzelac")
            print(num)
            print(shoot_possibility_function(self))
            if num <= shoot_possibility_function(self):
                self.__shoot()
            else:
                self.__pass_ball("to_nearest")
        elif self.__shall_shoot() and not self.__shall_pass():
            if num <= shoot_possibility_function(self):
                self.__shoot()
            else:
                self.__move_with_ball()
        elif not self.__shall_shoot() and self.__shall_pass():
            if num <= 80:
                self.__pass_ball("normal")
            else:
                self.__move_with_ball()
        else:
            self.__move_with_ball()

    def tackle(self):
        if tackle(self) == "winner":
            self.__pass_ball("to_atacker")

    def defend(self):
        if not self.can_tackle() and not self.tackling:
            self.__coordinates = self.move_to_defensive()

        elif self.can_tackle():
            self.tackle()

    def can_tackle(self):
        return can_tackle(self)

    def __move_with_ball(self):
        if not self.ball.action == "passing":
            if self.host:
                self.__coordinates = get_vector_to_point(self, [int(self.pitch.size[0]), int(self.pitch.size[1]/2)])
                self.__ball.move(self.__coordinates[0] + 5, self.__coordinates[1])
                self.pitch.move_agent(self.__ball, (self.__coordinates[0] + 1, self.__coordinates[1]))
            else:
                self.__coordinates = get_vector_to_point(self, [0, int(self.pitch.size[1]/2)])
                self.__ball.move(self.__coordinates[0] - 5, self.__coordinates[1])
                self.pitch.move_agent(self.__ball, (self.__coordinates[0] - 1, self.__coordinates[1]))

    def move(self):
        if self.__counter["value"] != self.__counter_max_value:
            new_cors = get_vector_to_point(self, self.__counter["vector"])
            self.__update_counter(None)
        else:
            coors = find_offensive_coordinates(self)
            self.__update_counter(coors)
            new_cors = get_vector_to_point(self, self.__counter["vector"])
        return new_cors

    def __update_counter(self, method):
        current_value = self.__counter["value"]
        current_vector = self.__counter["vector"]
        self.__counter["value"] = 0 if current_value == self.__counter_max_value else current_value + 1
        self.__counter["vector"] = method if method is not None else current_vector

    def move_to_defensive(self):
        if self.__counter["value"] != self.__counter_max_value:
            new_cors = get_vector_to_point(self, self.__counter["vector"])
            self.__update_counter(None)
        else:
            coors = find_defensive_coordinates(self)
            self.__update_counter(coors)
            new_cors = get_vector_to_point(self, self.__counter["vector"])
        return new_cors

    def reset_stop_counter(self):
        self.__counter["value"] = self.__counter_max_value

    def stop_tackling(self):
        teammates = find_teammates(self, 1000)
        for teammate in teammates:
            teammate.tackling = False
        self.tackling = False

    def __has_ball(self):
        return has_ball(self)

    def __shall_pass(self):
        return shall_pass(self)

    def __pass_ball(self, type):
        if type == "to_nerest":
            pass_ball_to_nearest(self)
        elif type == "to_atacker":
            pass_ball_to_attacker(self)
        else:
            pass_ball(self)

    def __shall_shoot(self):
        return shall_shoot(self)

    def __shoot(self):
        shoot(self)

    @property
    def id(self):
        return self.__id

    @property
    def coordinates(self):
        return self.__coordinates

    @property
    def ball(self):
        return self.__ball

    @property
    def poses_ball(self):
        return self.__poses_ball

    @property
    def pitch(self):
        return self.__pitch

    @property
    def speed(self):
        return self.__speed

    @property
    def strategy(self):
        return self.__strategy

    @property
    def stop(self):
        return self.__stop

    @property
    def role(self):
        return self.__role

    # @property
    # def host(self):
    #     return self.__host

    @id.setter
    def id(self, value):
        self.__id = value

    @role.setter
    def role(self, value):
        self.__role = value

    def change_strategy(self, value):
        teammates = find_teammates(self, 1000)
        for teammate in teammates:
            teammate.strategy = value
        self.__strategy = value

    @strategy.setter
    def strategy(self, value):
        self.__strategy = value

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @coordinates.setter
    def coordinates(self, value):
        self.__coordinates = value

    @ball.setter
    def ball(self, value):
        self.__ball = value

    # @host.setter
    # def host(self, value):
    #     self.__host = value

    @poses_ball.setter
    def poses_ball(self, value):
        self.__poses_ball = value

    @stop.setter
    def stop(self, value):
        self.__stop = value

    @pitch.setter
    def pitch(self, value):
        self.__pitch = value
        self.__pitch.place_agent(self, self.__coordinates)


