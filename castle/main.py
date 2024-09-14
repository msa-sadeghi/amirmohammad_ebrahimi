
# import wmi

# computer = wmi.WMI()
# computer_info = computer.Win32_ComputerSystem()[0]
# os_info = computer.Win32_OperatingSystem()[0]
# proc_info = computer.Win32_Processor()[0]
# gpu_info = computer.Win32_VideoController()[0]

# os_name = os_info.Name.encode('utf-8').split(b'|')[0]
# os_version = ' '.join([os_info.Version, os_info.BuildNumber])
# system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

# print('OS Name: {0}'.format(os_name))
# print('OS Version: {0}'.format(os_version))
# print('CPU: {0}'.format(proc_info.Name))
# print('RAM: {0} GB'.format(system_ram))
# print('Graphics Card: {0}'.format(gpu_info.Name))

# import torch

# if torch.cuda.is_available():
#     print("GPU is available")
# else:
#     print("GPU is not available")
import pygame
from castle import Castle
pygame.init()
screen = pygame.display.set_mode()
screen_width = screen.get_width()
screen_height = screen.get_height()

fps = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 32)
fps_text = font.render(f"fps:{fps}", True, (255, 0,0))
bg_image = pygame.image.load("assets/bg.png")

bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))

my_castle = Castle(1000, 50, screen_width - 350, screen_height - 400)
bullet_group = pygame.sprite.Group()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    # screen.fill((0,0,0))
    my_castle.shoot(bullet_group)
    screen.blit(bg_image, (0,0))
    my_castle.draw(screen)
    fps_text = font.render(f"fps:{clock.get_fps()}", True, (255, 0,0))
    screen.blit(fps_text,(10,10))
    bullet_group.update()
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(fps)
    # print(clock.get_fps())
    
    