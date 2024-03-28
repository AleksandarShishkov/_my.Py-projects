




def new_game():                                                                     

    choice = input('\nNew Game? (y/n)> \n')                                         

    while(choice != 'y'and choice != 'n'):                                          
        choice = input('\nInvalid input. Try again (y/n)> ')

    if(choice == 'y'):                                                              
        return True
    else:
        return False


