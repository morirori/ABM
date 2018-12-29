from src.Abstracts.AbstractAgent import AbstractAgent
from src.Strategies.Movement import *
from mesa.space import ContinuousSpace
from src.Utils.Tags import StrategiesTag


class DefensiveAgent(AbstractAgent):

    def __init__(self, idx, coordinates, speed, strategy, role, model, pitch:ContinuousSpace, ball, host):
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

    def step(self):
        if self.__strategy == StrategiesTag.OFFENSIVE:
            if self.__coordinates[0] < 0.75 * self.pitch.x_max:
                new_coord = find_opt_coord(self)
                self.__coordinates = new_coord
        self.pitch.move_agent(self, self.__coordinates)

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
