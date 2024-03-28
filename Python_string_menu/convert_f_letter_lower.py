



def convert_lower(user):                                                                
                                                                                        



    print('\nString: ', user)                                                           
    print('Lower-case: ', end = '')                                                     
    for i in range(len(user)):

        if(i == 0):

            print(user[i].lower(), end = '')

        elif(user[i - 1] == '.' and user[i] != ' '):

            print(user[i].lower(), end = '')

        elif(user[i - 2] == '.' and user[i - 1] == ' '):

            print(user[i].lower(), end = '')

        else:

            print(user[i], end = '')




