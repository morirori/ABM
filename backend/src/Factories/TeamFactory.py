from src.Factories.PlayerFactory import PlayerFactory
from src.Utils.Tags import AgentTag
from src.Models.Team import Team


class TeamFactory:

    @staticmethod
    def create(strategy, host, size: list, pitch, ball):
        team_size = 11
        players_coordinates = TeamFactory.__define_coordinates(size, host)
        team = Team(strategy, host, pitch)
        for i in range(1, team_size+1):
            if i == 1:
                player = PlayerFactory.create(AgentTag.GOALKEEPER, i,
                                              players_coordinates[AgentTag.GOALKEEPER], team, pitch, strategy, ball, host)
                team.add_player(AgentTag.GOALKEEPER, player)
                team.schedule.add(player)
            else:
                player = PlayerFactory.create(AgentTag.OFFENSIVE, i,
                                              players_coordinates[AgentTag.OFFENSIVE][i-2], team, pitch, strategy, ball, host)
                team.add_player(AgentTag.OFFENSIVE, player)
                team.schedule.add(player)
        team.schedule.add(ball)
        return team

    @staticmethod
    def __define_coordinates(size, host):
        if host:
            return {
                AgentTag.GOALKEEPER: [2, int(size[1] / 2)],
                AgentTag.OFFENSIVE: [[int(size[0] / 5),  int(size[1] / 6)],
                                     [int(size[0] / 5), int(2*size[1] / 6)],
                                     [int(size[0] / 5), int(4*size[1] / 6)],
                                     [int(size[0] / 5), int(5*size[1] / 6)],
                                     [int(size[0] / 3),  int(size[1] / 6)],
                                     [int(size[0] / 3), int(2*size[1] / 6)],
                                     [int(size[0] / 3), int(4*size[1] / 6)],
                                     [int(size[0] / 3), int(5*size[1] / 6)],
                                     [int(size[0] / 2),  int(size[1] / 2) - 25],
                                     [int(size[0] / 2), int(size[1] / 2) + 10]],
            }
        else:
            return {
                AgentTag.GOALKEEPER: [size[0]-2, int(size[1] / 2)],
                AgentTag.OFFENSIVE: [[0.85*int(size[0]),  int(size[1] / 6)],
                                     [0.85*int(size[0]), int(2*size[1] / 6)],
                                     [0.85*int(size[0]), int(4*size[1] / 6)],
                                     [0.85*int(size[0]), int(5*size[1] / 6)],
                                     [7*int(size[0] / 10),  int(size[1] / 6)],
                                     [7*int(size[0] / 10), int(2*size[1] / 6)],
                                     [7*int(size[0] / 10), int(size[1] / 2) + 20],
                                     [7*int(size[0] / 10), int(5*size[1] / 6)],
                                     [3*int(size[0] / 5),  int(size[1] / 2) - 35],
                                     [3*int(size[0] / 5), int(size[1] / 2) + 35]
                                     ],
            }
