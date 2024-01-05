# client.py
import asyncio
import websockets

async def connect():
    uri = "ws://localhost:8010/ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello World!")
        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(connect())