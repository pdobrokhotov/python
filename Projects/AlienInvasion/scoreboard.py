import pygame.font # we need this 'cause ScoreboardClass writes text to the screen 
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
        # Prepare the initial score image.
        self.prep_score()
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
    # Draw score to the screen.  
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect) 
    #=============================================================  

    