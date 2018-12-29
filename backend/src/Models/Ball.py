from mesa import Agent


class Ball(Agent):
    def __init__(self, pitch, x, y, ):
        self.x = x
        self.y = y
        self.unique_id = 1
        self.pitch = pitch
        self.pitch.place_agent(self, (self.x, self.y))
        self.direction = (0, 0)
        self.free = True

    def step(self):
        if not self.free:
            if self.x > self.pitch.size[0] - 5 or self.x < 5 or self.y < 5 or self.y > self.pitch.size[1] - 5:
                self.direction = (0, 0)
        if self. free and self.direction != (0, 0):
            self.pitch.move_agent(self, (self.x + self.direction[0], self.y + self.direction[1]))
            self.x = self.x + self.direction[0]
            self.y = self.y + self.direction[1]
        else:
            pass

    def to_json(self):
        return {
            "x": self.x,
            "y": self.y
        }

    def move(self, x, y):
        self.x = x
        self.y = y


