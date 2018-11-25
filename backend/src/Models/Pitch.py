class Pitch:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.borders = dict()


class Border:
    def __init__(self, size, direction):
        self.size = size
        self.direction = direction
