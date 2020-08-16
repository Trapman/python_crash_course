"""
Created on Sat Aug 15 21:50:20 2020

@author: das68451
"""
Instead of adding settings throughout the actual code, we will create 
a settings.py file within the folder and we can then edit everything in there
and then call it in the actual program"""

class Settings:
    """A class to store all of the settings for the game"""
    
    def __init__(self):
        """initialize the game's settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
