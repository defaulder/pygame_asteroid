import circleshape
import random
import pygame
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)


	def update(self, dt):
		self.position += self.velocity * dt


	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		new_radius = self.radius - ASTEROID_MIN_RADIUS
		random_angle = random.uniform(20, 50)
		angles = [random_angle, -random_angle]
		for angle in angles:
			new_vector = self.velocity.rotate(angle)
			new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid.velocity = new_vector * 1.2
