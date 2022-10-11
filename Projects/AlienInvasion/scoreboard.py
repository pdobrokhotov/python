import pygame.font # we need this 'cause ScoreboardClass writes text to the screen 
# Because we’re making a group of ships, we import the Group and Ship classes
from pygame.sprite import Group
from ship import Ship
#==================================================================================
# A class to report scoring information. 
class Scoreboard():
    #=============================================================
    # Initialize scorekeeping attributes."""
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score image. (i.e. render them on screen)
        self.prep_score()
        self.prep_high_score() # this score SHOULD NOT be reset
        self.prep_level()      # we always start with 1st level
        self.prep_ships()      # render remaining ships at the top
    #=============================================================
    # Turn the score into a rendered image.
    def prep_score(self):
        # Turn the numerical value stats.score into a string. 
        # But we better round the score to the nearst 10,100,100 etc,
        # because it can be multiplied by coeff if we reach new level 
        # and game speed increases
        # score_str = str(self.stats.score) # instead of this line we use 2 lines below
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score) # insert commas into numbers  
        
        
        # Create the image based on score-string above and display it
        # at the top right of the screen. To display it clearly onscreen, 
        # we pass the screen’s background color to render() 
        # as well as a text color.
        self.score_image = self.font.render(score_str, True,
                                            self.text_color,
                                            self.ai_settings.bg_color)
        '''
        We'll position the score in the upper-right corner of the screen and
        have it expand to the left as the score increases and the width of the number
        grows. To make sure the score always lines up with the right side of the
        screen, we create a rect called score_rect w and set its right edge 20 pixels
        from the right screen edge x. We then place the top edge 20 pixels
        down from the top of the screen y.
        '''
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    #=============================================================
    # Turn the high score into a rendered image. 
    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))  
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_color, self.ai_settings.bg_color)
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top  
    #=============================================================
    # Turn the level into a rendered image.       
    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), 
                                            True,
                                            self.text_color, 
                                            self.ai_settings.bg_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10   
        '''
        The method prep_level() creates an image from the value stored in
        stats.level and sets the image's right attribute to match the score's 
        right attribute. It then sets the top attribute 10 pixels beneath the
        bottom of the score image to leave space between the score and the level
        ''' 
    #=============================================================
    # Show how many ships are left.
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    '''
    The prep_ships() method creates an empty group = self.ships, to hold the ship
    instances. To fill this group, a loop runs once for every ship the player has 
    left. Inside the loop we create a new ship and set each ship's x-coordinate 
    value so the ships appear next to each other with a 10-pixel margin on the left
    side of the group of ships. We set the y-coordinate value 10 pixels down from 
    the top of the screen so the ships line up with the score image x. 
    Finally, we add each new ship to the group ships y.
    '''    
    #=============================================================  
    # Draw scores and ships to the screen. 
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect) 
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships using draw() on the group
        self.ships.draw(self.screen)
    #=============================================================  

    