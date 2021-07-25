import socket

PORT = 5050
SERVER = '192.168.2.7'
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):
    #encode
    message = msg.encode(FORMAT)
    #construct header
    msg_len = str(len(message)).encode(FORMAT)
    msg_len += b' ' * (HEADER - len(msg_len))
    #send
    client.send(msg_len) #header
    client.send(message) #message

while True:
    msg = input("Type your message: ")
    if msg != "!":
        send_msg(msg)
    else:
        break
send_msg(DISCONNECT_MSG)
client.close()