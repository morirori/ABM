from src.Models.Ball import Ball


class BallFactory:

    @staticmethod
    def create(x, y):
        return Ball(x, y)
