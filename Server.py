import socket
from _thread import *
import Constants

messages = [Constants.CHAT_SEPARATOR]

def send_messages(connect):
    all_messages = Constants.DELIMITER.join(messages)
    all_messages += '\n' + Constants.CHAT_SEPARATOR
    connect.send(all_messages.encode())


def client_thread(connect):
    send_messages(connect)
    try:
        name = connect.recv(Constants.BUFFER_LENGTH).decode()
        print("Name received: " + name)
        message_text = ""
        while message_text != Constants.EXIT:
            message_text = connect.recv(Constants.BUFFER_LENGTH).decode()
            print("Message received")
            if message_text == Constants.EXIT:
                continue
            messages.append(name + ": " + message_text)
            send_messages(connect)

        connect.close()
        print(name + " left the chat")
    except OSError:
        print("Lost connection from Client")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((Constants.SERVER_HOST, Constants.SERVER_PORT))
server_socket.listen()

try:
    while True:
        client, address = server_socket.accept()
        print("New client connected")
        start_new_thread(client_thread, (client, ))
except InterruptedError:
    print("Lost connection from Server")
