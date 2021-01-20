



def menu():                                             # definition of menu method


    print('\n\n\tSelect between the following:\n')
    print("'1' for string conversion to integers")
    print("'2' for integer conversion to string")
    print("'0' to quit the program")
    choice = int(input('> '))                           # prompting the user to select the choice

    while(choice < 0 or choice > 2):                    # validating the input

        choice = int(input('Try again> '))


    return choice                                       # returning the choice



