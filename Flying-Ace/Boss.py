import pygame
import random 
# Define player by extend the sepecifc class Sprite, 
# and use super to call the constructor of parent

#import some user input so we can use those key easier.
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define a player object that extends Sprite(2D representation)
# Use picture of plane to replace the surface 
class Boss(pygame.sprite.Sprite):
    def __init__(self,y = 0):
        super(Boss, self).__init__()
        # Load the picture from directory and use convert to optimize the surface
        self.image = pygame.image.load("boss.png").convert_alpha()
        # Change the size of image
        self.image = pygame.transform.scale(self.image,(80,80))
         # Use RLEACCEL（slow down the image) to optimize the game
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        # rect is used for get location of image, so we can change it by input
        # get_rect() returns the rectangle of image, and we set the random position to enemy
        self.rect = self.image.get_rect(center = (random.randint(20,480),random.randint(0,0)))
        # Set up the destroy image for enemy
        self.destroy = pygame.image.load("explode2.png").convert_alpha()
        self.destroy = pygame.transform.scale(self.destroy,(80,80))
        # Load the sound effect by using mixer.Sound
        self.explode = pygame.mixer.Sound("explode2.wav")
        self.explode.set_volume(0.3)
        self.speed = 8
    # Update the position of enemy by using screen.blit
    def update(self):
        self.rect.bottom += self.speed
        #The plane will move from top to bottom, and when it hits the bottom
        # it will just be removed by kill()
        if self.rect.top > 700:
            self.kill()
