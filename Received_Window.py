import pygame


# Received_Window class
class Received_Window(pygame.Surface):
    # Constructor
    def __init__(self):
        super().__init__((480, 415))
        super().fill((200, 200, 200))
    
    def update_window(self, serialized_list):
        # update if the length of the serialized list is not 0
        if len(serialized_list) != 0:
            super().fill((200, 200, 200))
            # get the image from
            img = pygame.image.fromstring(serialized_list[0], (450, 180), "RGBA")
            
            for i in range(len(self._image_list)):
                # update coordinates and redraw to screen
                self._image_coords[i] = (self._image_coords[i][0], self._image_coords[i][1] + 190)
                super().blit(self._image_list[i], self._image_coords[i])
            
            # draw new image at init coords and append to the list of images
            super().blit(img, self._init_coords)
            self._image_list.append(img)
            self._image_coords.append(self._init_coords)

            

    # protected member variables
    # list of images in the window
    _image_list = []
    #list of coordinates that correspond with images in the window
    _image_coords = []
    _init_coords = (10, 10)