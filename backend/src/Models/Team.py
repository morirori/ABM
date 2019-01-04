from mesa.time import RandomActivation
from src.Utils.Tags import AgentTag
from mesa import Model
from mesa.space import ContinuousSpace


class Team(Model):

    def __init__(self, strategy, host, pitch: ContinuousSpace):
        super().__init__()
        self.strategy = strategy
        self.host = host
        self.pitch = pitch
        self.schedule = RandomActivation(self)
        self.players = {
            AgentTag.GOALKEEPER: [],
            AgentTag.OFFENSIVE: []
        }

    def add_player(self, player_tag, player):
        temp_list = self.players[player_tag]
        temp_list.append(player)
        self.players[player_tag] = temp_list

    def step(self):
        self.schedule.step()

    def serialize(self):
        data = []
        for values in self.players.values():
            for item in values:
                data.append({
                    "id": item.id,
                    "x": item.coordinates[0],
                    "y": item.coordinates[1]
                })
        return data
