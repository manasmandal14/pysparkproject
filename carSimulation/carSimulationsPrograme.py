from carSimulation.utils import *

# Created the boundary for our car simulation
class FieldSize:
    def __init__(self, MAX_WIDTH, MAX_HEIGHT):
        self.MAX_X_AXIS = MAX_WIDTH
        self.MAX_Y_AXIS = MAX_HEIGHT


# This function will simulate the program.
def startProgramme(argument, fieldSize: FieldSize):
    match argument:
        case 1:
            factory(fieldSize)
            print("Your current list of cars are:")
            for car in all_cars.keys():
                print(all_cars[car].initial_status)
            userInput = takeUserInput("1.Add a car to a field\n2.Run Simulation\n", 6)
            startProgramme(int(userInput), fieldSize)
        case 2:
            runSimulation(fieldSize)


"""
Below function will be executed in a recursive way. 
This will have a function FieldSize which will set the height and width of the field

"""


def welcomeMessage():
    print("Welcome to Auto Driving Car Simulation !")
    fieldDimension = takeUserInput("Please enter the width and height of the simulation field in x y format\n", 4)
    print(f"You have created a field of {fieldDimension[0]} x {fieldDimension[1]}")
    MAX_X_AXIS = int(fieldDimension[0]) - 1
    MAX_Y_AXIS = int(fieldDimension[1]) - 1
    fieldSize = FieldSize(MAX_X_AXIS, MAX_Y_AXIS)
    while True:
        userInput = takeUserInput("1.Add a car to a field\n2.Run Simulation\n", 6)
        if int(userInput) == 1:
            break
        else:
            print("There is no Car in the System Yet. Please enter option 1")

    startProgramme(int(userInput), fieldSize)


if __name__ == '__main__':
    while True:
        welcomeMessage()
        all_cars.clear()
        print("Please choose from the following options:")
        userInput1 = takeUserInput("1.Start over\n2.Exit\n", 6)
        if int(userInput1) == 2:
            print("Thank you for running the simulation. Goodbye!")
            break
