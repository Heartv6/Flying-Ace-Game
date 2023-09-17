# Import the pygame and some key user input so we can directly use it 
import pygame 
from Player import Plane
from Enemy import Enemy
from Bullet import Bullet
from Boss import Boss

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize the pygame environment 
pygame.init()
pygame.mixer.init()


#Set up the screen and oringinal axis
width = 500
height = 750
x = (width - 60)/2
y = 600
val = 0.5

#Set up the font and size for score by using bulit-in function
# Load the font from local directory 
score_font = pygame.font.Font("bold.ttf",30)
score_color = (255,255,255)

# Setup the game start screen
start_screen  = pygame.display.set_mode([width,height])
#Load the background of gamestart 
background1 = pygame.image.load("gamestart.png")
# Set up the end game page
end_screen  = pygame.display.set_mode([width,height])
background2 = pygame.image.load("overover.jpg")
# Load the sound effect for gameover
gameover = pygame.mixer.Sound("gameover.wav")
gameover.set_volume(0.5)

# Design a function for end page if a plane dead over 3 times    
def end_page(score):
    gameover.play(0)
    last_run = True
    while last_run:
        end_screen.blit(background2, (0,0))
        # Load the icon to the ending page
        icon1 = pygame.image.load("gameover.png")
        icon1 = pygame.transform.scale(icon1, (250,100))
        icon2 = pygame.image.load("tryagain.png")
        icon2 = pygame.transform.scale(icon2, (200,80))
        icon3 = pygame.image.load("exit.png")
        icon3 = pygame.transform.scale(icon3, (200,80))
        end_screen.blit(icon1, (125,200))
        end_screen.blit(icon2, (150,400))
        end_screen.blit(icon3, (150,550))
         #Setup the font and color of the score
        score_font = pygame.font.Font("bold.ttf",40)
        score_color = (255,255,255)
        score_surface = score_font.render("Your Final Score: %s" % str(score), True, score_color)
        end_screen.blit(score_surface, (70,100))
        pygame.display.update()  
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            # Check whether mouse is pressed 
            buttons = pygame.mouse.get_pressed()
            # Get the position of mouse pressed
            x,y = pygame.mouse.get_pos()
            # Check if the button pressed is on the position of start icon and exit icon
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0]:
                    if x >= 150 and x <= 350 and y <= 480 and y >= 400:
                        # If it is on the restart icon, call the main function to restart the game
                        main1(False,0)
                    # if not juse quit the game 
                    elif x >= 150 and x <= 350 and y <=630 and y >= 550:
                        pygame.quit()
            # The game will also be quit if user enter esc or press close button
            elif event.type == QUIT:
                last_run = False
                pygame.quit()
            elif key[K_ESCAPE]:
                last_run = False 
                pygame.quit()
    pygame.quit()
    
def start_page():
     # Starting page before game can start 
    first_run = True
    while first_run:
        start_screen.blit(background1, (0,0))
        # Load the icon to the starting page
        icon1 = pygame.image.load("start.png")
        icon1 = pygame.transform.scale(icon1, (200,80))
        start_screen.blit(icon1, (150,400))
        icon2 = pygame.image.load("exit.png")
        icon2 = pygame.transform.scale(icon2, (200,80))
        start_screen.blit(icon2, (150,550))
        icon3 = pygame.image.load("flyingace.png").convert_alpha()
        icon3 = pygame.transform.scale(icon3, (310,300))
        start_screen.blit(icon3, (100,0))
        #Setup the font and color of the name
        name_font = pygame.font.Font("bold.ttf",50)
        name_color = (255,99,71)
        name_surface = name_font.render("FLYING ACE" , True, name_color)
        start_screen.blit(name_surface, (135,300))
        
        pygame.display.update()
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            # Check whether mouse is pressed 
            buttons = pygame.mouse.get_pressed()
            # Get the position of mouse pressed
            x,y = pygame.mouse.get_pos()
            # Check if the button pressed is on the position of start icon and exit icon
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0]:
                    if x >= 150 and x <= 350 and y <= 480 and y >= 400:
                        # If it is on the start icon, break the loop, and start main game loop
                        first_run = False
                    # Else the program will quit if the user hit the button of exit
                    # x and y represent the position that mouse is clicking
                    elif x >= 150 and x <= 350 and y <=630 and y >= 550:
                        pygame.quit()
            elif event.type == QUIT:
                pygame.quit()
            elif key[K_ESCAPE]:
                pygame.quit()
    
