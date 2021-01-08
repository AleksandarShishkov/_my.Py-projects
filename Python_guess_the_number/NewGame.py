

def new_game():                                                                     # defining new_game() function

    new_game = str(input('\tContinue? (y/n)> '))                                    # prompting the user to input a letter (y/n)

    while(new_game != 'y' and new_game != 'n'):                                     # validating the input

        new_game = input('\nInvalid input. Try agian '\
            '>')


    if(new_game == 'y'):
        print('\n\n\tYou are on the way of earning 100 points. . . \n')
        input('\tPress <Enter> to continue. . . \n')

        return True                                                                 # returning True if the inputted letter is 'y'
    else:
        print('\n\n\tThe game has ended. . . Better luck next time!\n')
        return False                                                                # returning False if the inputted letter is 'n'


