



def convert_capital(user):                                                               
                                                                                        


    print('\nString: ', user)                                                           
    print('Upper-case: ', end = '')                                                     

    for i in range(len(user)):

        if(i == 0):

            print(user[i].upper(), end = '')

        elif(user[i - 1] == '.' and user[i] != ' '):

            print(user[i].upper(), end = '')

        elif(user[i - 2] == '.' and user[i - 1] == ' '):

            print(user[i].upper(), end = '')

        else:

            print(user[i], end = '')
