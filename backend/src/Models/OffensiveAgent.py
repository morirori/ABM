from src.Abstracts.AbstractAgent import AbstractAgent
from src.Utils.Tags import StrategiesTag
from src.Strategies.Movement import *
from src.Models.Ball import Ball


class OffensiveAgent(AbstractAgent):

    def __init__(self, idx, coordinates, speed, strategy, role, model, pitch, ball, host):
        super().__init__(idx, model)
        self.__coordinates = coordinates
        self.__speed = speed
        self.__strategy = strategy
        self.__role = role
        self.__id = idx
        self.__pitch = pitch
        self.__ball = ball
        self.host = host
        self.__pitch.place_agent(self, self.__coordinates)
        self.__poses_ball = False

    def step(self):
        if self.__strategy == StrategiesTag.OFFENSIVE:
            if self.__has_ball():
                print("id", self.id)
                self.__move_with_ball()
            else:
                self.__coordinates = find_opt_coord(self)

        self.pitch.move_agent(self, self.__coordinates)

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
    def role(self):
        return self.__role

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

    def __has_ball(self):
        neighbours = self.__find_enemy_teammates(10)
        teammates = self.__find_teammates(10)
        enemy_with_ball = [neighbour for neighbour in neighbours if neighbour.poses_ball]
        teammates_with_ball = [teammate for teammate in teammates if teammate.poses_ball]

        if self.poses_ball:
            return True
        elif self.ball in self.pitch.get_neighbors(tuple(self.__coordinates), 10) and len(enemy_with_ball) == 0 \
                and len(teammates_with_ball) == 0:
            self.poses_ball = True
            return True

        return False

    def __find_enemy_teammates(self, radius):
        neighbours = self.pitch.get_neighbors(tuple(self.__coordinates), radius)
        return [neighbour for neighbour in neighbours
                if not isinstance(neighbour, Ball) and neighbour.host != self.host]

    def __find_teammates(self, radius):
        neighbours = self.pitch.get_neighbors(tuple(self.__coordinates), radius)
        return [neighbour for neighbour in neighbours
                if not isinstance(neighbour, Ball) and neighbour.host == self.host]

    def __move_with_ball(self):
        self.__coordinates = move_forward(self)
        self.ball.move(self.__coordinates[0] + 5, self.__coordinates[1])
        self.pitch.move_agent(self.ball, (self.__coordinates[0] + 1, self.__coordinates[1]))
