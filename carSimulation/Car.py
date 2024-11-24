class Cars:
    def __init__(self, name: str, mylist: list):
        self.x_axis = int(mylist[0])
        self.y_axis = int(mylist[1])
        self.direction = mylist[2]
        self.movement = {}
        self.isCollided = False
        self.name = name
        self.command = ""
        self.commandInDict = {}
        self.carStatus = ""
        self.initial_status = ""

    def setCommand(self, command: str):
        self.initial_status = f" -{self.name},({self.x_axis},{self.y_axis} ) {self.direction},{self.command}"
        self.command = command
        commandList = list(self.command)
        for i in range(0, len(commandList)):
            self.commandInDict[i] = commandList[i]

    def left_turn(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def right_turn(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def move_coordinate(self):

        if self.direction == 'E':
            self.x_axis -= 1
        elif self.direction == 'W':
            self.x_axis += 1
        elif self.direction == 'N':
            self.y_axis += 1
        elif self.direction == 'S':
            self.y_axis -= 1



    def __str__(self):
        if self.isCollided:
            return f"{self.carStatus}"
        else:
            return f"-{self.name},({self.x_axis},{self.y_axis}) {self.direction} "
