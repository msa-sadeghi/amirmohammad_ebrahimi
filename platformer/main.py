import pygame
from world import World
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
world = World()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
f = pygame.font.SysFont("arial", 28)
welcome_text = f.render("welcome", True, (255,0,0))
start_time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    world.draw(screen)
    if pygame.time.get_ticks() - start_time < 2000:
        screen.blit(welcome_text, (200,200))
        
    
    pygame.display.update()
    clock.tick(FPS)