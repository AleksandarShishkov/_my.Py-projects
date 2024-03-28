



def menu():                                                                     


    print('\n\n\tSelect between the following:\n')
    print("'1' for string conversion to integers")
    print("'2' for integer conversion to string")
    print("'0' to quit the program")
    choice = int(input('> '))                                                   

    while(choice < 0 or choice > 2):                                            

        choice = int(input('Try again> '))


    return choice                                                               
