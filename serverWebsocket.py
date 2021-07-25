import asyncio
import websockets

HOST = "192.168.2.10"
PORT = 8765
DISCONNECT_MSG="!"

ESP_MESSAGE = "ESP"
espWebsocket = 0


async def parseESPMessage(msg):
    print (f'[ESP MESSAGE] {msg}')
    pass

async def parseClientMessage(msg):
    print(f"[CLIENT MESSAGE] {msg}")
    await espWebsocket.send(msg)


async def handle_client(websocket, path):
    global espWebsocket
    print("[NEW CONNECTION ESTABLISHED]")
    connected = True
    isESP = False
    isFirstMessage = True
    while connected:
        msg = await websocket.recv()
        if (msg):
            # isESP init
            if isFirstMessage:
                isESP = msg == ESP_MESSAGE
                if isESP:
                    print('[ESP DETECTED]')
                    espWebsocket = websocket
                else:
                    print('[USER DETECTED]')
                isFirstMessage = False
            # parse messages
            if (isESP):
                await parseESPMessage(msg)
            else:
                if (msg != DISCONNECT_MSG):
                    print(espWebsocket)
                    if espWebsocket:
                        await parseClientMessage(msg)
                else:
                    connected = False
                    print(f"[CLIENT DISCONNECTED]")
                    

async def start_server():
    print("[STARTING SERVER]")
    start_server = await websockets.serve(handle_client, HOST, PORT)
    print(f"[SERVER RUNNING] Listening at {HOST}:{PORT}")

asyncio.get_event_loop().run_until_complete(start_server())
asyncio.get_event_loop().run_forever()

