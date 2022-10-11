'''
First, we import the sys and pygame modules. The pygame module contains
the functionality needed to make a game. We'll use the sys module to
exit the game when the player quits.
Alien Invasion starts as the function run_game(). The line pygame.init()
at initializes background settings that Pygame needs to work properly.
Then we call pygame.display.set_mode() to create a display window called
screen, on which we'll draw all of the game's graphical elements. The argument
(1200, 800) is a tuple that defines the dimensions of the game window.
By passing these dimensions to pygame.display.set_mode(), we create a game
window 1200 pixels wide by 800 pixels high. (You can adjust these values
depending on the size of your display.)
'''
#=========================================================================================
import sys    # We’ll use the sys module to exit the game when the player quits.
import pygame # Main library we use for gaming-code
from settings import Settings # this file stores code for Settings-class
from ship import Ship # import file with Ship-class
import game_functions as gf # stores all the function we're gone use with events in while-loop 
from pygame.sprite import Group # Group behaves like a list and stores the bullets group
from game_stats import GameStats # import file with GameStatics Class
from button import Button # import file with Button Class
from scoreboard import Scoreboard # import file with class for Scoreboard image
#=========================================================================================
# Alien Invasion starts as the function run_game().
def run_game():   
    # Initializes background settings that Pygame needs to work properly:
    # I.e. pygame, settings, and screen object.
    pygame.init() 
    # Use settings Class to store our settings
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Create a display window called screen, on which we’ll draw all of the game’s graphical elements.
    '''
    The screen object is called a surface. A surface in Pygame is a part
    of the screen where you display a game element. Each element in the
    game, like the aliens or the ship, is a surface. The surface returned by
    display.set_mode() represents the entire game window. When we activate
    the game's animation loop, this surface is automatically redrawn on every
    pass through the loop. 
    '''
    screen = pygame.display.set_mode((1200, 800)) 
    pygame.display.set_caption("Alien Invasion")
    # Render the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    # Create a scoreboard image on screen
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ship. We now need also to pass ai_settings as an argument
    ship = Ship(ai_settings, screen)
    # Make a group to store Bullets in.
    bullets = Group()
    # Make a group to store Aliens in.   
    aliens = Group()
    # Create the fleet of aliens instead of one Alien
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # alien = Alien(ai_settings, screen) # no longer need this
    
    '''
    The game is controlled by a while loop that contains an event loop
    and code that manages screen updates. An event is an action that the user
    performs while playing the game, such as pressing a key or moving the
    mouse. To make our program respond to events, we'll write an event loop to
    listen for an event and perform an appropriate task depending on the kind
    of event that occurred. The for loop at x is an event loop.  
    '''
    # Start the main loop for the game.
    '''
    Note, that we always need to call check_events(), even if the game
    is inactive. For example, we still need to know if the user presses Q to quit
    the game or clicks the button to close the window. We also continue updating
    the screen so we can make changes to the screen while waiting to see
    whether the player chooses to start a new game. The rest of the function
    calls only need to happen when the game is active, because when the game
    is inactive, we don't need to update the positions of game elements.  
    '''
    while True:
        # Respond to keypresses and mouse events passig Ship, Alien
        # Bullets-group objects and etc.
        gf.check_events(ai_settings, screen, stats, sb, 
                        play_button, ship, aliens, bullets)
        # The code below is needed only if the game is active
        if stats.game_active:
            ship.update() # Update Ship images on the screen 
            # Update Bullets and get rid of bullets that have run behind the screen.
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets)
            # Update Aliens' images on the screen 
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        # Update all objects on the screen 
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,bullets, play_button)       
#=========================================================================================
# Run MAIN function that STARTS GAME     
run_game()
#=========================================================================================
