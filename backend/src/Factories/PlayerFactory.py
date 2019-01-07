from src.Utils.Tags import AgentTag
from src.Models.GoalKeeperAgent import GoalKeeperAgent
from src.Models.OffensiveAgent import OffensiveAgent


class PlayerFactory:

    @staticmethod
    def create(player_tag, idx, coordinates: list, model, pitch, strategy, ball, host):

        if player_tag == AgentTag.GOALKEEPER:
            return GoalKeeperAgent(idx, coordinates, 0.4, strategy, 0, model, pitch, ball, host)

        elif player_tag == AgentTag.OFFENSIVE:
            return OffensiveAgent(idx, coordinates, 1, strategy, 0, model, pitch, ball, host)

