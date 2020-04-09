import asyncio
import websockets
import Robot_driver as airobot


class RobotComm:
    def __init__(self, ip_address, port, robot_name, robot_type, robot_speed):
        self.ip_address = ip_address
        self.port = port
        self.robotname = robot_name
        self.rorobottype = robot_type
        self.robotspeed = robot_speed
        self.work = airobot.irobot(self.robotname,self.rorobottype,self.robotspeed)

    def details_server_param(self):
        print("robot server begin " + self.ip_address, self.port)

    async def Robot_Mgmt_protocol(self, websocket, path):
        async for message in websocket:
            print(f"< {message}")

            greeting = f"Hello {message}!"

            await websocket.send(greeting)
            print(f"> {greeting}")
            """
            parser host ( client request )
            """
            self.robot_status(message)

    def start_robot_comm(self):
        start_server = websockets.serve(self.Robot_Mgmt_protocol, self.ip_address, self.port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    def robot_status(self, robot_msg):
        switcher = {
            'ir': self.work.ir()
        }
