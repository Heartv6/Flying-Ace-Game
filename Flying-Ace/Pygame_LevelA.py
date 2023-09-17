#import the pygame and initialize the game library to use all the modules
import pygame

#import some user input so we can directly use it without pygame.
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

#Set up the screen and oringinal axis
width = 900
height = 700
x = (width - 60)/2
y = 600
val = 0.5

# Create the screen by using the width and height we previous defined
screen = pygame.display.set_mode([width,height])

# The main event loop
run = True
while run:
    # When user click the window close buttob, the run will become false
    # the program loop will end
    # Also, when a key escape is pressed, the program will also quit
    for event in pygame.event.get():
        key =  pygame.key.get_pressed()
        if key[K_ESCAPE]:
                run = False
        elif event.type == QUIT:
            run = False
    
    # Handling the user inpput whenever a user press left,right,up or down button
    # Item will move according to the button pressed in the loop
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        x -= val
    if keys[K_RIGHT]:
        x += val
    if keys[K_UP]:
        y -= val
    if keys[K_DOWN]:
        y += val
    
    # Fill screen with alice blue color 
    screen.fill((240,248,255))
    
    # Creare an item with size(70*70) by using surface 
    item = pygame.Surface((60,60))
    # Fill the item with red color
    item.fill((255,0,0))
    
    # Draw some rectangle as a boundary of scrren with blue color
    pygame.draw.rect(screen, (30,144,255),(0,0,900,25))
    pygame.draw.rect(screen, (30,144,255),(0,0,25,700))
    pygame.draw.rect(screen, (30,144,255),(0,675,900,25))
    pygame.draw.rect(screen, (30,144,255),(875,0,25,700))
    # Draw some circle on the screen
    pygame.draw.circle(screen, (138,43,226), (200, 100), 50)
    pygame.draw.circle(screen, (255,211,155), (700, 100), 50)
    pygame.draw.circle(screen, (152,245,255), (250, 250), 50)
    pygame.draw.circle(screen, (118,238,0), (500, 250), 50)
    
    # Draw the item on screen at the location of (x,y)
    screen.blit(item, (x,y))
    
    #Update the scrren
    pygame.display.flip()

#Quit the pygame whe the loop is finished 
pygame.quit()