"""
This file is to set savedSettings so all future sessions start with the same settings.
"""


"""
File Decision between First Game Settings versus SavedSettings.
"""

isFirstRun = markerCheck()


if isFirstRun = true#firstTimeRunningGame
then #useDefaultResoltion

elif isFirstRun = False#!firstTimeRunningGame
then #useSavedResoltion


else throw Exception("Critical Exception, could not determine if First Run of Game.")

"""
Default Settings for first time startup.

"""
DEFAULT_SCREEN_WIDTH = 1280
DEFAULT_SCREEN_HEIGHT = 720



"""
Saved Settings for future sessions.
These settings will be loaded from savedSettings.py.
"""
SCREEN_WIDTH = DEFAULT_SCREEN_WIDTH
SCREEN_HEIGHT = DEFAULT_SCREEN_HEIGHT


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
return screen