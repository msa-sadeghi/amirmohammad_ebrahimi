from pygame.sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.images = []
        for i in range(1,5):
            image = pygame.image.load(f"assets/guy{i}.png")
            image_width = image.get_width()
            image_height = image.get_height()
            image = pygame.transform.scale(image, (image_width * 0.5, image_height * 0.5))
            self.images.append(image)            
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.image_number = 0
        self.last_update_time = pygame.time.get_ticks()
        self.moving = False
    def draw(self, screen):
        self.image = self.images[self.image_number]
        screen.blit(self.image, self.rect)
    def animation(self):
        
        if pygame.time.get_ticks() - self.last_update_time > 100 and self.moving:
            self.last_update_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.images):
                self.image_number = 0
    def update(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.moving = True
            dx += 5
            
        self.rect.x += dx
        self.rect.y += dy
        if self.moving:
            self.animation()
        