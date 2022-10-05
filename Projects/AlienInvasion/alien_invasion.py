'''
First, we import the sys and pygame modules. The pygame module contains
the functionality needed to make a game. We’ll use the sys module to
exit the game when the player quits.
Alien Invasion starts as the function run_game(). The line pygame.init()
at u initializes background settings that Pygame needs to work properly.
At v, we call pygame.display.set_mode() to create a display window called
screen, on which we’ll draw all of the game’s graphical elements. The argument
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
    # Make a ship.
    ship = Ship(screen)
    
    '''
    The game is controlled by a while loop that contains an event loop
    and code that manages screen updates. An event is an action that the user
    performs while playing the game, such as pressing a key or moving the
    mouse. To make our program respond to events, we'll write an event loop to
    listen for an event and perform an appropriate task depending on the kind
    of event that occurred. The for loop at x is an event loop.  
    '''
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events. For example, when the player clicks
        # the game window’s close button, a pygame.QUIT event is detected and we call 
        # sys.exit() to exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # fill the screen with the background color dfined as RGB() which takes only one argument: a color.
            screen.fill(ai_settings.bg_color)
            ship.blitme() # Render ship in the screen
            pygame.display.flip() # Make the most recently drawn screen visible.
#=========================================================================================

# Run function that STARTS GAME    
run_game()