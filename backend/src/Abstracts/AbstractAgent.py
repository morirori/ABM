from abc import ABCMeta, abstractmethod


class AbstractAgent(metaclass=ABCMeta):
    # TODO define more parameters

    @property
    @abstractmethod
    def coordinates(self):
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

