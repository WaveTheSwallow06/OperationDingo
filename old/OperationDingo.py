import pygame
from pygame.locals import *
pygame.init()
print("Operation Dingo!")
while pygame.mixer.music.get_busy():
pygame.time.wait(1000)
pygame.mixer.music.load("mm2wood.mid")
pygame.mixer.music.play()
