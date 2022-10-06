import pygame
from pygame.sprite import Sprite
'''
Most of this class is like the Ship class except for the placement of the
alien. We initially place each alien near the top-left corner of the screen,
adding a space to the left of it that's equal to the alien's width and a space
above it equal to its height
'''
#======================================================================
#  A class to represent a single alien in the fleet.
#======================================================================
class Alien(Sprite):
    # Initialize the alien and set its starting position. 
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("Projects/AlienInvasion/images/alien.bmp")
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact position.
        self.x = float(self.rect.x)
    #=========================================================  
    # Draw the alien at its current location."""        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    #=========================================================
    # Move the alien right or left. 
    def update(self):
        '''
        Each time we update an alien's position, we move it to the right by the
        amount stored in alien_speed_factor. We track the alien's exact position
        with the self.x attribute, which can hold decimal values. We then use
        the value of self.x to update the position of the alien's rect 
        When multiplying by fleet_direction (= 1 or -1) we set direction
        for moving either right or left (1 = right; -1 = left )       
        '''
        self.x += (self.ai_settings.alien_speed_factor * 
                   self.ai_settings.fleet_direction)   
        self.rect.x = self.x
    #=========================================================
    # Return True if alien is at edge of screen.
    # We'll use this check in update()-function above 
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True 
        '''
        The alien is at the right edge if the right attribute of its rect 
        is greater than or equal to the right attribute of the screen's rect.
        It's at the left edge if its left value is less than or equal to 0.        
        '''  
    #=========================================================
    
    
    #=========================================================
    