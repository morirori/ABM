from src.Abstracts.AbstractAgent import AbstractAgent
from src.Utils.Tags import StrategiesTag
from src.Strategies.Movement import *
import random

class OffensiveAgent(AbstractAgent):

    def __init__(self, idx, coordinates, speed, strategy, role, model, pitch, ball, host):
        super().__init__(idx, model)
        self.__coordinates = coordinates
        self.__speed = speed
        self.__strategy = strategy
        self.__role = role
        self.__id = idx
        self.pitch = pitch
        self.ball = ball
        self.host = host
        self.pitch.place_agent(self, self.__coordinates)
        self.has_ball = False
        self.just_passed = 0

    def step(self):
        if self.just_passed:
            self.just_passed -= 1
        if self.has_ball:
            if random.randint(1, 100) <= 5:
                for neighbour in self.pitch.get_neighbors(tuple(self.__coordinates), 50):
                    try:
                        if neighbour.host and neighbour != self:
                            pass_to(self, neighbour)
                            self.has_ball = False
                            self.ball.free = True
                            self.just_passed = 5
                            return
                    except:
                        pass
            if self.__coordinates[0] > 0.85*self.pitch.size[0]:
                shoot(self.ball)
                self.has_ball = False
                self.ball.free = True
            self.__coordinates = move_forward(self)
            self.pitch.move_agent(self.ball, (self.__coordinates[0] + 5, self.__coordinates[1]))
            self.ball.move(self.__coordinates[0] + 5, self.__coordinates[1])
        elif self.ball in self.pitch.get_neighbors(tuple(self.__coordinates), 30) and self.ball.free \
                and self.just_passed == 0:
            self.__coordinates = move_to_ball(self)
            if self.ball in self.pitch.get_neighbors(tuple(self.__coordinates), 5):
                self.ball.free = False
                self.has_ball = True
                self.pitch.move_agent(self.ball, (self.__coordinates[0] + 5, self.__coordinates[1]))
                self.ball.move(self.__coordinates[0] + 5, self.__coordinates[1])
        else:
            for neighbour in self.pitch.get_neighbors(tuple(self.__coordinates), 30):
                try:
                    if neighbour.host and neighbour != self:
                        print("go away")
                        self.__coordinates = move_away(self, neighbour)
                        self.pitch.move_agent(self, self.__coordinates)
                        return
                except:
                    pass

            self.__coordinates = move_forward(self)
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
