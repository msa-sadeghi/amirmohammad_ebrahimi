from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2


    def draw(self):
        screen.blit(self.image, self.rect)