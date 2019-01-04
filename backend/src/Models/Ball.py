from mesa import Agent
from src.Strategies.Movement import get_vector_from_ball_to_target_player, get_vector_from_ball_to_target_point
import math


class Ball(Agent):
    def __init__(self, pitch, x, y, ):
        self.x = x
        self.y = y
        self.unique_id = 1
        self.pitch = pitch
        self.pitch.place_agent(self, (self.x, self.y))
        self.action = False
        self.target = None

    def step(self):
        if self.action == "passing":
            self.__passing()
        elif self.action == "shooting":
            self.__shooting()

    def to_json(self):
        return {
            "x": self.x,
            "y": self.y
        }

    def move(self, x, y):
        self.x = x
        self.y = y

    def pass_(self, target):
        self.target = target
        self.action = "passing"

    def __passing(self):
        new_cords = get_vector_from_ball_to_target_player(self, self.target)
        self.x = new_cords[0]
        self.y = new_cords[1]
        self.pitch.place_agent(self, (self.x, self.y))
        if self.__calc_dist_between_agent_and_ball(self.target) <= 10:
            self.target = None
            self.action = None

    def __shooting(self):
        new_cords = get_vector_from_ball_to_target_point(self, self.target)
        self.x = new_cords[0]
        self.y = new_cords[1]
        self.pitch.place_agent(self, (self.x, self.y))
        if self.__calc_dist_between_agent_and_point(self.target) <= 2:
            self.target = None
            self.action = None

    def shoot(self, x, y):
        self.target = [x, y]
        self.action = "shooting"

    def __calc_dist_between_agent_and_ball(self, agent):
        return math.sqrt(math.pow(self.x - agent.coordinates[0], 2)
                         + math.pow(self.y - agent.coordinates[1], 2))

    def __calc_dist_between_agent_and_point(self, point):
        return math.sqrt(math.pow(self.x - point[0], 2)
                         + math.pow(self.y - point[1], 2))


