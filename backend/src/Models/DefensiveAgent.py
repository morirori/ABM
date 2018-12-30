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
        self.__counter = {"value": 0, "method": "move_forward"}

    def step(self):
        if self.__strategy == StrategiesTag.OFFENSIVE:
            if self.__has_ball():
                self.perform_action_with_ball()
            else:
                self.perform_action_without_ball()
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
        teammates = find_teammates(self, 700)
        midd_field_teammates = [teammate for teammate in teammates if
                                (self.host and self.coordinates[0] < teammate.coordinates[0] and isinstance(teammate, MiddleFielderAgent))
                                or (not self.host and self.coordinates[0] > teammate.coordinates[0] and isinstance(teammate, MiddleFielderAgent))]

        valid = False
        new_coords = []
        while not valid:
            if len(midd_field_teammates) != 0:
                new_coords = self.__attack()
                valid = True if is_coords_valid(self, new_coords) else False
            else:
                new_coords = self.__move_backward()
                valid = True if is_coords_valid(self, new_coords) else False
        return new_coords

    def __attack(self):
        num = random.uniform(0, 10)

        if self.__counter["value"] < DefensiveAgent.COUNTER_MAX_VALUE:
            method_to_call = getattr(src.Strategies.Movement, self.__counter["method"])
            self.__update_counter(None)
            return method_to_call(self)
        elif num <= 9:
            DefensiveAgent.COUNTER_MAX_VALUE = 15
            return self.__move_forward()
        else:
            DefensiveAgent.COUNTER_MAX_VALUE = 5
            return self.__move_backward()

    def __move_forward(self):
        num = random.uniform(0, 10)
        if num <= 8:
            coordinates = move_forward(self)
            self.__update_counter("move_forward")
        elif 8 < num <= 9:
            coordinates = move_forward_towards_middle_filed(self)
            self.__update_counter("move_forward_towards_middle_filed")
        else:
            coordinates = move_forward_towards_side_line(self)
            self.__update_counter("move_forward_towards_side_line")
        return coordinates

    def __move_backward(self):
        num = random.uniform(0, 10)
        if num <= 4:
            coordinates = move_backward(self)
            self.__update_counter("move_backward")
        elif 4 < num <= 7:
            coordinates = move_backward_towards_middle_filed(self)
            self.__update_counter("move_backward_towards_middle_filed")
        else:
            coordinates = move_backward_towards_side_line(self)
            self.__update_counter("move_backward_towards_side_line")
        return coordinates

    def __update_counter(self, method):
        current_value = self.__counter["value"]
        current_method = self.__counter["method"]
        self.__counter["value"] = 0 if current_value == DefensiveAgent.COUNTER_MAX_VALUE else current_value + 1
        self.__counter["method"] = method if method is not None else current_method

    def __move_with_ball(self):
        if not self.ball.action == "passing":
            self.__coordinates = self.move()
            self.__ball.move(self.__coordinates[0] + 5, self.__coordinates[1])
            self.pitch.move_agent(self.__ball, (self.__coordinates[0] + 1, self.__coordinates[1]))

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

