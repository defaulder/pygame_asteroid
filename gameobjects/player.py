import pygame
from .circleshape import CircleShape
from .shot import Shot
from constants import (
    PLAYER_RADIUS,
    PLAYER_LIVES,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
)


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.direction = pygame.Vector2(0, 1)
        self.__timer = 0
        self.lives = PLAYER_LIVES
        self.invincible = False

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_d]:
            self.rotate(PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_w]:
            self.move(PLAYER_SPEED * dt)
        if keys[pygame.K_s]:
            self.move(-PLAYER_SPEED * dt)
        if keys[pygame.K_SPACE] and self.__timer <= 0:
            self.shoot()
            self.__timer = PLAYER_SHOOT_COOLDOWN
        self.__timer -= dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        right = self.direction.rotate(90) * self.radius * 0.65
        up_radius_vector = self.direction * self.radius
        return (
            self.position + up_radius_vector,
            self.position - up_radius_vector + right,
            self.position - up_radius_vector - right
        )


    def rotate(self, degrees):
        self.direction = self.direction.rotate(degrees)

    def move(self, distance):
        self.position += self.direction * distance

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = self.direction * PLAYER_SHOOT_SPEED

    def try_respawn(self):
        if self.lives <= 0:
            return False
        self.lives -= 1
        self.invincible = False
        return True
