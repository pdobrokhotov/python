'''
We are moving here the code that manages events to a separate function called check_events().
This will simplify run_game() and isolate the event management loop. 
Isolating the event loop allows you to manage events separately
from other aspects of the game, like updating the screen
'''
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

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
def update_screen(ai_settings, screen, ship, aliens, bullets):
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
    '''
    When you call draw() on a group, Pygame automatically draws each element
    in the group at the position defined by its rect attribute. In this case,
    aliens.draw(screen) draws each alien in the group to the screen.
    '''
    aliens.draw(screen)               # Render Group of Aliens in the screen
    pygame.display.flip()             # Make the most recently drawn screen visible.
#===================================================================================
# Update position of bullets and get rid of old bullets. 
def update_bullets(ai_settings, screen, ship, aliens, bullets):
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
    # Respond to bullet-alien collisions.
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    '''
    We pass bullets to check_events() and update_screen(). We'll need to work
    with bullets in check_events() when the spacebar is pressed, and we'll need
    to update the bullets that are being drawn to the screen in update_screen().
    When you call update() on a group, the group automatically calls
    update() for each sprite in the group. The line bullets.update() calls
    bullet.update() for each bullet we place in the group bullets       
    '''   
#===================================================================================
# Respond to bullet-alien collisions. 
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):   
    # Check for any bullets that have hit aliens. 
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    '''
    The new line we added loops through each bullet in the group bullets and
    then loops through each alien in the group aliens. Whenever the rects of 
    a bullet and alien overlap, groupcollide() adds a key-value pair to the 
    dictionary it returns. The two True arguments tell Pygame if to delete
    the bullets and aliens that have collided.    
    '''
    # If the group aliens is empty destroy existing bullets and create new fleet.
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)  
        
#=================================================================================== 
# Create a full fleet of aliens.
def create_fleet(ai_settings, screen, ship, aliens):
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width. 
    '''
    We've already thought through most of this code. We need to know the
    alien's width and height in order to place aliens, so we create an alien
    before we perform calculations. This alien won't be part of the fleet, so we
    don't add it to the group aliens.  
    The definition of create_fleet() also has a new parameter for the ship object, 
    which means we need to include the ship argument in the call to create_fleet() 
    in alien_invasion.py : gf.create_fleet(ai_settings, screen, ship, aliens) 
    '''
    alien = Alien(ai_settings, screen)
    # Get number of Aliens that can fit into the screen in X-Axis
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # Get number of Aliens that can fit into the screen in Y-Axis
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # To create multiple rows, we use two nested loops: one outer loop Y
    # and one inner loop X. The inner loop creates the aliens in one row. 
    # The outer loop counts from 0 to the number of rows we want; 
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,row_number)    
 
#===================================================================================
# Determine the number of aliens that fit in a row. 
def get_number_aliens_x(ai_settings, alien_width):
    '''
    Calculate the horizontal space available for aliens and the number 
    of aliens that can fit into that space. The only change here from 
    our original formulas is that we're using int() to ensure we end up 
    with an integer number of aliens. The only change here from our original
    formulas is that we're using int() to ensure we end up with an integer 
    number of aliens x because  we don't want to create partial aliens, 
    and the range() function needs an integer. The int() function drops 
    the decimal part of a number, effectively rounding down.
    (This is helpful  because we'd rather have a little extra space 
    in each row than an overly crowded row.) 
    '''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # We use int() to ensure we end up with an integer number of aliens
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
#===================================================================================
# Create an alien and place it in the row. 
       
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    '''
    Note, that here we also change an alien's y-coordinate value when it's
    not in the first row by starting with one alien's height to create empty space
    at the top of the screen. Each row starts two alien heights below the last row,
    so we multiply the alien height by two and then by the row number. The first
    row number is 0, so the vertical placement of the first row is unchanged. 
    All subsequent rows are placed farther down the screen.
    '''
    # Get the alien's width from its rect attribute and store this value in 
    # alien_width so we don't have to keep working through the rect attribute.
    # Each alien is pushed to the right one alien width from the left margin    
    alien_width = alien.rect.width
    # Set its x-coordinate value to place it in the row
    '''
    To acheve this we multiply the alien width by 2 to account for the space 
    each alien takes up,including the empty space to its right, and we multiply
    this amount by the alien's position in the row. Then we add each new alien 
    to the group aliens. 
    '''
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien) 
#===================================================================================
#  Determine the number of rows of aliens that fit on the screen.   
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
#===================================================================================
# Update the postions of all aliens in the fleet.
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''
    We use the update() method on the aliens group, which automatically
    calls each alien's update() method. When you run Alien Invasion now, you
    should see the fleet move right and disappear off the side of the screen  
    '''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Look for alien-ship collisions.
    '''
    The method spritecollideany() takes two arguments: a sprite and a
    group. The method looks for any member of the group that''s collided with
    the sprite and stops looping through the group as soon as it finds one member
    that has collided with the sprite. Here, it loops through the group aliens
    and returns the first alien it finds that has collided with ship. If no collisions 
    occur, spritecollideany() returns None and the if block won't execute
    '''
    if pygame.sprite.spritecollideany(ship, aliens):
        #print("Ship hit!!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        
    # Look for aliens hitting the bottom of the screen.
    # We call check_aliens_bottom() after updating the positions of all 
    # the aliens and after looking for alien-ship collisions
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)    
#===================================================================================
# Respond appropriately if any aliens have reached an edge."""
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
    '''
    Here we loop through the fleet and call check_edges() on each alien.
    If check_edges() returns True, we know an alien is at an edge and
    the whole fleet needs to change direction, so we call change_fleet_direction()
    and break out of the loop. In change_fleet_direction(), we loop through all
    the aliens and drop each one using the setting fleet_drop_speed. Then we  
    change the value of fleet_direction by multiplying its current value by -1.
    '''
#===================================================================================
# Drop the entire fleet and change the fleet's direction. 
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    # After dropping above change direction to the left by multiplying to (=-1)
    ai_settings.fleet_direction *= -1
#===================================================================================
# Respond to ship being hit by alien. 
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Pause.
        sleep(0.5)
    else:
        stats.game_active = False
        
    '''
    Notice that we never make more than one ship; we make only one ship instance for the
    whole game and recenter it whenever the ship has been hit. The statistic ships_left
    will tell us when the player has run out of ships.
    '''
#===================================================================================
# Check if any aliens have reached the bottom of the screen.
# An alien reaches the bottom when its rect.bottom value is greater 
# than or equal to the screen’s rect.bottom attribute
# If so treat the same as if Ship was hit
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


#===================================================================================
#===================================================================================
#===================================================================================
