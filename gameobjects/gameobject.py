import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.color = pygame.Color("white")

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        #  sub-classes must override
        pass
