# Requirements:
# Text User Interface
# Read Evaluate Print Loop
# Add Tasks
# Delete Tasks when complete
# list current tasks in the order they were added
# Persist across runs (load in multiple terminals) 
# every user gets their own list
# editable storage format
# all tasks will be entered by the user
# report # of tasks 


from os import system

def elicitInt(_min, _max):
    valid = False

    while not valid:
        _in = input(f"Enter a valid integer between {_min} and {_max} (inclusive of both): ")

        try:
            _in = int(_in)
        
            if _min <= _in <= _max:
                valid = True
            else:
                print("Integer out of bounds")
        
        except ValueError:
            print("Invalid int provided.")

    return _in



def printMenu(): 
    print("1) Add 2) List 3) Delete 4) Count Tasks 5) Quit ")



def acceptMenuInput():
    return elicitInt(1, 5)


def handleInput(userInput):
    print(userInput)
    return True

def main():
    _quit = False

    system("clear")

    while not _quit:
        printMenu()
       

        userInput = acceptMenuInput()

        system("clear")

        _quit = handleInput(userInput)

    print("Bye")


if __name__ == "__main__":
    main()
