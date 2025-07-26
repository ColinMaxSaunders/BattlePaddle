"""
MAIN METHOD FOR THE PYTHON SCRIPT
This script is designed to be run as a standalone program.
"""

import sys
import pygame
from constants import *
from player import Player
from paddle import Paddle
from playingField import PlayingField
from shot import Shot

def main():
    # Initialize Pygame
    pygame.init

    hScreenSize = 0
    vScreenSize = 0

    """Set up the display based on user defined variables in activeSession.py."""
    #getHorizontalResolution = pygame.display.Info()
    #getVerticalResolution = pygame.display.Info()
    #print(f"Horizontal Resolution: {getHorizontalResolution.current_w}")
    #print(f"Vertical Resolution: {getVerticalResolution.current_h}")
    #save

    """Set up the display based on the constants defined in constants.py."""

    #send parameters to the display savedSettings.py
    #    hScreenSize = savedSettings().SCREEN_WIDTH
    #    vScreenSize = savedSettings().SCREEN_HEIGHT
    # Initialize the screen with the saved settings
    #screen = pygame.display.set_mode((getHorizontalResolution.current_w, getVerticalResolution.current_h))
    #screen = pygame.display.set_mode((getHorizontalResolution, getVerticalResolution))
    #screen = pygame.display.set_mode((hScreeSize, vScreenSize))
    #screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    #screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.RESIZABLE)

    screen = pygame.display.set_mode((hScreenSize, vScreenSize))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    paddles = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Paddle.containers = (paddles, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    PlayingField.containers = updatable
    playing_field = PlayingField()

    pygame.display.set_caption("Pygame Window")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color
        screen.fill((0, 0, 0))

        for obj in drawable:
         obj.draw(screen)

        # Update the display
        pygame.display.flip()

        dt = clock.tick(240) / 1000
    # Quit Pygame
    pygame.quit()
    
    """If there are more windoes than just the play window, then we need to close them all."""
    #sys.exit()

    if __name__ == "__main__":
    main()