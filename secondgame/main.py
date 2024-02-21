from constants import *
from player import Player

from enemy import Monster
from random import randint, choice
enemy_group = pygame.sprite.Group()
level = 0

FPS = 60
clock = pygame.time.Clock()

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
    

start_level()

target_monster_type = randint(0,3)
target_monster_image = all_monster_images[target_monster_type]
target_monster_rect = target_monster_image.get_rect(centerx = SCREEN_WIDTH/2, bottom=100)

def select_target():
    global target_monster_image, target_monster_type, target_monster_rect
    target_monster_type = choice(enemy_group.sprites()).type
    target_monster_image = all_monster_images[target_monster_type]
    target_monster_rect = target_monster_image.get_rect(centerx = SCREEN_WIDTH/2, bottom=100)
    
select_target()

def check_collisions():
    collided_monster = pygame.sprite.spritecollideany(my_player, enemy_group)
    if collided_monster:
        print("collided_monster.type", collided_monster.type)
        print("target_monster_type", target_monster_type)
        if collided_monster.type == target_monster_type:
            collided_monster.remove(enemy_group)
            
            # TODO  اضافه کردن امتیاز
            # TODO  پلی کردن صدا
            if len(enemy_group) > 0:
                select_target()
            else:
                pass
                # TODO رفتن به مرحله بعد


my_player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    check_collisions()
    screen.fill((0,0,0))
    screen.blit(target_monster_image, target_monster_rect)          
    my_player.draw()
    my_player.move()
    enemy_group.draw(screen)
    enemy_group.update()
    pygame.display.update()
    clock.tick(FPS)