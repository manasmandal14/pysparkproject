import pytest
from carSimulation.carSimulationsMain import FieldSize
from carSimulation.carSimulationsMain import welcomeMessage, startProgramme
from carSimulation.carSimulationsMain import FieldSize
from carSimulation.Car import Cars
from carSimulation.utils import withInBoundary,registerCar,numberOfMovement,newCoordinate,collisionCheck


def test_welcomeMessage(monkeypatch):
    def mock_userInput(aa: str, num: int):
        if num == 4:
            return [5, 5]
        elif num == 6:
            return 1

    def mock_startProgramme(num: int, fieldSize: FieldSize):
        return "Program Started !"

    monkeypatch.setattr("carSimulation.carSimulationsMain.takeUserInput", mock_userInput)
    monkeypatch.setattr("carSimulation.carSimulationsMain.startProgramme", mock_startProgramme)
    welcomeMessage()


def test_startProgramme(monkeypatch):
    def mock_userInput(aa: str, num: int):
        if num == 2:
            return "testCarName"
        elif num == 6:
            return 2

    def mock_startProgramme(num: int, fieldSize: FieldSize):
        return 2

    def mock_runSimulation(fieldSize: FieldSize):
        return "Run the Simulation !"

    def mock_registerCar(fieldSize: FieldSize, carName: str):
        return ""

    fieldSize = FieldSize(5, 5)
    car1 = Cars("firstcar", [4, 5, "N"])
    car2 = Cars("secondcar", [4, 5, "S"])
    all_cars = {"firstcar": car1, "secondcar": car2}

    monkeypatch.setattr("carSimulation.carSimulationsMain.takeUserInput", mock_userInput)
    monkeypatch.setattr("carSimulation.carSimulationsMain.startProgramme", mock_startProgramme)
    monkeypatch.setattr("carSimulation.carSimulationsMain.runSimulation", mock_runSimulation)
    monkeypatch.setattr("carSimulation.carSimulationsMain.registerCar", mock_registerCar)
    startProgramme(1, fieldSize)


def test_withInBoundary():
    fieldSize = FieldSize(5, 5)
    assert withInBoundary(4, -1, fieldSize) == True
    assert withInBoundary(6, -1, fieldSize) == False
    assert withInBoundary(-1, 6, fieldSize) == False
    assert withInBoundary(-1, 4, fieldSize) == True


def test_registerCar(monkeypatch):
    fieldSize = FieldSize(5, 5)
    car1 = Cars("firstcar", [4, 5, "N"])
    car2 = Cars("secondcar", [4, 5, "S"])
    all_cars = {"firstcar": car1, "secondcar": car2}

    # To Test Car with the same name already present
    registerCar(fieldSize,"firstcar",all_cars)
    # Register a new car in the system

    def mock_userInput(aa: str, num: int):
        if num == 1:
            return [5,5,"N"]
        elif num == 5:
            return "FFFF"

    monkeypatch.setattr("carSimulation.utils.takeUserInput", mock_userInput)
    registerCar(fieldSize, "thirdCar", all_cars)
    # To check if we are able to register the Car, check the command in the car
    assert all_cars["thirdCar"].command =="FFFF"


def test_numberOfMovement():
    car1 = Cars("firstcar", [4, 5, "N"])
    car2 = Cars("secondcar", [4, 5, "S"])
    car1.setCommand("FFFFLR")
    car2.setCommand("FFFFFFFFRRR")
    all_cars = {"firstcar": car1, "secondcar": car2}
    assert numberOfMovement(all_cars) ==11



def test_newCoordinate(monkeypatch):
    car1 = Cars("firstcar", [4, 5, "N"])
    fieldSize = FieldSize(5, 5)

    def mock_withInBoundary(x_axis:int,y_axis:int,fieldSize:FieldSize):
        return True

    monkeypatch.setattr("carSimulation.utils.withInBoundary", mock_withInBoundary)
    newCoordinate(car1,fieldSize)
    assert car1.y_axis == 6


def test_collisionCheck():
    car1 = Cars("firstcar", [4, 5, "N"])
    car2 = Cars("secondcar", [4, 5, "N"])
    all_cars = {"firstcar": car1, "secondcar": car2}
    collisionCheck(2,all_cars)
    assert all_cars["firstcar"].carStatus =="-firstcar collides with secondcar at (4,5) at step 2"







