'''
We are moving the code that manages events to a separate function called check_events().
This will simplify run_game() and isolate the event management loop. 
Isolating the event loop allows you to manage events separately
from other aspects of the game, like updating the screen
'''
import sys
import pygame
#===========================================================================================
def check_events(ship): 
    # Respond to keypresses and mouse events. Watch for keyboard and mouse events. 
    # Each event is picked up by the pygame.event.get() method
    # Each keypress is registered as a KEYDOWN event. Clos button-click is QUIT-event
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: # if player clicks the game window’s close button, QUIT-event arises
            sys.exit()
        elif event.type == pygame.KEYDOWN:   # KEYDOWN-event raises when user presses any button
            if event.key == pygame.K_RIGHT:  # user presses button = [right arrow key] (K_RIGHT)
                ship.moving_right = True     # Respond to KEYDOWN events if user presses the right arrow key
            elif event.key == pygame.K_LEFT: # user presses button = [left arrow key] (K_LEFT)
                ship.moving_left = True      # Respond to KEYDOWN events if user presses the right arrow key
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False    # Respond to KEYUP events if user releases the right arrow key
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False     # Respond to KEYUP events if user releases the left arrow key
        '''
        If a KEYDOWN event occurs for the K_LEFT key, we set moving_left to True. If
        a KEYUP event occurs for the K_LEFT key, we set moving_left to False. We can
        use elif blocks here because each event is connected to only one key. If the
        player presses both keys at once, two separate events will be detected.      
        '''        
#===========================================================================================                
def update_screen(ai_settings, screen, ship):# Update images on the screen and flip to the new screen. 
    # Fill the screen with the background color dfined as RGB() which takes only one argument: a color.
    screen.fill(ai_settings.bg_color) # Redraw the screen during each pass through the loop.
    ship.blitme()                     # Render ship in the screen
    pygame.display.flip()             # Make the most recently drawn screen visible.
#===========================================================================================