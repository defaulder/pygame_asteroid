import asyncio
import pygame

from gameobjects import Player, Asteroid, AsteroidField, Score, Shot, Text
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

FPS = 60

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

async def main():
    run = True
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = [updatable, drawable]
    AsteroidField.containers = [updatable]
    Asteroid.containers = [updatable, drawable, asteroids]
    Shot.containers = [updatable, drawable, shots]

    field = AsteroidField()
    score = Score(drawable)
    score.rect = score.rect.move(0, 0)
    text = Text(drawable)
    text.rect = score.rect.move(0, score.rect.height)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    text.text = f"Lives: {0}"

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        for asteroid in asteroids:
            if asteroid.check_collision_with(player):
                if player.try_respawn():
                    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                else:
                    player.kill()
            for shot in shots:
                if asteroid.check_collision_with(shot):
                    asteroid.split()
                    shot.kill()
                    score.points += 100

        dt = clock.tick(FPS) / 1000
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
