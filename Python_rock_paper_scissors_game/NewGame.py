




def new_game():                                                                     # defining the new_game() function

    choice = input('\nNew Game? (y/n)> \n')                                         # prompting the user for an imput

    while(choice != 'y'and choice != 'n'):                                          # validating the input
        choice = input('\nInvalid input. Try again (y/n)> ')

    if(choice == 'y'):                                                              # returning True or False depending on the validation
        return True
    else:
        return False


