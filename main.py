import pygame
pygame.init()
class Dog:
    def __init__(self, name, age, gender, sound, image):
        self.name = name
        self.age = age
        self.gender = gender
        self.sound = sound
        self.image = image

    def bark(self):
        print(f"{self.name} is Barking")


dog1 = Dog("jessi", 6, "girl", pygame.mixer.Sound("w1.wav"), pygame.image.load("w1.png"))

