from os import fpathconf
import socket
import threading

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.close()
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT) #header
        if (msg_len):
            msg = conn.recv(int(msg_len)).decode(FORMAT) #message
            if (msg == DISCONNECT_MSG): #Disconnect message
                connected =  False
                print(f"[CLIENT DISCONNECTED]] {addr}")
            else:
                print(f"[MESSAGE RECEIVED] {addr} {msg}")

    conn.close()

def start_server():
    print("[STARTING] Starting server...")
    server.listen()
    print(f"[RUNNING] Server running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


start_server()



