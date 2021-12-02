import asyncio
import json
import logging
import websockets
from traffic_simulator import *

logging.basicConfig()

USERS = set()

size = (20, 20)
city = City(*size)
city.add_street((4, 0), (4, size[0]), Direction.RIGHT)
city.add_street((0, 4), (size[0], 4), Direction.UP)

# Define parameters
parameters = {
    "size": size,
    "city": city,
    "cars": 35,
    "spawn_points": [(4, 0), (0, 4)],
}


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def counter(websocket):
    global USERS, VALUE
    try:
        # Register user
        USERS.add(websocket)
        city_model = CityModel(parameters)
        city_model.sim_setup()
        # Send current state to user
        await websocket.send(city_model.get_frame())
        # Manage state changes
        print("helll")
        async for message in websocket:
            print(message)
            event = json.loads(message)
            print(event)
            if event["action"] == "get_frame":
                websockets.broadcast(USERS, city_model.get_frame())
            else:
                logging.error("unsupported event: %s", event)
    finally:
        # Unregister user
        USERS.remove(websocket)
        city_model.end()
        websockets.broadcast(USERS, users_event())


async def main():
    async with websockets.serve(counter, "localhost", 6789):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
