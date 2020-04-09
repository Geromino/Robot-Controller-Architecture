import robot_comm as RobotModule


def main():
    print("Hello World!")

    Irobot = RobotModule.RobotComm("localhost", 8765)
    Irobot.start_robot_comm()


if __name__ == "__main__":
    main()