def main1(hard_level,score):
    # Set up the screen and set up the name for this game
    screen = pygame.display.set_mode([width,height])
    pygame.display.set_caption("Flying Ace ")

    # Set up the game icon by load the image and use set_icon
    icon = pygame.image.load("plane.png")
    pygame.display.set_icon(icon)

    # Set up the backgroun image 
    background = pygame.image.load("back2.jpg")

    # Load a background sound clip and begin playing it.
    # The sound never end by setting the named parameter loops=-1.
    pygame.mixer.music.load("bkgmusic.wav")
    pygame.mixer.music.play(-1)

    # Load the sound effect for explosion by using mixer.Sound
    explode = pygame.mixer.Sound("explode.wav")
    explode.set_volume(0.5)

    # Load the sound effect for shooting
    shoot = pygame.mixer.Sound("shoot.wav")
    shoot.set_volume(0.5)
    
    # Load the picture of pause 
    pause_icon = pygame.image.load("pause.png")
    pause_icon = pygame.transform.scale(pause_icon,(40,40))

    # Creating the object from Player and other 3 plane for counting lives
    p = Plane()
    # Set up the scale and original position, therse sprites won't be updated
    # Just for showing how many lives do you have by image
    p1 = Plane()
    p1.image = pygame.transform.scale(p1.image,(40,40))
    p1.rect = p1.image.get_rect(left = 460, bottom = 750)
    p2 = Plane()
    p2.image = pygame.transform.scale(p2.image,(40,40))
    p2.rect = p2.image.get_rect(left = 420, bottom = 750)
    p3 = Plane()
    p3.image = pygame.transform.scale(p3.image,(40,40))
    p3.rect = p3.image.get_rect(left = 380, bottom = 750)
    p_list = [p1, p2, p3]
    # The player will have 3 lives to play the game
    lives = 3 

    # Create enemy and boss by using sprite group that hold all the enemy sprites
    # enemies group can be later used for collision detection and update the position
    # all_sprites is used for displaying all the sprites
    enemies = pygame.sprite.Group()
    sprites = pygame.sprite.Group()
    sprites.add(p)

    # Define an event that is called add_enemy
    add_enemy = pygame.USEREVENT
    # The add_enemy event will be occured every 0.4 second
    pygame.time.set_timer(add_enemy, 400)

    # Define another event that is called add_boss
    add_boss = pygame.USEREVENT + 2
    # The add_enemy event will be occured every 0.8 second
    pygame.time.set_timer(add_boss, 800)
    
    if hard_level:
        pygame.time.set_timer(add_enemy, 350)
        pygame.time.set_timer(add_boss, 700)

    # Setup the clock for hadnling the framerate by using time.Clock()
    clock = pygame.time.Clock()

    # Create a sprite group that store the bullet objects
    my_bullet = pygame.sprite.Group()
    enemy_bullet = pygame.sprite.Group()
    
    # Define a event that will add bullet to enemy every 1 second
    # if it is the hard mode 
    add_bullet = pygame.USEREVENT + 3 
    pygame.time.set_timer(add_bullet, 1000)

   
                

    # The main event loop
    run = True
    pause = False 
    flag = False 
    while run:
        # When user click the window close buttob, the run will become false
        # the program loop will end
        # Also, when a key escape is pressed, the program will also quit
        for event in pygame.event.get():
            key =  pygame.key.get_pressed()
            #Check the button
            buttons = pygame.mouse.get_pressed()
            # Get the position of mouse pressed
            x,y = pygame.mouse.get_pos()
            if key[K_ESCAPE]:
                run = False 
            elif event.type == QUIT:
                run = False
            # Every 0.5 second, the add_enemy event will occur, and add one enemy
            elif event.type == add_enemy:
                e = Enemy()
                enemies.add(e)
                sprites.add(e)
            # Every 0.5 second, the add_enemy event will occur, and add one boss to the sprite group
            elif event.type == add_boss:
                boss = Boss()
                sprites.add(boss)
                enemies.add(boss)
            # Using key_space to shoot the bullet
            elif key[pygame.K_SPACE]:
                # The position of bullet will be originally placed at top of the plane
                # Create a new bullet 
                b = Bullet(p.rect.centerx,p.rect.top, True)
                # Add one bullet to the sprite group
                my_bullet.add(b)
                sprites.add(b)
                # Play sound effect
                shoot.play(0)
              # if the user press the top right button or press the keyboard 1
            # The pause will become True and the pause loop will start 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0]:
                    if x >= 460 and x <= 500 and y <= 40 and y >= 0:
                        pause = True
            elif key[pygame.K_1]:
                pause = True 
            elif hard_level:
                if event.type == add_bullet:
                    # For all the enemy, they can attack at the hard_level
                    # Every 2 second the enemy will fire a bullet
                    for i in enemies:
                        i.speed += 1
                        b = Bullet(i.rect.centerx, i.rect.bottom, False)
                        b.speed = i.speed + 3  
                        b.image = pygame.image.load("enemy_bullet.png").convert_alpha()
                        b.image = pygame.transform.scale(b.image,(30,50))
                        enemy_bullet.add(b)
                        sprites.add(b)
           
        # If the user choose pause the game, this loop will run instead of main loop              
        while pause:
            # Load the pause screen 
            screen.blit(background2, (0,0))
            # Load three icon to the pause screen, and one is resume button,
            # Another one is exit button
            icon1 = pygame.image.load("resume.png")
            icon1 = pygame.transform.scale(icon1, (200,80))
            icon2 = pygame.image.load("exit.png")
            icon2 = pygame.transform.scale(icon2, (200,80))
            icon3 = pygame.image.load("break.png")
            icon3 = pygame.transform.scale(icon3, (300,300))
            screen.blit(icon3, (100,50))
            screen.blit(icon2, (150,550))
            screen.blit(icon1, (150,400))
            pygame.display.update()
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                # Check whether mouse is pressed 
                buttons = pygame.mouse.get_pressed()
                # Get the position of mouse pressed
                x,y = pygame.mouse.get_pos()
                # Check if the button pressed is on the position of resume icon and exit icon
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttons[0]:
                        if x >= 150 and x <= 350 and y <= 480 and y >= 400:
                            # If it is on the resume icon, break the loop, and back to main game loop
                            pause = False
                        # Else the program will quit if the user hit the button of exit
                        # x and y represent the position that mouse is clicking
                        elif x >= 150 and x <= 350 and y <=630 and y >= 550:
                            pygame.quit()
                elif event.type == QUIT:
                    pygame.quit()
                elif key[K_ESCAPE]:
                    pygame.quit()
        while flag:
            background3 = pygame.image.load("hard_level.png")
            background3 = pygame.transform.scale(background3,(width,height))
            screen.blit(background3, (0,0))
            iconx = pygame.image.load("congra.png")
            iconx = pygame.transform.scale(iconx, (400,300))
            icony = pygame.image.load("doyou.png")
            icony = pygame.transform.scale(icony, (400,300))
            continue_icon = pygame.image.load("continue.png")
            continue_icon = pygame.transform.scale(continue_icon, (200,80))
            exit_icon = pygame.image.load("exit.png")
            exit_icon = pygame.transform.scale(exit_icon, (200,80))
            screen.blit(iconx, (50,0))
            screen.blit(icony, (50,100))
            screen.blit(continue_icon,(150,400))
            screen.blit(exit_icon, (150,550))
            pygame.display.update()
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                # Check whether mouse is pressed 
                buttons = pygame.mouse.get_pressed()
                # Get the position of mouse pressed
                x,y = pygame.mouse.get_pos()
                # Check if the button pressed is on the position of resume icon and exit icon
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttons[0]:
                        if x >= 150 and x <= 350 and y <= 480 and y >= 400:
                            # If it is on the continue icon, break the loop, and continue main game loop
                            main1(hard_level,5000)
                            flag = False    
                        # Else the program will quit if the user hit the button of exit
                        # x and y represent the position that mouse is clicking
                        elif x >= 150 and x <= 350 and y <=630 and y >= 550:
                            pygame.quit()
                elif event.type == QUIT:
                    pygame.quit()
                elif key[K_ESCAPE]:
                    pygame.quit()

        # Detect the keys that are pressed
        keys = pygame.key.get_pressed()
        # Put player at the specific postion we want and
        # Update the postion according to the user input 
        p.update(keys)
        
        # Update all the enemy positon in that sprite group
        enemies.update() 
        
        #Update all the bullet position in the sprite group
        my_bullet.update()
        
        #Update all the bullet position of enemy 
        enemy_bullet.update()
        
        # Fit the background
        screen.blit(background,(0,0))
        
        # Draw all the sprites in that sprite group on the screen
        for i in sprites:
            screen.blit(i.image, i.rect)
            
        # Draw the lives you currently have on the screen
        for players in p_list:
            screen.blit(players.image, players.rect)
            
        # Draw the pause button on the righttop of the screen
        screen.blit(pause_icon,(460,0))
        
        # Check if enemy colide with player by using bulit in function
        # .spritecollideany()accepts a Sprite and a Group as parameters
        # and it will automatically check if the rectangle of player
        # intersects with any rectangle in enemies group
        if pygame.sprite.spritecollideany(p,enemies):
            # if that is the case, the player sprite will be killed , the game is over
            # Check if player still have lives, if not end the game and kill the sprite           
            if lives == 0:
                # Draw the explosion image at the position of plane
                screen.blit(p.destroy, p.rect)
                # Play the sound of explosion
                explode.play(0)
                p.kill()
                #Display the gameover page
                end_page(score) 
            # if the player still have lives, reset the plane 
            else:
                screen.blit(p.destroy, p.rect)
                # minus one lives 
                lives -= 1
                # Reset the position of plane
                p.reset()
                explode.play(0)
                # remove one plane that represent you have one plane less
                p_list.pop()
                
        
        # Set up a variable called dict_colide that will
        # check if there is any colision between two group my_bullet and enemies
        # The bulit-in function groupcolide will return a dictionary with elements colide in both group
        dict_colide = pygame.sprite.groupcollide(enemies,my_bullet,False,False)
        # Loop through the diectionary and kill all the sprites in that dictionary
        for key,value in dict_colide.items():
            for elements in value:
                # kill the bullet sprite
                elements.kill()
                sprites.remove(elements)
                # Draw the destroy picture at the postion of enemy
                screen.blit(key.destroy, key.rect)
                # Sound effect when an enemy is destroyed 
                key.explode.play(0)
                # kill the ememy sprite
                key.kill()
                sprites.remove(key)
            # Add score if a player kill the enemies successfully 
            score += 100
            
        # Check if the plane is hit by enemy's bullet 
        if pygame.sprite.spritecollideany(p,enemy_bullet):
            # if that is the case, the player sprite will be killed , the game is over
            # Check if player still have lives, if not end the game and kill the sprite           
            if lives == 0:
                # Draw the explosion image at the position of plane
                screen.blit(p.destroy, p.rect)
                # Play the sound of explosion
                explode.play(0)
                p.kill()
                #Display the gameover page
                end_page(score) 
            # if the player still have lives, reset the plane 
            else:
                screen.blit(p.destroy, p.rect)
                # minus one lives 
                lives -= 1
                # Reset the position of plane
                p.reset()
                explode.play(0)
                # remove one plane that represent you have one plane less
                p_list.pop()
        
        # Setup the score surface by using render function
        # render takes three arguments which is text, whether antalias and the color of score
        score_surface = score_font.render("Score: %s" % str(score), True, score_color)
        # Draw the score surface on the screen 
        screen.blit(score_surface,(10, 5))
        
         # Check if the user reach score of 3000
        if score == 3000:
            hard_level = True
            flag = True
            # Narrow the gap between enemy appearances
            pygame.time.set_timer(add_enemy, 300)
            pygame.time.set_timer(add_boss, 600)
        

              
                
        
        pygame.display.update()


        # Change the game speed by using tick function
        # tick calculate the number of milliseconds each frame should take.
        # Lock 60 Frame per second 
        clock.tick(60)
       
        


    pygame.quit()

        
if __name__ == '__main__':
    start_page()
    main1(False,0)
 
