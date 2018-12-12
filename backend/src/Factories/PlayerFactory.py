from src.Utils.Tags import AgentTag
from src.Models.DefensiveAgent import DefensiveAgent
from src.Models.GoalKeeperAgent import GoalKeeperAgent
from src.Models.MiddleFielderAgent import MiddleFielderAgent
from src.Models.OffensiveAgent import OffensiveAgent


class PlayerFactory:

    @staticmethod
    def create(player_tag, idx, coordinates: list, model, pitch):
        if player_tag == AgentTag.MIDFIELDER:
            return MiddleFielderAgent(idx, coordinates, 0, 0, 0, model, pitch)

        elif player_tag == AgentTag.GOALKEEPER:
            return GoalKeeperAgent(idx, coordinates, 0, 0, 0, model, pitch)

        elif player_tag == AgentTag.DEFENSIVE:
            return DefensiveAgent(idx, coordinates, 0, 0, 0, model, pitch)

        if player_tag == AgentTag.OFFENSIVE:
            return OffensiveAgent(idx, coordinates, 0, 0, 0, model, pitch)

