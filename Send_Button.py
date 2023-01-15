# Send_Button.py
import pygame
import pickle
from Chat_Canvas import Chat_Canvas
from Button import Button

# concrete send button class
class Send_Button(Button):
    def __init__(self, canv, server):
        # set up the send button
        super().__init__(canv)
        # load an icon for the button
        send_icon = pygame.image.load("Send_Icon.png")
        super().blit(send_icon, (0, 0))
        # assign the server and draw canvas
        self._draw_canvas = canv
        self._server = server

    def on_press(self):
        # on press should serialize the
        self.serialize_and_send()
        self._draw_canvas.clear_canvas()
    
    def serialize_and_send(self):
        # pygame includes serialization for surfaces with tostring,
        # tostring doesn't convert to string, but really bytes, to allow for
        # sending
        serialization = pygame.image.tostring(self._draw_canvas, "RGBA")
        self.send_to_server(serialization)

    # send the serialized message to the server
    def send_to_server(self, serialization):
        self._server.send(serialization)

    _server = 0