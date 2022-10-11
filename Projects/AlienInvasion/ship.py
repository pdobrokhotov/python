# we need this main LIBRARY that has everything for coding our game
import pygame
# we need SPRITE to use a GROUP of remained ships rendered at the top of screen
from pygame.sprite import Sprite  
'''
To use our ship, we'll write a module called ship, which contains the class Ship. 
This class will manage most of the behavior of the player's ship.
First, we import the pygame module. The __init__() method of Ship takes
two parameters: the self reference and the screen where we'll draw the ship.
To load the image, we call pygame.image.load(). This function returns a
surface representing the ship, which we store in self.image.
Once the image is loaded, we use get_rect() to access the surface's rect
attribute. One reason Pygame is so efficient is that it lets you treat game
elements like rectangles (rects), even if they're not exactly shaped like rectangles.
Treating an element as a rectangle is efficient because rectangles
are simple geometric shapes. This approach usually works well enough that
no one playing the game will notice that we're not working with the exact
shape of each game element.
When working with a rect object, you can use the x- and y-coordinates
of the top, bottom, left, and right edges of the rectangle, as well as the
center. You can set any of these values to determine the current position
of the rect.
==========================================================================
'''
# Our ship-class is based on parent class = sprite that allows groups of Ships
class Ship(Sprite): 
    #==============================================================================
    # Initialize the ship and set its starting position, but make sure it inherits
    # it's parent (super) class = SPRITE. For this call INIT-method of parent class
    def __init__(self, ai_settings, screen): 
        super(Ship, self).__init__() # inherit super class
        self.screen = screen
        self.ai_settings = ai_settings # turn this parameter into an attribute, so we can use it in update()
        #image_ship_path = "D:\My Documents\python\Projects\AlienInvasion\images\ship.bmp" # = absolute path
        image_ship_path = "Projects/AlienInvasion/images/ship.bmp" # = relative path
        self.image = pygame.image.load(image_ship_path) # Load the ship image and get its rect.
        self.rect = self.image.get_rect() # store rect-obkect for Ship image
        self.screen_rect = screen.get_rect() # access the surface’s rect attribute (i.e. our screen)
        # Start each new ship at the bottom center of the screen
        # But to do so, we  first had to store the screen’s rect in self.screen_rect
        # Make the value of self.rect.centerx (the x-coordinate of the ship’s center) 
        # match the centerx attribute of the screen’s rect. Also Position the ship image 
        # so it's centered horizontally and aligned with the bottom of the screen.        
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom
        # the rect attrib can store only the integer. Thus to store the ship’s position 
        # accurately, we define new attribute self.center, which can hold decimal values
        self.center = float(self.rect.centerx) # Store a decimal value for the ship's center.
        # Movement flag to distinguish button single PRESS from CONSTANT
        self.moving_right = False # we move right keeping arrow-button pressed
        self.moving_left  = False # we move left keeping  arrow-button pressed
        '''
        When you're working at an edge of the screen,
        work with the top, bottom, left, or right attributes. When you're adjusting
        the horizontal or vertical placement of the rect, you can just use the x and y
        attributes, which are the x- and y-coordinates of its top-left corner. These
        attributes spare you from having to do calculations that game developers
        formerly had to do manually, and you'll find you'll use them often    
        '''
    #==============================================================================
    def update(self): # Update the ship's position based on the movement flag. 
        # Update the ship's self.center value, not the self.rect.centerx as was before. !!!
        # Also check not to run behind the screen borders both in the right and left positions
        if self.moving_right and self.rect.right < self.screen_rect.right: # stop if out of border
           self.center += self.ai_settings.ship_speed_factor # incremet x-coordinate (move right)
        if self.moving_left and self.rect.left > 0: # stop if out of border
           self.center -= self.ai_settings.ship_speed_factor # decremet x-coordinate (move left)
        # After self.center is made of decimal type, we use the new value to
        # update self.rect.centerx, which controls the position of the ship y. 
        # Though only the integer portion of self.center will be stored in self.rect.centerx, 
        # but that’s fine for displaying the ship.           
        self.rect.centerx = self.center # Update rect object from self.center.
    #==============================================================================
    def blitme(self): # Draw the ship at its current location. 
        self.screen.blit(self.image, self.rect)
        
    '''
    When working with a rect object, you can use the x- and y-coordinates
    of the top, bottom, left, and right edges of the rectangle, as well as the
    center. You can set any of these values to determine the current position
    of the rect.
    When you're centering a game element, work with the center, centerx, or
    centery attributes of a rect. When you're working at an edge of the screen,
    work with the top, bottom, left, or right attributes. When you're adjusting
    the horizontal or vertical placement of the rect, you can just use the x and
    y attributes, which are the x- and y-coordinates of its top-left corner. These
    attributes spare you from having to do calculations that game developers
    formerly had to do manually, and you'll find you'll use them often
    ----------------------- NOTE -------------------------------------------------
    In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates
    increase as you go down and to the right. On a 1200 by 800 screen, the origin is at
    the top-left corner, and the bottom-right corner has the coordinates (1200, 800).
    --------------------------------------------------------------------------------
    '''
    #==============================================================================
    # Center the ship on the screen. To center the ship, we set the value of the 
    # ship's center attribute to match the center of the screen, which we get 
    # through the screen_rect attribute. This attribute can be used for setting
    # object's positin like we did it earlier: self.rect.centerx = self.center
    def center_ship(self):
        self.center = self.screen_rect.centerx