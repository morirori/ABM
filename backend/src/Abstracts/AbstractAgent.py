from abc import ABCMeta, abstractmethod
from mesa import Agent


class AbstractAgent(Agent, metaclass=ABCMeta):
    # TODO define more parameters

    COUNTER_MAX_VALUE = 50

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    @abstractmethod
    def step(self):
        pass

    # @property
    # @abstractmethod
    # def host(self):
    #     pass

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

    @property
    @abstractmethod
    def stop(self):
        pass
