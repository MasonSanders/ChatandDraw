import pygame
import threading
from socket import *
from Chat_Canvas import Chat_Canvas
from Button import Button
from Color_Button import Color_Button
from Clear_Button import Clear_Button
from Send_Button import Send_Button
from Received_Window import Received_Window


# main function for user interaction, drawing and sending
def interaction_main():
    # initialize pygame and the pygame window
    pygame.init()
    screen = pygame.display.set_mode([500, 700])
    draw_canv = Chat_Canvas()
    red_btn = Color_Button(draw_canv, (255, 0, 0))
    green_btn = Color_Button(draw_canv, (0, 255, 0))
    blue_btn = Color_Button(draw_canv, (0, 0, 255))
    erase_btn = Color_Button(draw_canv, (255, 255, 255))
    clear_btn = Clear_Button(draw_canv)
    send_btn = Send_Button(draw_canv, server)
    recv_window = Received_Window()

    # keep track of the mouse position
    mouse_x = 0
    mouse_y = 0

    # loop for user interaction
    running = True
    while running:
        # get information from pygame events and take appropriate action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                listen_to_server = False
            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check for where the mouse presses, whether it's on a button or the draw canvas
                # more convenient to check the y position first since categories of items
                # are organized by their height on the screen.
                if event.pos[1] <= 675 and event.pos[1] >= 495:
                    if event.pos[0] >= 25 and event.pos[0] <= 475:
                        draw_canv.set_drawing(True)
                if event.pos[1] <= 485 and event.pos[1] >= 436:
                    if event.pos[0] >= 25 and event.pos[0] <= 75:
                        red_btn.on_press()
                    if event.pos[0] >= 85 and event.pos[0] <= 135:
                        green_btn.on_press()
                    if event.pos[0] >= 145 and event.pos[0] <= 195:
                        blue_btn.on_press()
                    if event.pos[0] >= 205 and event.pos[0] <= 255:
                        erase_btn.on_press()
                    if event.pos[0] >= 265 and event.pos[0] <= 315:
                        clear_btn.on_press()
                    if event.pos[0] > 325 and event.pos[0] <= 375:
                        send_btn.on_press()
            if event.type == pygame.MOUSEBUTTONUP:
                draw_canv.set_drawing(False)

        # update the pygame window
        screen.fill((155, 155, 155))
        screen.blit(draw_canv, (25, 495))
        screen.blit(red_btn, (25, 435))
        screen.blit(green_btn, (85, 435))
        screen.blit(blue_btn, (145, 435))
        screen.blit(erase_btn, (205, 435))
        screen.blit(clear_btn, (265, 435))
        screen.blit(send_btn, (325, 435))
        screen.blit(recv_window, (10, 10))
        draw_canv.update_canvas(mouse_x - 25, mouse_y - 495)
        recv_window.update_window(serialized_list)
        #update serialized list to reflect when an item has been sent
        if len(serialized_list) != 0:
            serialized_list.pop(0)
        pygame.display.flip()
    # quit pygame after exiting the loop
    pygame.quit()
# End interaction_main

# main method to listen for contact from the server
def listen_main():
    byte_loader = []
    while True:
        # may receive multiple pieces of the data,
        # concatenate a list of the bytes received
        data = server.recv(4096)
        # try to resolve a quit message,
        # if the quit message can't be resolved,
        # 
        try:
            if data.decode() == "quit":
                break
        except:
            list_of_bytes = list(data)
            byte_loader += list_of_bytes

            if len(bytes(byte_loader)) == 324000:
                serialized_list.append(bytes(byte_loader))
                byte_loader = []
# End listen_main


# client side socket TCP setup
server_ip = "localhost"
server_port = 8000
server = socket(AF_INET, SOCK_STREAM)
server.connect((server_ip, server_port))

# list of serialized strings received from server
# acts as a queue, only 1 item from the queue will be
# released every GUI loop.
serialized_list = []


# call main
if __name__ == "__main__":
    # separate threads for handling user interactions and listening to the server
    draw_thread = threading.Thread(target=interaction_main)
    listen_thread = threading.Thread(target=listen_main)

    # start each thread
    draw_thread.start()
    listen_thread.start()

    # join threads back to the main thread once complete
    draw_thread.join()
    # once the gui thread joins, need the listener to join
    # send a quit message to the server, server will send back a quit messsage to the client
    msg = "quit"
    server.send(msg.encode())

    listen_thread.join()

# close connection to the server
server.close()
