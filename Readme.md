python version : 3.12

Program Information:
Main logic of car is written in carSimulationsMain.py . Using this file we can simulate our programme.
Car.py : Car member variable and its functionality is written in this file.
userinputfile.py: We have written all the i/p validations in this class.
utils.py: This file contain all the utility which our program is having.
testing.py : This file is having unit testing for the function we have created using pytest.

Car Logic Explanation.

This is a car simulation car programme .


Step1 : Add the height and Width of the Car Field.
We have created a class FieldSize to implement this functionality.
User is supposed to add the Height and Width of the field before simulating the program.
If user enter a field of 10X10 then the maximum movement can do is 9X9.

Step2 : Register the Car in the field.
We have created registerCar function in the utils.py file. 
This Function will check if the car is already registered or not. If not registered it will ask the Initial position and direction for the car

Step3: Once the car will be registered it will ask to add more car or Run Simulations.
If Add more car then it will execute step2 again.

Step4: Run simulation.
In this we will simulate all the car present in our system. It will go step by step.
example : CAR1 [FFFRFF]  CAR2[FFFLFF]
First it will execute first command "F" for CAR1 then "F" for CAR2 . Then it will check if they are collided. If collided then we will stop the 
execution.




