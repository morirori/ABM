from abc import ABCMeta, abstractmethod
from mesa import Agent


class AbstractAgent(Agent, metaclass=ABCMeta):
    # TODO define more parameters

    @abstractmethod
    def step(self):
        pass

    @property
    @abstractmethod
    def coordinates(self):
        pass

    def get_coordinates(self):
        return self.__coordinates

    @property
    @abstractmethod
    def speed(self):
        pass

    @property
    @abstractmethod
    def strategy(self):
        pass

    @property
    @abstractmethod
    def role(self):
        pass

    @property
    @abstractmethod
    def id(self):
        pass

