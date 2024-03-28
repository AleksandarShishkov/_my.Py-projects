



def consonants(user):                                                                   

    numConsonants = 0                                                                   
    cons_list = []                                                                      
    cons_located = False


    for i in range(len(user)):

        if((ord(user[i]) > 64 and ord(user[i]) < 91) or 
           (ord(user[i]) > 96 and ord(user[i]) < 123) and 
           (user[i].lower() != 'a' and user[i].lower() != 'e'and 
           user[i].lower() != 'i' and user[i].lower() != 'u' and 
           user[i].lower() != 'o')):

            numConsonants += 1                                                          
            cons_list += list(user[i])                                                  
            cons_located = True



    

    if(cons_located):

        print('\nString: ', user)                                                       
        print('Number of consonants: ', numConsonants)                                  
        print('Letters: ', end = '')                                                    
   
        for i in cons_list:

            print(i, end = ' ')

        print('\n')

    else:

        print('\nNo consonats located')                                                 
                                                                                        
