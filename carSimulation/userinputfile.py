import string

direction_list = ["E", "W", "N", "S"]
possibleCommandList = ['F', 'R', 'L']


def isPossibleCommand(string, possibleCommandList):
    return all(char in possibleCommandList for char in string)


def inputValidations(checkInput: list, numberOfInputExpected, stringOrNumber):
    if stringOrNumber == 1:
        if len(checkInput) == numberOfInputExpected and all(checkInput):
            try:
                for i in range(0, len(checkInput)):
                    x = int(checkInput[i])
                return True
            except ValueError:
                print(f"This i/p expect only {numberOfInputExpected} values in integer. Please try again ")
                return False
        else:
            print(f"We need to add {numberOfInputExpected} i/p. Please review the i/p and try again")
            return False
    elif stringOrNumber == 2:
        if len(checkInput) == numberOfInputExpected and all(checkInput):
            if isPossibleCommand(checkInput[0], possibleCommandList):
                return True
            else:
                print("Please provide the possible commands as 'F' or 'R' or 'L'")
        else:
            print("Please check the command")


def inputValidationsForCordinate(checkInput: list, numberOfInputExpected):
    if len(checkInput) == numberOfInputExpected and all(checkInput):
        try:
            for i in range(0, len(checkInput) - 1):
                x = int(checkInput[i])
            return True
        except ValueError:
            print(f"Please i/p the x and y  coordinate in integer formate ")
            return False


def takeUserInput(displayMessage, argument):
    match argument:
        case 1:
            while True:
                init_position = input(displayMessage).split()
                if inputValidationsForCordinate(init_position, 3) and init_position[2] in direction_list:
                    break
                else:
                    print("Provide the correct input:Sample 3 4 N")
            return init_position

        case 2:
            name = input(displayMessage).split()
            return name[0]
        case 4:
            while True:
                fields_dimensions = input(displayMessage).split()
                if inputValidations(fields_dimensions, 2, 1):
                    if int(fields_dimensions[0]) > 0 and int(fields_dimensions[1]) > 0:
                        break
                    else:
                        print("Please check the field height and width. It should be greater than 0  ")

            return fields_dimensions

        case 5:

            while True:
                commands_provided = input(displayMessage).split()
                if inputValidations(commands_provided, 1, 2):
                    break
            return commands_provided[0]

        case 6:
            while True:
                userInput = input(displayMessage).split()
                if inputValidations(userInput, 1, 1):
                    if int(userInput[0]) == 1 or int(userInput[0]) == 2:
                        break
                    else:
                        print("Please enter either 1 or 2 ")
            return userInput[0]
