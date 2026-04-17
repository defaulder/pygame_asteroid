import pygame


class GameObject(pygame.sprite.Sprite):
    containers = []
    position: pygame.Vector2
    color: pygame.Color

    def __init__(self, x=0, y=0):
        if self.containers:
            super().__init__(*tuple(self.containers))
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.color = pygame.Color("white")


    def draw(self, screen):
        raise NotImplementedError("Subclass must implement draw()")

    def update(self, dt):
        raise NotImplementedError("Subclass must implement update()")

