from carSimulation.utils import *
from carSimulation.Car import Cars
from carSimulation.carSimulationsPrograme import FieldSize

import pytest

name = "A"
mylist = [2, 4, 'N']
car = Cars(name, mylist)
MAX_WIDTH = 10
MAX_HEIGHT = 10
fieldSize = FieldSize(MAX_WIDTH, MAX_HEIGHT)


def test_newDirection(monkeypatch):
    all_cars = {"A": car}
    monkeypatch.setattr("carSimulation.utils.all_cars", all_cars)
    newDirection(car, 'R')
    assert all_cars["A"].direction == 'E'


def test_withInBoundary():
    # Check for x_axis crossing the boundary
    assert withInBoundary(11, -1, fieldSize) == False
    assert withInBoundary(10, -1, fieldSize) == True

def test_newCoordinate(monkeypatch):
    car1 = Cars(name, mylist)
    all_cars = {"A": car1}
    monkeypatch.setattr("carSimulation.utils.all_cars", all_cars)
    # Check if the car direction is pointing towards N then new coordinate should increase the Y AXIS to one poistion by keeping the direction same
    newCoordinate(car1,fieldSize)
    assert all_cars["A"].y_axis ==5
    assert all_cars["A"].direction =='N'

def test_factory(monkeypatch):
    all_cars = {"A": car}
    def mock_fetch_data(aa:str,num:int):
        return "A"

    monkeypatch.setattr("carSimulation.utils.all_cars", all_cars)
    monkeypatch.setattr("carSimulation.utils.takeUserInput", mock_fetch_data)
    factory(fieldSize)




