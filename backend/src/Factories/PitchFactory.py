from src.Models.Pitch import Pitch, Border
from src.Utils.Tags import DirectionTag


class PitchFactory:

    @staticmethod
    def create(width, height):
        rectangle = Pitch(width, height)
        PitchFactory.__set_borders(width, height, rectangle)
        return rectangle

    @staticmethod
    def __set_borders(width, height, rectangle):
        rectangle.borders["upper_border"] = Border(width, DirectionTag.HORIZONTAL)
        rectangle.borders["bottom_border"] = Border(width, DirectionTag.HORIZONTAL)
        rectangle.borders["left_border"] = Border(height, DirectionTag.VERTICAL)
        rectangle.borders["right_border"] = Border(height, DirectionTag.VERTICAL)
        return rectangle
