import robot_comm as RobotModule


def main():
    print("Welcome robot world ")

    Irobot = RobotModule.RobotComm("localhost", 8765,"will smit","irobot",500)
    Irobot.details_server_param()
    Irobot.start_robot_comm()


if __name__ == "__main__":
    main()
