



def convert_capital(user):                                                              # defining convert_capital method with a parameter 
                                                                                        # for the string


    print('\nString: ', user)                                                           # printing the string
    print('Upper-case: ', end = '')                                                     # printing the string with the converted letters

    for i in range(len(user)):

        if(i == 0):

            print(user[i].upper(), end = '')

        elif(user[i - 1] == '.' and user[i] != ' '):

            print(user[i].upper(), end = '')

        elif(user[i - 2] == '.' and user[i - 1] == ' '):

            print(user[i].upper(), end = '')

        else:

            print(user[i], end = '')


        

    
    
