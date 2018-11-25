from enum import Enum


class AgentTag(Enum):

    OFFENSIVE = "offensive"
    DEFENSIVE = "defensive"
    MIDFIELDER = "midfielder"
    GOALKEEPER = "goal_keeper"


class StrategiesTag(Enum):

    OFFENSIVE = "offensive"
    DEFENSIVE = "defensive"


class DirectionTag(Enum):

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
