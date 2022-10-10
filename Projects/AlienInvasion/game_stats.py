'''
Now we need to figure out what happens when an alien collides with the
ship. Instead of destroying the ship instance and creating a new one, we’ll
count how many times the ship has been hit by tracking statistics for the
game. (Tracking statistics will also be useful for scoring.)
'''
# Track statistics for Alien Invasion. 
class GameStats():
    #===============================================================================  
    #Initialize statistics. 
    def __init__(self, ai_settings): 
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True # Start Alien Invasion in an active state.   
    #===============================================================================    
    # Initialize statistics that can change during the game.W'll initialize 
    # most of the statistics here instead of directly in __init__(). 
    # We’ll call this method from __init__() so the statistics are set properly 
    # when the GameStats instance is first created. We'll also be able to call 
    # reset_stats() any time the player starts a new game.  
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
    #===============================================================================  