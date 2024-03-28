



def vowels(user):                                                                       
                                                                                        

    numVowels = 0                                                                       
    vowel_list = []                                                                     
    vowel_located = False                                                               


    for i in range(len(user)):

        if(user[i].lower() == 'a' or user[i].lower() == 'e' or 
           user[i].lower() == 'i' or user[i].lower() == 'u' or 
           user[i].lower() == 'o'):

            numVowels += 1                                                              
            vowel_list += list(user[i])                                                 
            vowel_located = True                                                        




    if(vowel_located):

        print('\nString: ', user)                                                       
        print('Number of vowels: ', numVowels)                                          
        print('Letters: ', end = '')                                                    
   
        for i in vowel_list:

            print(i, end = ' ')

        print('\n')


    else:

        print('\nNo vowels were located!')                                              
                                                                                        
