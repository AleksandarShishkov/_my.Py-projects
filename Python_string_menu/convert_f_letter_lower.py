



def convert_lower(user):                                                                # defining convert_lower method with parameter for
                                                                                        # the string



    print('\nString: ', user)                                                           # printing the string
    print('Lower-case: ', end = '')                                                     # printing the string with the converted letters

    for i in range(len(user)):

        if(i == 0):

            print(user[i].lower(), end = '')

        elif(user[i - 1] == '.' and user[i] != ' '):

            print(user[i].lower(), end = '')

        elif(user[i - 2] == '.' and user[i - 1] == ' '):

            print(user[i].lower(), end = '')

        else:

            print(user[i], end = '')




