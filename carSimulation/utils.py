from carSimulation.Car import Cars
from carSimulation.userinputfile import takeUserInput

all_cars = {}


# This will register the car in our system and place the car in the field. We have to make sure car is not place outside the boundary:
def factory(fieldSize):
    name = takeUserInput("Please enter the name of the car:\n", 2)
    if name in all_cars.keys():
        print("Car with the same name already exists")
    else:
        while True:
            initPosDir = takeUserInput(f"Provide initial position of car {name} in x y Direction format:\n", 1)
            # Below validation is to check the car is not going to place outside the boundary by considering
            if ((0 < int(initPosDir[0]) <= fieldSize.MAX_X_AXIS and 0 < int(initPosDir[1]) <= fieldSize.MAX_Y_AXIS)
                    or (int(initPosDir[0]) == 1 and int(initPosDir[1]) == 1)) :
                break
            else:
                print(
                    f"Please check the x and y coordinate . It should be within the boundary defined")
        car_commands = takeUserInput(f"Please enter the commands for car {name}\n", 5)
        car = Cars(name, initPosDir)
        car.setCommand(car_commands)
        all_cars[name] = car


def simulation(car: Cars, fieldSize):
    """
    First check is there is any command is available for the cat then only execute.
    If command is available in the object then based on the command call the respective functions
    """
    if len(car.commandInDict) > 0:
        # Take the command present in the 0th index or the command which we need to execute
        command = car.commandInDict[next(iter(car.commandInDict))]
        if command == "F":
            # Move the car to new coordinate with additional check if this is within boundary
            newCoordinate(car, fieldSize)
        elif command == "R" or command == "L":
            # Find the direction of the car
            newDirection(car, command)
    # After executing the command we will remove from the command list
    car.commandInDict.pop(next(iter(car.commandInDict)))


# This will provide the new direction based on the current direction and command given to change direction
def newDirection(cars: Cars, value):
    if cars.direction == 'N':
        if value == 'R':
            all_cars[cars.name].direction = 'E'
        elif value == 'L':
            all_cars[cars.name].direction = 'W'
    elif cars.direction == 'S':
        if value == 'R':
            all_cars[cars.name].direction = 'W'
        elif value == 'L':
            all_cars[cars.name].direction = 'E'
    elif cars.direction == 'E':
        if value == 'R':
            all_cars[cars.name].direction = 'S'
        elif value == 'L':
            all_cars[cars.name].direction = 'N'
    elif cars.direction == 'W':
        if value == 'R':
            all_cars[cars.name].direction = 'N'
        elif value == 'L':
            all_cars[cars.name].direction = 'S'


# This will provide the new coordinate based on the current facing direction
def newCoordinate(cars: Cars, fieldSize):
    """
    This function will move to new coordinate if the object is moving within boundary.
    So if object try to move out of the boundary then we will neglect the command and preserve the existing coordinates
    """
    if cars.direction == 'E':
        if withInBoundary((cars.x_axis - 1), -1, fieldSize):
            all_cars[cars.name].x_axis = cars.x_axis - 1
    elif cars.direction == 'W':
        if withInBoundary((cars.x_axis + 1), -1, fieldSize):
            all_cars[cars.name].x_axis = cars.x_axis + 1
    elif cars.direction == 'N':
        if withInBoundary(-1, cars.y_axis + 1, fieldSize):
            all_cars[cars.name].y_axis = cars.y_axis + 1
    elif cars.direction == 'S':
        if withInBoundary(-1, cars.y_axis - 1, fieldSize):
            all_cars[cars.name].y_axis = cars.y_axis - 1


"""
This functionality is to check while providing the new coordinate are we crossing the boundary or not.
Based on True to False the calling function will decide the necessary actions 
"""


def withInBoundary(x_axis, y_axis, fieldSize):
    if 0 <= x_axis <= fieldSize.MAX_X_AXIS:
        return True
    elif 0 <= y_axis <= fieldSize.MAX_Y_AXIS:
        return True
    else:
        return False


# This will check after every step in simulation is the cars are colliding
def collisionCheck(i):
    for checkCurrentCar in all_cars.keys():
        for checkOtherCars in all_cars.keys():
            if checkCurrentCar != checkOtherCars:
                if all_cars[checkCurrentCar].x_axis == all_cars[checkOtherCars].x_axis and all_cars[
                    checkCurrentCar].y_axis == all_cars[checkOtherCars].y_axis:
                    all_cars[checkCurrentCar].isCollided = True
                    all_cars[checkCurrentCar].carStatus = (
                        f"-{all_cars[checkCurrentCar].name} collides with {all_cars[checkOtherCars].name} at "
                        f"({all_cars[checkCurrentCar].x_axis},{all_cars[checkOtherCars].y_axis}) at step {i}")


def numberOfMovement():
    max_num = 0
    for i in all_cars.keys():
        max_num = max(max_num, len(all_cars[i].commandInDict))
    return max_num


# This function will run when we press run simulation from the programe.
def runSimulation(fieldSize):
    for step in range(1, numberOfMovement() + 1):
        for carObject in all_cars.keys():
            if (all_cars[carObject].isCollided == False) and (len(all_cars[carObject].commandInDict)) > 0:
                simulation(all_cars[carObject], fieldSize)
        collisionCheck(step)
    print("Your current list of cars are:")
    for cars in all_cars.keys():
        print(all_cars[cars].initial_status)
    print("After simulation, the result is:")
    for carsfinal in all_cars.keys():
        print(all_cars[carsfinal])
