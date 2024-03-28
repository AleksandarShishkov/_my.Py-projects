



def upper_case(user):                                                                    
                                                                                        

    upperCase = 0                                                                       
    upper_case = []                                                                     

    for i in range(len(user)):

        if(user[i].isupper()):

            upperCase += 1                                                              
            upper_case += list(user[i])                                                 




    print('\nString: ', user)                                                           
    print('Number of upper-case letters: ', upperCase)                                  
    print('Letters: ', end = '')                                                        

    for i in upper_case:

        print(i, end =' ')

