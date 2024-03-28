



def spaces(user):                                                                       


    numSpaces = 0                                                                       

    for i in range(len(user)):

        if(user[i] == ' '):
            numSpaces += 1                                                              


    
    print('\nString: ', user)                                                           
    print('White spaces: ', numSpaces)                                                  
