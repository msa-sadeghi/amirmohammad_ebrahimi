import pygame
class World:
    def __init__(self):
        self.image = pygame.image.load("assets/sky.png")
        
    def draw(self, screen):
        screen.blit(self.image, (0,0))
        