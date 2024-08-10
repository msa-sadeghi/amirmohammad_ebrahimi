import pygame
from world import World
from player import Player
from level_creator import world_data

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
enemy_group = pygame.sprite.Group()
world = World(world_data, enemy_group)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
f = pygame.font.SysFont("arial", 28)
welcome_text = f.render("welcome", True, (255,0,0))
start_time = 0

player = Player(100, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    world.draw(screen)
    if pygame.time.get_ticks() - start_time < 2000:
        screen.blit(welcome_text, (200,200))
        
    player.update(world.tiles)
    player.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)