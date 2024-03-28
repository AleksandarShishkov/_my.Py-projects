



def lower_case(user):                                                                   


    lowerCase = 0                                                                       
    lower_case = []                                                                     

    for i in range(len(user)):

        if(user[i].islower()):

            lowerCase += 1                                                              
            lower_case += list(user[i])                                                 




    print('\nString: ', user)
    print('Number of lower-case letters: ', lowerCase)                                  
    print('Letters: ', end = '')                                                        

    for i in lower_case:

        print(i, end = ' ')
