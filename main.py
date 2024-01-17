import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))

class Dog:
    def __init__(self, name, age, gender, sound, image):
        self.name = name
        self.age = age
        self.gender = gender
        self.sound = sound
        self.image = image

    def bark(self):
        self.sound.play()
        print(f"{self.name} is Barking")


dog1 = Dog("jessi", 6, "girl", pygame.mixer.Sound("w2.mp3"), pygame.image.load("w1.png"))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dog1.bark()
