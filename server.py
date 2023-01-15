#server.py
from socket import *
import threading


# setup the server
port = 8000
s = socket(AF_INET, SOCK_STREAM)

# if not running the program through localhost, please
# switch the port from 8000 to something else as
# port 8000 should not be open to the internet.
s.bind(("localhost", port))

# clients list
clients = []

def listen_to_client(conn, address):
    # code for the server to listen and respond to clients
    # this function is running in a thread for each client connected
    while True:
        msg = conn.recv(4096)
        # try to see if the message is a quit message,
        # if so, respond to the client with a quit message
        # to tell it to stop listening
        try:
            if msg.decode() == "quit":
                conn.send(msg)
                clients.remove(conn)
                break
        except:
            for client in clients:
                client.send(msg)
    conn.close()
    

def get_new_clients(s):
    # this function runs in a thread and allows for getting new clients
    # upon receiving a new client, that client is added to a clients list
    while True:
        conn, address = s.accept()
        clients.append(conn)

        # start a new thread to listen to the new client
        threading.Thread(target=listen_to_client, args=(conn, address)).start()


def main():
    # server can listen for at most 5 connections, start a new thread that allows for getting clients.
    s.listen(5)
    threading.Thread(target=get_new_clients, args=(s,)).start()
    

if __name__ == "__main__":
    main()


