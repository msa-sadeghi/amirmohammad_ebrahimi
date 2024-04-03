from pygame.sprite import Sprite
import pygame
from constants import WINDOW_HEIGHT


class EnemyBullet(Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("space/assets/red_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10

        bullet_group.add(self)

    def update(self):
        self.rect.y += self.velocity
        if self.rect.top >= WINDOW_HEIGHT:
            self.kill()
