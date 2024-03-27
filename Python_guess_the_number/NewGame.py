

def new_game():                                                                     

    new_game = str(input('\tContinue? (y/n)> '))                                    

    while(new_game != 'y' and new_game != 'n'):                                     

        new_game = input('\nInvalid input. Try agian '\
            '>')


    if(new_game == 'y'):
        print('\n\n\tYou are on the way of earning 100 points. . . \n')
        input('\tPress <Enter> to continue. . . \n')

        return True                                                                 
    else:
        print('\n\n\tThe game has ended. . . Better luck next time!\n')
        return False                                                                


