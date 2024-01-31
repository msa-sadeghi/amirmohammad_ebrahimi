from constants import *
from player import Player

from enemy import Monster
from random import randint
enemy_group = pygame.sprite.Group()
level = 0

blue_monster = pygame.image.load("assets/blue_monster.png")
green_monster = pygame.image.load("assets/green_monster.png")
yellow_monster = pygame.image.load("assets/yellow_monster.png")
purple_monster = pygame.image.load("assets/purple_monster.png")
all_monster_images = [blue_monster, green_monster, yellow_monster, purple_monster]


def start_level():
    global level
    level += 1
    for i in range(level):
        enemy_group.add(Monster(all_monster_images[0], randint(0,SCREEN_WIDTH), randint(100,SCREEN_HEIGHT-100), 0))
        enemy_group.add(Monster(all_monster_images[1], randint(0,SCREEN_WIDTH), randint(100,SCREEN_HEIGHT-100), 1))
        enemy_group.add(Monster(all_monster_images[2], randint(0,SCREEN_WIDTH), randint(100,SCREEN_HEIGHT-100), 2))
        enemy_group.add(Monster(all_monster_images[3], randint(0,SCREEN_WIDTH), randint(100,SCREEN_HEIGHT-100), 3))
    



my_player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    my_player.draw()
    pygame.display.update()