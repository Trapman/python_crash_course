import pygame

# one good thing about pygame is that it allows us to treat all game elements
# like they're rectangles. So we will use the .rect method a lot here

class Ship:
    """a class to manage the ship"""
    
    def __init__(self.ai_game):
        """initialize the ship and set its starting position"""
        """takes 2 parameters: self referece, and a reference to the current instance of the AlienInvasion class
        """this will give the Ship access to all the game resources defined in AlienInvasion
        self.screen = ai_game.screen #assign the screen an attribute of Ship so we can easily access it in the methods in this class
        self.screen_rect = ai_game.screen.get_rect() # access the screen's rect attribute and use it to place the ship in a specific location on the screen
        
        # load the image of the ship. try to use a bitmap (BMP)
        self.image = pygame.image.load('images/ship.bmp')  # this is just the location of the image
        self.rect = self.image.get_rect()
        
        # start each shit at the bottom center of the scree
        self.rect.midbottom = self.screen_react.midbottom
        
    def bliteme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
