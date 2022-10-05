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
'''
import pygame

#====================================================================================
class Ship():
    #--------------------------------------------------------------------------------
    def __init__(self, screen): # Initialize the ship and set its starting position. 
        self.screen = screen
        self.image = pygame.image.load('images\ship.bmp') # Load the ship image and get its rect.
        self.rect = self.image.get_rect() # store rect-obkect for Ship image
        self.screen_rect = screen.get_rect() # access the surface’s rect attribute (i.e. our screen)
        # Start each new ship at the bottom center of the screen
        # But to do so, we  first had to store the screen’s rect in self.screen_rect
        # Make the value of self.rect.centerx (the x-coordinate of the ship’s center) 
        # match the centerx attribute of the screen’s rect
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom
        # @ lines above position the ship image so it's centered horizontally and aligned 
        # with the bottom of the screen.
        '''
        When you’re working at an edge of the screen,
        work with the top, bottom, left, or right attributes. When you’re adjusting
        the horizontal or vertical placement of the rect, you can just use the x and y
        attributes, which are the x- and y-coordinates of its top-left corner. These
        attributes spare you from having to do calculations that game developers
        formerly had to do manually, and you’ll find you’ll use them often    
        '''
    #--------------------------------------------------------------------------------    
    def blitme(self): # Draw the ship at its current location. 
        self.screen.blit(self.image, self.rect)
        
'''
When working with a rect object, you can use the x- and y-coordinates
of the top, bottom, left, and right edges of the rectangle, as well as the
center. You can set any of these values to determine the current position
of the rect.
When you’re centering a game element, work with the center, centerx, or
centery attributes of a rect. When you’re working at an edge of the screen,
work with the top, bottom, left, or right attributes. When you’re adjusting
the horizontal or vertical placement of the rect, you can just use the x and
y attributes, which are the x- and y-coordinates of its top-left corner. These
attributes spare you from having to do calculations that game developers
formerly had to do manually, and you’ll find you’ll use them often
----------------------- NOTE -------------------------------------------------
In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates
increase as you go down and to the right. On a 1200 by 800 screen, the origin is at
the top-left corner, and the bottom-right corner has the coordinates (1200, 800).
--------------------------------------------------------------------------------
'''