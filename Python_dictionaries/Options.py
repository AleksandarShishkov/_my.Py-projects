



def menu(choice):                                                                                           # defining menu() method with a parameter for
                                                                                                            # the choice




    print("\n\t\tSelect between the following:\n")                                                          # displaying the options
    print("\t'1' to create a contact with name and email")
    print("\t'2' to add a telephone number")
    print("\t'3' to add an address")
    print("\t'4' to change an email")
    print("\t'5' to change a telephone number")
    print("\t'6' to change an address")
    print("\t'7' to delete a contact")
    print("\t'8' to delete all of the contacts")
    print("\t'9' to review the contacts")
    print("\n\t'0' to exit")


    choice = int(input("> "))                                                                               # promting the user to enter the input

    while(choice < 0 or choice > 9):                                                                        # validating the input

        print("\nInvalid input.")
        choice = int(intput("Try again> "))



    return choice                                                                                           # returning the input



