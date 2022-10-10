import pygame.font # import module, which lets Pygame render text on screen
'''
Because Pygame doesn't have a built-in method for making buttons, we'll write 
a Button class to create a filled rectangle with a label. You can use this
code to make any button in a game. 
'''
class Button():
    def __init__(self, ai_settings, screen, msg):
        # Initialize button attributes.(size, color etc..)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0) # color the button's rect object = green
        self.text_color = (255, 255, 255)
        # The None argument tells Pygame to use the default font, and 48 determines the size of the text.
        self.font = pygame.font.SysFont(None, 48)
        # Build the button's rect object and center it.
        # Pygame works with text by rendering the string you want to display as an image
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # The button message needs to be prepped only once.
        self.prep_msg(msg)
    #===================================================================================
    # Turn msg into a rendered image and center text on the button. The button message
    # needs to be prepped only once. font.render() turns the text stored in msg into 
    # an image. It also takes a Boolean value to turn antialiasing on or off 
    # (antialiasing makes the edges of the text smoother). The remaining arguments are
    # the specified font color and background color. We set antialiasing to True and 
    # set the text background to the same color as the button. If you don't include 
    # background color, Pygame will render the font with a transparent background.
    def prep_msg(self, msg):
        # Turn the text stored in msg into an image
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # Center the text image on the button by creating a rect from the image and 
        # setting its center attribute to match that of the button
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    #===================================================================================
    # Draw blank button and then draw message.
    def draw_button(self):
        # Draw the rectangular portion of the button.
        self.screen.fill(self.button_color, self.rect)
        # Draw the text image to the screen, passing it 
        # an image and the rect object associated with the image
        self.screen.blit(self.msg_image, self.msg_image_rect)
    #===================================================================================
    
    
    