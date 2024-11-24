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
            # Factory method is used to create the Car class in the system.
            # This will recursively add car in the system unless user will add Run Simulation
            carName = takeUserInput("Please enter the name of the car:\n", 2)
            registerCar(fieldSize, carName,all_cars)
            print("Your current list of cars are:")
            for car in all_cars.keys():
                print(all_cars[car].initial_status)
            userInput = takeUserInput("1.Add a car to a field\n2.Run Simulation\n", 6)

            startProgramme(int(userInput), fieldSize)
        case 2:
            runSimulation(fieldSize)


"""This Function will be called as the first function in our Simulation Program.
Below function will be executed in a recursive way. 
Each and every steps is provided with the functionality it will execute.
"""


def welcomeMessage():
    print("Welcome to Auto Driving Car Simulation !")
    # Take the field size from users as I/P.
    fieldDimension = takeUserInput("Please enter the width and height of the simulation field in x y format\n", 4)
    print(f"You have created a field of {fieldDimension[0]} x {fieldDimension[1]}")
    # We are subtracting 1 as our index will start from 0 so field size of 10 X10 will have max X as 9 and Max Y as 9
    MAX_X_AXIS = int(fieldDimension[0]) - 1
    MAX_Y_AXIS = int(fieldDimension[1]) - 1
    # Create the field size as object as this will be used in another functions.
    fieldSize = FieldSize(MAX_X_AXIS, MAX_Y_AXIS)
    # Below loop will run until user add car to the system . We can not simulate unless car is added in the system.
    while True:
        userInput = takeUserInput("1.Add a car to a field\n2.Run Simulation\n", 6)
        if int(userInput) == 1:
            break
        else:
            print("There is no Car in the System Yet. Please enter option 1")
    # Once the car is added in the system we need to start the simulation program.
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
