import socket
import Constants

def get_name():
    client_name = input("Enter your name: ")
    while client_name == "":
        print("Name cannot be empty")
        client_name = input("Enter your name: ")
    return client_name.strip()

def send_message(client):
    text_message = input("Your message: ")
    client.send(text_message.encode())
    return text_message


try:
    name = get_name()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((Constants.SERVER_HOST, Constants.SERVER_PORT))
    # print("Client connected")
    client_socket.send(name.encode())

    message = ""
    while message != Constants.EXIT:
        messages = client_socket.recv(Constants.BUFFER_LENGTH).decode()
        print(messages)
        message = send_message(client_socket)
    client_socket.close()
except InterruptedError:
    print("Lost connection from Client")