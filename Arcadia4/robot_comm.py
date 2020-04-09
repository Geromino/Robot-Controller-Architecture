import asyncio
import websockets


async def robot_management_protocol(websocket, path):
    async for message in websocket:
        print(f"< {message}")

        greeting = f"Hello {message}!"

        await websocket.send(greeting)
        print(f"> {greeting}")


class RobotComm:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

    def details_server_param(self):
        print("robot server begin " + self.ip_address, self.port)

    def  start_robot_comm(self):
        start_server = websockets.serve(robot_management_protocol, self.ip_address, self.port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()