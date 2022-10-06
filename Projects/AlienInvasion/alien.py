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
    #Initialize the alien and set its starting position. 
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('"Projects/AlienInvasion/images/alien.bmp')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact position.
        self.x = float(self.rect.x)
    #=========================================================  
    #Draw the alien at its current location."""        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    #=========================================================