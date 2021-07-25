import asyncio
import websockets

HOST = "192.168.2.7"
PORT = 8765
DISCONNECT_MSG="!"

uri = "ws://"+HOST+":"+str(PORT)

async def connect_to_server():
    websocket = await websockets.connect(uri)
    running = True
    while running:
        name = input("Please type your message: ")
        await websocket.send(name)
        if name == "!":
            running=False
    # reponse = await websocket.recv()
        
asyncio.get_event_loop().run_until_complete(connect_to_server())