import pygame
from enemy import Enemy
class World:
    def __init__(self, world_data, enemy_group):
        self.tiles = []
        self.image = pygame.image.load("assets/sky.png")
        for i in range(len(world_data)):
            for j in range(len(world_data[i])):
                if world_data[i][j] == 1:
                    img = pygame.image.load("assets/dirt.png")
                    img = pygame.transform.scale(img, (50, 50))
                    rect = img.get_rect(topleft = (j * 50,i * 50))
                    self.tiles.append((img, rect))
                if world_data[i][j] == 2:
                    img = pygame.image.load("assets/grass.png")
                    img = pygame.transform.scale(img, (50, 50))
                    rect = img.get_rect(topleft = (j * 50,i * 50))
                    self.tiles.append((img, rect))
                if world_data[i][j] == 3:
                    Enemy(j * 50,i * 50 + 15, enemy_group)
                    
        
    def draw(self, screen):
        screen.blit(self.image, (0,0))
        for tile in self.tiles:
            screen.blit(tile[0], tile[1])
        