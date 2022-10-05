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
    def __init__(self): #Initialize the game's settings." 
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)