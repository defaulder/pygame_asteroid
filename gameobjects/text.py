import pygame


class Text(pygame.sprite.Sprite):
    """To render text on screen"""

    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.color = "white"
        self.font = pygame.font.Font(None, 20)
        self.__text = ""
        self.image = self.font.render(self.__text, 0, self.color)
        self.rect = self.image.get_rect()

    @property
    def text(self):
        """The  property."""
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
        self.image = self.font.render(self.__text, 0, self.color)


    def draw(self, screen):
        screen.blit(self.image, self.rect)
