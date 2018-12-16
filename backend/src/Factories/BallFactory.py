from src.Models.Ball import Ball


class BallFactory:

    @staticmethod
    def create(x, y, pitch):
        ball = Ball(pitch, x, y)
        print("factory:", ball)
        return ball
