from src.Factories.BallFactory import BallFactory
from src.Factories.TeamFactory import TeamFactory
from src.Utils.Tags import StrategiesTag
from mesa.space import ContinuousSpace


class MatchSingleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Match(metaclass=MatchSingleton):

    def __init__(self):
        self.time = 0
        self.team_home = None
        self.team_away = None
        self.ball = None
        self.objects = {"ball": self.ball, "team_home": self.team_home, "team_away": self.team_away}
        self.pitch = None
        self.running = False

    def handle(self, command, x, y):
        if command == 'init':
            self.initialize(x, y)
        elif command == 'start':
            self.enable()
        elif command == 'restart':
            self.disable()
            self.initialize(x, y)
        elif command == 'pause':
            self.disable()
        else:
            raise Exception('Unsupported command!')

    def initialize(self, x, y):
        self.time = 0
        self.pitch = ContinuousSpace(x, y, torus=True)
        print("hello")
        self.ball = BallFactory.create(int(x / 2), int(y / 2), self.pitch)
        print("there")
        self.team_home = TeamFactory.create(StrategiesTag.OFFENSIVE, True, [x, y], self.pitch, self.ball)
        self.team_away = TeamFactory.create(StrategiesTag.DEFENSIVE, False, [x, y], self.pitch, self.ball)

        print(self.ball)
        self.objects["ball"] = self.ball
        self.objects["team_away"] = self.team_away
        self.objects["team_home"] = self.team_home

    def enable(self):
        self.running = True

    def disable(self):
        self.running = False

    def process(self):
        if not self.running:
            return
        self.time += 1
        for key, value in self.objects.items():
            value.step()
