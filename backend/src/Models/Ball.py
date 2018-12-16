from mesa import Agent


class Ball(Agent):
    def __init__(self, pitch, x, y, ):
        self.x = x
        self.y = y
        self.unique_id = 1
        self.pitch = pitch
        self.pitch.place_agent(self, (self.x, self.y))

    def step(self):
        #self.pitch.place_agent(self, (self.x, self.y))
        pass

    def to_json(self):
        return {
            "x": self.x,
            "y": self.y
        }

    def move(self, x, y):
        self.x = x
        self.y = y


