import pygame

# chat_canvas class
class Chat_Canvas(pygame.Surface):

    # Constructor
    def __init__(self):
        super().__init__((450, 180))
        super().fill((255, 255, 255))
    # End Constructor

    # set_drawing method: sets the drawing state of the canvas
    def set_drawing(self, draw_mode):
        if draw_mode == False:
            self._is_drawing = False
            self._last_mx = -1
            self._last_my = -1
        if draw_mode == True:
            self._is_drawing = True
    # End set_drawing

    # update_canvas method: updates the canvas by drawing any lines that need to be drawn
    def update_canvas(self, mx, my):
        if self._is_drawing:
            # check the bounds so that you can't draw outside the canvas
            if mx >= 0 and my >= 0:
                if mx <= 450 and my <= 180:
                    # draw a line between the previous position of the mouse and the current position
                    if self._last_mx != -1 and self._last_my != -1:
                        pygame.draw.line(self, self._brush_color, (self._last_mx, self._last_my), (mx, my), self._brush_size)
                    else:
                        pygame.draw.circle(self, self._brush_color, (mx, my), self._brush_size // 2)
                    self._last_mx = mx
                    self._last_my = my
    # End update_canvas

    def set_brush_color(self, color):
        self._brush_color = color
        
        # set the brush size larger when in erase mode
        if self._brush_color == (255, 255, 255):
            self._brush_size = 6
        else:
            self._brush_size = 3
        

    # clear_canvas method: fills the canvas by filling completely white
    def clear_canvas(self):
        super().fill((255, 255, 255))
    # End clear_canvas

    # protected member variables
    _is_drawing = False
    _brush_size = 3
    _brush_color = (255, 0, 0)
    _last_mx = -1
    _last_my = -1