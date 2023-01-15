# Button.py

import pygame
from Chat_Canvas import Chat_Canvas

"""
Button is meant to be an abstract class.
Since python doesn't support abstract classes
and interfaces by default. I used the pass command
for on_press to make it somewhat of an abstract method
The button can be instantiated, but it does nothing
and appears as a black square.
"""

# Button abstract class
class Button(pygame.Surface):
    def __init__(self, canv):
        # is a pygame surface
        super().__init__((50, 50))
        super().fill((0, 0, 0))
        self._draw_canvaas = canv

    def on_press(self):
        pass
    
    _draw_canvas = Chat_Canvas()