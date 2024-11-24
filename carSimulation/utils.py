from carSimulation.Car import Cars
from carSimulation.userinputfile import takeUserInput

all_cars = {}


# This will register the car in our system and place the car in the field. We have to make sure car is not place outside the boundary:
def registerCar(fieldSize, carName,all_cars:dict):
    if carName in all_cars.keys():
        print("Car with the same name already exists")
    else:
        while True:
            initPosDir = takeUserInput(f"Provide initial position of car {carName} in x y Direction format:\n", 1)
            # Below validation is to check the car is not going to place outside the boundary by considering
            if 0 <= int(initPosDir[0]) <= fieldSize.MAX_X_AXIS and 0 <= int(initPosDir[1]) <= fieldSize.MAX_Y_AXIS:
                break
            else:
                print(
                    f"Please check the x and y coordinate . It should be within the boundary defined")
        car_commands = takeUserInput(f"Please enter the commands for car {carName}\n", 5)
        car = Cars(carName, initPosDir)
        car.setCommand(car_commands)
        all_cars[carName] = car


def simulation(car: Cars, fieldSize):
    """
    First check is there is any command is available for the cat then only execute.
    If command is available in the object then based on the command call the respective functions
    """
    if len(car.commandInDict) > 0:
        # Take the present command available in the car and execute it.
        command = car.commandInDict[next(iter(car.commandInDict))]
        if command == "F":
            # Move the car to new coordinate with additional check if this is within boundary
            newCoordinate(car, fieldSize)
        elif command == "R":
            car.right_turn()

        elif command == "L":
            car.left_turn()
    # After executing the command for the specified car we will remove from it.
    car.commandInDict.pop(next(iter(car.commandInDict)))



# This will provide the new coordinate based on the current facing direction
def newCoordinate(car: Cars, fieldSize):
    """
    This function will move to new coordinate if the object is moving within boundary.
    So if object try to move out of the boundary then we will neglect the command and preserve the existing coordinates
    """
    if car.direction == 'E':
        if withInBoundary((car.x_axis - 1), -1, fieldSize):
            car.move_coordinate()
    elif car.direction == 'W':
        if withInBoundary((car.x_axis + 1), -1, fieldSize):
            car.move_coordinate()
    elif car.direction == 'N':
        if withInBoundary(-1, car.y_axis + 1, fieldSize):
            car.move_coordinate()
    elif car.direction == 'S':
        if withInBoundary(-1, car.y_axis - 1, fieldSize):
            car.move_coordinate()


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


"""
After Every Steps i.e. When all car will execute their given command we will check if there is an collision.
For that every car coordinate will be checked with the others car in the simulation
"""


def collisionCheck(step,all_cars:dict):
    for checkCurrentCar in all_cars.keys():
        for checkOtherCars in all_cars.keys():
            if checkCurrentCar != checkOtherCars:
                if all_cars[checkCurrentCar].x_axis == all_cars[checkOtherCars].x_axis and all_cars[checkCurrentCar].y_axis == all_cars[checkOtherCars].y_axis:
                    all_cars[checkCurrentCar].isCollided = True
                    all_cars[checkCurrentCar].carStatus = (
                        f"-{all_cars[checkCurrentCar].name} collides with {all_cars[checkOtherCars].name} at "
                        f"({all_cars[checkCurrentCar].x_axis},{all_cars[checkOtherCars].y_axis}) at step {step}")


"""This funtions is to find the max number of movements is present in our simulation program. Car with max number of 
movement will be the value. ex : Car 1 has 5 movement , Car 2 has 6 movements then ANSWER=6
"""
def numberOfMovement(all_cars:dict):
    max_num = 0
    for i in all_cars.keys():
        max_num = max(max_num, len(all_cars[i].commandInDict))
    return max_num


def runSimulation(fieldSize):
    """
    We will check what is the max number of commands present in all the cars in the system i.e. numberOfMovement
    Outer loop will run until all the commands is finished in our car system.
    """
    for step in range(1, numberOfMovement(all_cars) + 1):
        """
        This inner loop will run the step 1 commands for all cars followed by step 2 for all cars followed by step3,
        step 4 and so on
        """
        for carObject in all_cars.keys():
            if (all_cars[carObject].isCollided == False) and (len(all_cars[carObject].commandInDict)) > 0:
                simulation(all_cars[carObject], fieldSize)
        """
        After every step we will check which all cars are collided.Then we will store the information in the car object. 
        If Collided then collided car will not move
        """
        collisionCheck(step,all_cars)
    # Final Step to print the cars in the system
    print("Your current list of cars are:")
    for cars in all_cars.keys():
        print(all_cars[cars].initial_status)
    print("After simulation, the result is:")
    for carsfinal in all_cars.keys():
        print(all_cars[carsfinal])
