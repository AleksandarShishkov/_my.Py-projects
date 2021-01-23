



def menu():                                                                                         # defining the menu() method


    print("\n\tSelect between the follwiong:\n")                                                    # printing the options
    print("'1' to input a number")
    print("'2' to input range of numbers")
    print("'0' to quit")

    try:                                                                                            # validating the input with try - except blocks

        choice = int(input("\n> "))                                                                 # promting the user to input the selected option

        while(choice < 0 or choice > 2):                                                            # validating the input

            print("\nInvalid input")
            choice = int(input("Try again> "))


        return choice                                                                               # returning choice


    except ValueError:

        print("\nInvalid input.")                                                                   
        choice = int(input("Try again> "))                                                          # promting the user to select again if
                                                                                                    # an exception is caught



