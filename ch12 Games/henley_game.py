import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """This initializes the game and creates game resources"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.disply.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
    def run_game(self):
        """This starts the main loop for the game."""
        while True:
            # watches for keyboard and mouse events
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
                    
                # redraw the screen during each pass through the loop
                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()
                    
            # makes the most recently drawn screen visible
            pygame.display.flip()
            
if __name__ == '__main__':
    # makes a game instance, and runs the game
    ai = AlienInvasion()
    ai.run_game()
####
####
