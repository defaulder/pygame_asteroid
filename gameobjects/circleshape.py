import pygame
from .gameobject import GameObject


#Base class for game objects
class CircleShape(GameObject):
    radius: int | float
    velocity: pygame.Vector2


    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)


    def update(self, dt):
        self.position += self.velocity * dt


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)


    def check_collision_with(self, circleshape):
        distance = self.position.distance_to(circleshape.position)
        return distance <= (self.radius + circleshape.radius)
