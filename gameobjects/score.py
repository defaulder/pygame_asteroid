import pygame
from .text import Text


class Score(Text):
    """to keep track of the score."""

    def __init__(self, *groups):
        Text.__init__(self, *groups)
        self.font.set_italic(1)
        self.__points = 0
        self.points = self.__points


    @property
    def points(self):
        return self.__points


    @points.setter
    def points(self, value):
        self.__points = value
        self.text = f"Score: {self.__points}"

