from mesa.space import ContinuousSpace
from src.Utils.Tags import StrategiesTag
from src.Strategies.Movement import *
import random
from src.Models.MiddleFielderAgent import MiddleFielderAgent
import src.Strategies.Movement
from src.Strategies.Passing import *
from src.Utils.Helpers import find_teammates, has_ball, is_coords_valid


class DefensiveAgent(AbstractAgent):
    def __init__(self, idx, coordinates, speed, strategy, role, model, pitch: ContinuousSpace, ball, host):
        super().__init__(idx, model)
        self.__coordinates = coordinates
        self.__speed = speed
        self.__strategy = strategy
        self.__role = role
        self.__id = idx
        self.host = host
        self.__pitch = pitch
        self.pitch.place_agent(self, self.__coordinates)
        self.__ball = ball
        self.__poses_ball = False
        self.__stop = False
        self.__counter = {"value": 30, "vector": []}
        self.__counter_max_value = 30

    def step(self):
        if self.__strategy == StrategiesTag.OFFENSIVE:
            if self.__has_ball():
                self.perform_action_with_ball()
            else:
                self.perform_action_without_ball()
        else:
            self.move_to_defensive()
        self.pitch.move_agent(self, self.__coordinates)

    def perform_action_without_ball(self):
        num = random.uniform(0, 10)
        if num <= 6:
            self.__coordinates = self.move()
        else:
            pass

    def perform_action_with_ball(self):
        num = random.uniform(0, 10)
        if self.__shall_shoot() and self.__shall_pass():
            if num <= 5:
                self.__shoot()
            elif num < 5 <= 9:
                self.__pass_ball()
            else:
                self.__move_with_ball()
        elif self.__shall_shoot() and not self.__shall_pass():
            if num <=8:
                self.__shoot()
            else:
                self.__move_with_ball()
        elif not self.__shall_shoot() and not self.__shall_pass():
            if num <= 8:
                self.__pass_ball()
            else:
                self.__move_with_ball()
        else:
            self.__move_with_ball()

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

    def __move_with_ball(self):
        if not self.ball.action == "passing":
            self.__coordinates = self.move()
            self.__ball.move(self.__coordinates[0] + 5, self.__coordinates[1])
            self.pitch.move_agent(self.__ball, (self.__coordinates[0] + 1, self.__coordinates[1]))

    def move_to_defensive(self):
        self.__coordinates = find_defensive_coordinates(self)

    def __has_ball(self):
        return has_ball(self)

    def __shall_pass(self):
        return shall_pass(self)

    def __pass_ball(self):
        print("podaje", self.id)
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
    def speed(self):
        return self.__speed

    @property
    def strategy(self):
        return self.__strategy

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
    def role(self):
        return self.__role

    @property
    def stop(self):
        return self.__stop

    @id.setter
    def id(self, value):
        self.__id = value

    @role.setter
    def role(self, value):
        self.__role = value

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

    @poses_ball.setter
    def poses_ball(self, value):
        self.__poses_ball = value

    @pitch.setter
    def pitch(self, value):
        self.__pitch = value
        self.__pitch.place_agent(self, self.__coordinates)

    @stop.setter
    def stop(self, value):
        self.__stop = value



