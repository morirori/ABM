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
            elif 2 <= i <= 5:
                player = PlayerFactory.create(AgentTag.DEFENSIVE, i,
                                              players_coordinates[AgentTag.DEFENSIVE][i-2], team, pitch, strategy, ball, host)
                team.add_player(AgentTag.DEFENSIVE, player)
                team.schedule.add(player)
            elif 6 <= i <= 9:
                player = PlayerFactory.create(AgentTag.MIDFIELDER, i,
                                              players_coordinates[AgentTag.MIDFIELDER][i-6], team, pitch, strategy, ball, host)
                team.add_player(AgentTag.MIDFIELDER, player)
                team.schedule.add(player)

            elif 10 <= i:
                player = PlayerFactory.create(AgentTag.OFFENSIVE, i,
                                              players_coordinates[AgentTag.OFFENSIVE][i - 10], team, pitch, strategy, ball, host)

                team.add_player(AgentTag.OFFENSIVE, player)
                team.schedule.add(player)
        team.schedule.add(ball)
        return team

    @staticmethod
    def __define_coordinates(size, host):
        if host:
            return {
                AgentTag.GOALKEEPER: [2, int(size[1] / 2)],
                AgentTag.DEFENSIVE: [[int(size[0] / 5),  int(size[1] / 6)],
                                     [int(size[0] / 5), int(2*size[1] / 6)],
                                     [int(size[0] / 5), int(4*size[1] / 6)],
                                     [int(size[0] / 5), int(5*size[1] / 6)]
                                     ],
                AgentTag.MIDFIELDER: [[int(size[0] / 3),  int(size[1] / 6)],
                                      [int(size[0] / 3), int(2*size[1] / 6)],
                                      [int(size[0] / 3), int(4*size[1] / 6)],
                                      [int(size[0] / 3), int(5*size[1] / 6)]
                                      ],
                AgentTag.OFFENSIVE: [[int(size[0] / 2),  int(size[1] / 2) - 25],
                                     [int(size[0] / 2), int(size[1] / 2) + 10]],
            }
        else:
            return {
                AgentTag.GOALKEEPER: [size[0]-2, int(size[1] / 2)],
                AgentTag.DEFENSIVE: [[4*int(size[0] / 5),  int(size[1] / 6)],
                                     [4*int(size[0] / 5), int(2*size[1] / 6)],
                                     [4*int(size[0] / 5), int(4*size[1] / 6)],
                                     [4*int(size[0] / 5), int(5*size[1] / 6)]
                                     ],
                AgentTag.MIDFIELDER: [[7*int(size[0] / 10),  int(size[1] / 6)],
                                      [7*int(size[0] / 10), int(2*size[1] / 6)],
                                      [7*int(size[0] / 10), int(size[1] / 2) + 20],
                                      [7*int(size[0] / 10), int(5*size[1] / 6)],
                                      ],
                AgentTag.OFFENSIVE: [[3*int(size[0] / 5),  int(size[1] / 2) - 35],
                                     [3*int(size[0] / 5), int(size[1] / 2) + 35]
                                     ],
            }
