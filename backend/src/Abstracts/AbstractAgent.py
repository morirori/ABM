from abc import ABCMeta, abstractmethod
from mesa import Agent


class AbstractAgent(Agent, metaclass=ABCMeta):
    # TODO define more parameters

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.__coordinates = None

    @abstractmethod
    def step(self):
        pass

    @property
    @abstractmethod
    def coordinates(self):
        pass

    @property
    @abstractmethod
    def poses_ball(self):
        pass

    @property
    @abstractmethod
    def ball(self):
        pass

    @property
    @abstractmethod
    def pitch(self):
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



