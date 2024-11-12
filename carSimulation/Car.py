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
        self.carStatus=""
        self.initial_status = ""

    def setCommand(self, command: str):
        self.initial_status = f" -{self.name},({self.x_axis},{self.y_axis} ) {self.direction},{self.command}"
        self.command = command
        commandList = list(self.command)
        for i in range(0, len(commandList)):
            self.commandInDict[i] = commandList[i]

    def __str__(self):
        if self.isCollided:
            return f"{self.carStatus}"
        else:
            return f"-{self.name},({self.x_axis},{self.y_axis}) {self.direction} "

