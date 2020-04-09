class robot:
    """
     Returns a ```Robot``` object with given name and type.

     """

    def __init__(self, name, robot_type):
        self.name = name
        self.type = robot_type

    def get_details(self):
        return "{0} has {1} special ability ".format(self.name, self.robot_type)

    def says(self):
        return " i am an unknow robot "


class irobot(robot):

    def __init__(self, name, robot_type, speed):
        super().__init__(name, robot_type)
        self.speed = speed

    def ir(self):
        print('LED Luminous is Mah')
