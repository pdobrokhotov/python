'''
We are moving here the code that manages events to a separate function called check_events().
This will simplify run_game() and isolate the event management loop. 
Isolating the event loop allows you to manage events separately
from other aspects of the game, like updating the screen
'''
import sys
import pygame
from bullet import Bullet
#=======================================================================================
# Respond to Key-PRESS event.
def check_keydown_events(event, ai_settings, screen, ship, bullets): 
    if event.key == pygame.K_RIGHT:    # user presses button = [right arrow key] (K_RIGHT)
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:   # user presses button = [left arrow key] (K_LEFT)
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # Create a new bullet and add it to the bullets group.
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
#=======================================================================================
# Fire a bullet if limit not reached yet. 
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)    
#=======================================================================================
# Respond to Key-RELEASE event.
def check_keyup_events(event, ship):  
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
#=======================================================================================
def check_events(ai_settings, screen, ship, bullets):
    # Respond to keypresses and mouse events. Watch for keyboard and mouse events. 
    # Each event is picked up by the pygame.event.get() method
    # Each keypress is registered as a KEYDOWN event. Clos button-click is QUIT-event
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: # if player clicks the game window’s close button, QUIT-event arises
            sys.exit()
        elif event.type == pygame.KEYDOWN:   # KEYDOWN-event raises when user presses any button
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        '''
        If a KEYDOWN event occurs for the K_LEFT key, we set moving_left to True. If
        a KEYUP event occurs for the K_LEFT key, we set moving_left to False. We can
        use elif blocks here because each event is connected to only one key. If the
        player presses both keys at once, two separate events will be detected.      
        '''   
#=======================================================================================     
# Update images on the screen and flip to the new screen.                
def update_screen(ai_settings, screen, ship, bullets): 
    # Fill the screen with the background color dfined as RGB() which takes only one argument: a color.
    screen.fill(ai_settings.bg_color) # Redraw the screen during each pass through the loop.
    '''
     We give the bullets parameter to update_screen() at x, which draws
    the bullets to the screen. The bullets.sprites() method returns a list of all
    sprites in the group bullets. To draw all fired bullets to the screen, we loop
    through the sprites in bullets and call draw_bullet() on each one   
    '''
    for bullet in bullets.sprites():  # Redraw all bullets behind ship and aliens.
        bullet.draw_bullet()
    # Now Render ship in the screen and Make the most recently drawn screen visible. 
    ship.blitme()                     # Render ship in the screen
    pygame.display.flip()             # Make the most recently drawn screen visible.
#===================================================================================
# Update position of bullets and get rid of old bullets. 
def update_bullets(bullets): 
    # Get rid of bullets that have run behind the screen.
    # If we DO NOT do this the'll still continue running and take memory
    # We shouldn’t remove items from a list or group within a for loop, so
    # we have to loop over a copy of the group. We use the copy() method to set
    # up the for loop u, which enables us to modify bullets inside the loop. We
    # check each bullet to see whether it has disappeared off the top of the screen
    # If it has, we remove it from bullets and theb insert a print statement
    # to show how many bullets currently exist in the game and verify that
    # they're being deleted.  
    bullets.update()  # Update bullet positions.    
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
           bullets.remove(bullet)
        #  print(len(bullets))
    '''
    We pass bullets to check_events() and update_screen(). We'll need to work
    with bullets in check_events() when the spacebar is pressed, and we'll need
    to update the bullets that are being drawn to the screen in update_screen().
    When you call update() on a group, the group automatically calls
    update() for each sprite in the group. The line bullets.update() calls
    bullet.update() for each bullet we place in the group bullets       
    '''  