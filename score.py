import pygame
import gameobject


class Score(pygame.sprite.Sprite):
	"""to keep track of the score."""
	def __init__(self, *groups):
		pygame.sprite.Sprite.__init__(self, *groups)
		self.font = pygame.font.Font(None, 20)
		self.font.set_italic(1)
		self.color = "white"
		self.__score = 0
		self.add_score(0)
		self.rect = self.image.get_rect().move(0, 0)


	def add_score(self, points):
		self.__score += points
		msg = f"Score: {self.__score}"
		self.image = self.font.render(msg, 0, self.color)

	def draw(self, screen):
		screen.blit(self.image, self.rect)
