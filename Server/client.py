import websockets
import asyncio
from asyncio.tasks import sleep
import json


async def wsrun(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            # Starts receive things, not only once
            await websocket.send(json.dumps({"action": "get_frame"}))
            print(await websocket.recv())
            await sleep(0.5)

asyncio.get_event_loop().run_until_complete(wsrun('ws://localhost:6789'))
