# Color_Button.py

import pygame
from Chat_Canvas import Chat_Canvas
from Button import Button

# concrete send button class
class Color_Button(Button):

    def __init__(self, canv, color):
        # setup the color button
        super().__init__(canv)
        self._color = color
        super().fill(self._color)
        self._draw_canvas = canv

    def on_press(self):
        # call the canvas to set the color of the brush
        self._draw_canvas.set_brush_color(self._color)
    
    _color = 0