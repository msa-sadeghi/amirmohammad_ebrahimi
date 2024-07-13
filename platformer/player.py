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
        self.flip = False
        self.vel_y =  0
    def draw(self, screen):
        self.image = self.images[self.image_number]
        self.image = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(self.image, self.rect)
    def animation(self):
        if pygame.time.get_ticks() - self.last_update_time > 100 and self.moving:
            self.last_update_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.images):
                self.image_number = 0
    def update(self, tiles):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.flip = True
            self.moving = True
            dx -= 5
        elif keys[pygame.K_RIGHT]:
            self.flip = False
            self.moving = True
            dx += 5
        else:
            self.moving = False 
        if keys[pygame.K_SPACE]:
            self.vel_y = -15
        dy += self.vel_y
        self.vel_y += 1   
        
        
        for t in tiles:
            if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.size[0], self.rect.size[1]):
                dy = 0
                self.vel_y = 0
        
        
         
        self.rect.x += dx
        self.rect.y += dy
        if self.moving:
            self.animation()
        