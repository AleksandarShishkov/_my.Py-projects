



def options():                                                      # options() method
                                                                    # printing the options
    print('\n\tSelect between the following:\n')
    print('\t1 - for new profile')
    print('\t2 - to review the profile')
    print('\t0 - to quit')

    choice = int(input('\n\t> '))                                   # promting the user to select an option

    return choice                                                   # returning the choice
