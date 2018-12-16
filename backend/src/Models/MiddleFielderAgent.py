from src.Abstracts.AbstractAgent import AbstractAgent
from src.Utils.Tags import StrategiesTag
from src.Strategies.Movement import move_forward, move_to_ball
from math import sqrt


class MiddleFielderAgent(AbstractAgent):

    def __init__(self, idx, coordinates, speed, strategy, role, model, pitch, ball):
        super().__init__(idx, model)
        self.__coordinates = coordinates
        self.__speed = speed
        self.__strategy = strategy
        self.__role = role
        self.__id = idx
        self.pitch = pitch
        self.ball = ball
        self.pitch.place_agent(self, self.__coordinates)

    def step(self):
        if self.__strategy == StrategiesTag.OFFENSIVE:
            if self.__coordinates[0] < 0.75 * self.pitch.x_max:
                new_coord = move_forward(self)
                self.__coordinates = new_coord
        else:
            if self.ball in self.pitch.get_neighbors(self.__coordinates, 50):
                new_coord = move_to_ball(self)
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
