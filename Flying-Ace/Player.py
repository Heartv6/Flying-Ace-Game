import pygame 
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
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super(Plane, self).__init__()
        # Load the picture from directory and use convert to optimize the surface
        self.image = pygame.image.load("plane.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(80,80))
        # Use RLEACCEL（slow down the image) to optimize the game
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        # rect is used for get location of image, so we can change it by input
        # get_rect() returns the rectangle of image, and we set the original position
        self.rect = self.image.get_rect(left = 200, bottom = 750)
        # Set up the destroy image for plane
        self.destroy = pygame.image.load("explode1.png").convert_alpha()
        self.destroy = pygame.transform.scale(self.destroy,(100,100))
        # Load the sound effect by using mixer.Sound
        self.explode = pygame.mixer.Sound("explode.wav")
        self.explode.set_volume(0.4)
    # Update the position of sprite by detecting the user input
    # move_ip stands for move in place, with x and y axis as parameter
    def update(self, pressed_key):
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_key[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_key[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_key[K_RIGHT]:
            self.rect.move_ip(10, 0)
            
        # Keep our plane in the screen
        # If it hit left corner, we keep the value of
        # the X-coordinate of the left side of the rectangle be 0
        if self.rect.left < 0:
            self.rect.left = 0
        # If it hit right corner, we keep the value of
        # the X-coordinate of the right side of the rectangle be width
        if self.rect.right > 500:
            self.rect.right = 500
        # If it hit top corner, we keep the value of
        # the Y-coordinate of the top side of the rectangle be 0
        if self.rect.top <= 0:
            self.rect.top = 0
        # If it hit bottom corner, we keep the value of
        # the Y-coordinate of the bottom side of the rectangle be height
        if self.rect.bottom >= 750:
            self.rect.bottom = 750
   
    # Reset the position of the plane 
    def reset(self):
        self.rect = self.image.get_rect(left = 200, bottom = 750)

            
       