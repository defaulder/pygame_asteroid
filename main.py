# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	AsteroidField.containers = (updatable)
	Asteroid.containers = (updatable, drawable, asteroids)
	Shot.containers = (updatable, drawable, shots)

	field = AsteroidField()
	player = Player(
		x = SCREEN_WIDTH / 2,
		y = SCREEN_HEIGHT /2
	)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return


		screen.fill("black")
		updatable.update(dt)

		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		for asteroid in asteroids:
			if asteroid.check_collision_with(player):
				print("Game over!")
				sys.exit()
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
