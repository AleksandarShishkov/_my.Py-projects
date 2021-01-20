



def spaces(user):                                                                       # defining spaces method


    numSpaces = 0                                                                       # an integer to keep count of the number of spaces

    for i in range(len(user)):

        if(user[i] == ' '):
            numSpaces += 1                                                              # adding 1 to numSpaces if a space is located


    
    print('\nString: ', user)                                                           # printing the string
    print('White spaces: ', numSpaces)                                                  # printing the number of spaces