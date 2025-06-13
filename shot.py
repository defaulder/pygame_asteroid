import pygame
import circleshape
from constants import *


class Shot(circleshape.CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)


	def update(self, dt):
		self.position += self.velocity * dt
