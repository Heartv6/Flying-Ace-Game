import pygame

class Bullet(pygame.sprite.Sprite):
    # Define player by extend the sepecifc class Sprite, 
    # and use super to call the constructor of parent
    def __init__(self,position_x,position_y,direction):
        pygame.sprite.Sprite.__init__(self)
        
        #Load the picture from directory and use convert to optimize the surface
        self.image = pygame.image.load("bullet.png").convert_alpha()
        # Change the size of the image 
        self.image = pygame.transform.scale(self.image,(20,35))
         # Use RLEACCEL（slow down the image) to optimize the game
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        # Get the rectangle of this image 
        self.rect = self.image.get_rect()
        # Setup the speed
        self.speed = 5
        # Setup the primary position of bullet
        self.rect.centerx = position_x
        self.rect.centery = position_y
        #Setup the direction of the bullet
        self.direction = direction
   
    
    # Update the bullet position according to the direction
    def update(self):
        # When self.direction is true, the bulluet is moving upward
        if self.direction:
            self.rect.top -= self.speed
            # If the bullet hit the top of the screen, it will be removed
            if self.rect.top < 0:
                self.kill()
        else:
            self.rect.top += self.speed
            if self.rect.top > 700:
                self.kill()

        
        