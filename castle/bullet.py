from pygame.sprite import Sprite
import pygame
import math
class Bullet(Sprite):
    def __init__(self, x,y, group, angle):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        w = self.image.get_width()
        h = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (w * 0.3, h * 0.3))
        self.rect = self.image.get_rect(center = (x,y))
        group.add(self)
        self.angle = angle
        
    def update(self):
        dx = math.cos(self.angle) * 4
        dy = -1 * math.sin(self.angle) * 4
        self.rect.x += dx
        self.rect.y += dy
        