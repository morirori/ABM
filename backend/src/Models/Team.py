from src.Controllers import PlayerController


class Team:

    def __init__(self, strategy, controller: PlayerController, host):
        self.strategy = strategy
        self.player_controller = controller
        self.host = host

    def play(self):
        # TODO its temporary implementation
        self.player_controller.play()