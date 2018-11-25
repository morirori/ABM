from src.Utils.Tags import AgentTag
from random import randint


class PlayerController:

    # TODO define methods which can manage all players
    def __init__(self):
        self.players = {
            AgentTag.GOALKEEPER: [],
            AgentTag.DEFENSIVE: [],
            AgentTag.MIDFIELDER: [],
            AgentTag.OFFENSIVE: []
        }

    def add_player(self, player_tag, player):
        temp_list = self.players[player_tag]
        temp_list.append(player)
        self.players[player_tag] = temp_list

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

    def play(self):
        # TODO it is temporary implementation
        for agents in self.players.values():
            for agent in agents:
                temp = agent.coordinates
                agent.coordinates[0] = temp[0] + randint(-10, 10)
                agent.coordinates[1] = temp[1] + randint(-10, 10)

    def print(self):
        print(self.players)
