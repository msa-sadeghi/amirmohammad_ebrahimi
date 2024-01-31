from constants import *
from pygame.sprite import Sprite
import random
class Monster(Sprite):
    def __init__(self, image, x,y, type):
        self.image = image
        self.rect = self.image.get_rect(topleft = (x,y))
        self.type = type
        self.dx = random.choice((-1,1))
        self.dy = random.choice((-1,1))