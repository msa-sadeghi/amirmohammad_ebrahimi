from pygame.sprite import Sprite
import pygame

class Castle(Sprite):
    def __init__(self, health, ammo, x, y):
        super().__init__()
        self.image_100 = pygame.image.load("assets/castle/castle_100.png")
        w = self.image_100.get_width()
        h = self.image_100.get_height()
        self.image_100 = pygame.transform.scale(self.image_100, (w * 0.2, h * 0.2))
        self.image_50 = pygame.image.load("assets/castle/castle_50.png")
        w = self.image_50.get_width()
        h = self.image_50.get_height()
        self.image_50 = pygame.transform.scale(self.image_50, (w * 0.2, h * 0.2))
        self.image_25 = pygame.image.load("assets/castle/castle_25.png")
        w = self.image_25.get_width()
        h = self.image_25.get_height()
        self.image_25 = pygame.transform.scale(self.image_25, (w * 0.2, h * 0.2))
        self.images = [
            self.image_100,
            self.image_50, 
            self.image_25
        ]
        self.health = health
        self.ammo = ammo
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = (x,y))
    def draw(self, screen):
        screen.blit(self.image, self.rect)