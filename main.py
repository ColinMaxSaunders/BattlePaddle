"""
MAIN METHOD FOR THE PYTHON SCRIPT
This script is designed to be run as a standalone program.
"""

import sys
import pygame
from constants import *

def main():
    # Initialize Pygame
    pygame.init

    """Set up the display based on user defined variables in activeSession.py."""
    #getHorizontalResolution = pygame.display.Info()
    #getVerticalResolution = pygame.display.Info()
    #print(f"Horizontal Resolution: {getHorizontalResolution.current_w}")
    #print(f"Vertical Resolution: {getVerticalResolution.current_h}")
    #save

    """Set up the display based on the constants defined in constants.py."""

    #send parameters to the display savedSettings.py

    screen = savedSettings().screen


    pygame.display.set_caption("Pygame Window")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()