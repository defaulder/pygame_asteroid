import gameobject
import pygame


#Base class for game objects
class CircleShape(gameobject.GameObject):
	def __init__(self, x, y, radius):
		super().__init__(x, y)
		self.radius = radius
		self.velocity = pygame.Vector2(0, 0)


	def update(self, dt):
		pass


	def draw(self, screen):
		pygame.draw.circle(screen, self.color, self.position, self.radius, 2)


	def check_collision_with(self, circleshape):
		distance = pygame.math.Vector2.distance_to(self.position, circleshape.position)
		return distance <= (self.radius + circleshape.radius)
