import pygame
from pygame.sprite import Sprite
#====================================================================================
''' 
The bullet is not based on an image so we have to build a rect 
from scratch using the pygame.Rect() class. This class requires 
the x- and y-coordinates of the top-left corner of the rect, and 
the width and height of the rect. We initialize the rect at (0, 0),
but we'll move it to the correct location in the next two lines, 
because the bullet's position is dependent on the ship's position. 
We get the width and height of the bullet from the values stored 
in ai_settings.    
'''
#===================================================================
#      A class to manage bullets fired from the ship
#===================================================================
class Bullet(Sprite):  # a child class that inherits from BASE-clase = Sprite
    def __init__(self, ai_settings, screen, ship):
        # Create a bullet object at the ship's current position. 
        # super(Bullet, self).__init__() # This is Python 2.7 syntax that also works 
        super().__init__()               # But we preffer Python 3.0 syntax !!!
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # Set the bullet’s centerx to be the same as the ship’s rect.centerx.
        self.rect.centerx = ship.rect.centerx
        # The bullet should emerge from the top of the ship, so we set the top of the
        # bullet’s rect to match the top of the ship’s rect, making it look like the 
        # bullet is fired from the ship
        self.rect.top = ship.rect.top
        # Store the bullet's position as a decimal value so we could make 
        # fine adjustments to the bullet’s speed
        self.y = float(self.rect.y)
        # Store the bullet’s color and speed settings 
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    #==================================================================================
    # Move the bullet up the screen. Note, bullet's x-coordinate value never changes
    # because it moves only vertically in a straight line.     
    def update(self): # Using speed_factor we can increase\decrease the speed by ratio      
        self.y -= self.speed_factor # Decrease the decimal Y-position of the bullet. 
        self.rect.y = self.y        # Update the rect position.
    #====================================================================
    # Draw the bullet to the screen. Fills the part of the screen defined 
    # by the bullet’s rect with the color stored in self.color
    def draw_bullet(self): 
        pygame.draw.rect(self.screen, self.color, self.rect)
