import robot_comm as RobotModule


def main():
    print("Hello World!")

    Irobot = RobotModule.RobotComm("localhost", 8765,"will smit","irobot",500)
    Irobot.start_robot_comm()


if __name__ == "__main__":
    main()
