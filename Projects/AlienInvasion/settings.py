'''
This file class called Settings to store all the settings in one place. 
This approach allows us to pass around one settings object instead of many 
individual settings.In addition, it makes our function calls simpler and makes
it easier to modify the game’s appearance as our project grows. To modify the game, 
we’ll simply change some values in settings.py instead of searching for different
settings throughout our files.
'''
#A class to store all settings for Alien Invasion.
class Settings():  
    #===========================================================================
    # "Initialize the game's static settings. 
    def __init__(self): 
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
       # Limit number of Ships
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 15 # Try 300 The bullet will be like a horizontal line
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3 # Limit to three bullets at a time.

        '''
        The setting fleet_drop_speed controls how quickly the fleet drops down
        the screen each time an alien reaches either edge. It's helpful to separate
        this speed from the aliens' horizontal speed so you can adjust the two
        speeds independently.
        '''         
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1   # How quickly the game speeds up
        # How quickly the alien point values increase if game raises speed
        self.score_scale = 1.5  
        self.initialize_dynamic_settings() 
    #===========================================================================   
    # Initialize settings that change throughout the game.     
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5 # Adjust position by 1.5 pixels rather than 1 pixel
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1 
        '''
        To implement the setting fleet_direction, we could use a text value, such
        as 'left' or 'right', but we'd end up with if-elif statements testing for 
        the fleet direction. Instead, because we have only two directions to deal with,
        let's use the values 1 and -1 and switch between them each time the fleet
        changes direction. (Using numbers also makes sense because moving right
        involves adding to each alien's x-coordinate value, and moving left involves
        subtracting from each alien's x-coordinate value.) 
        '''
        self.fleet_direction = 1 # 1 = right; -1 = left
         # Scoring
        self.alien_points = 1
    #===========================================================================   
    # Increase speed settings.       
    def increase_speed(self):
        self.ship_speed_factor   *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor  *= self.speedup_scale 
        # If game speed increase, points are multiplied by coeff
        self.alien_points = int(self.alien_points * self.score_scale)