# Clear_Button.py

import pygame
from Chat_Canvas import Chat_Canvas
from Button import Button


# concrete clear button class
class Clear_Button(Button):
    def __init__(self, canv):
        # setup the clear button
        super().__init__(canv)
        clear_icon = pygame.image.load("Clear_Icon.png")
        super().blit(clear_icon, (0, 0))
        self._draw_canvas = canv
    
    def on_press(self):
        # call the canvas to clear the drawable area 
        self._draw_canvas.clear_canvas()
        