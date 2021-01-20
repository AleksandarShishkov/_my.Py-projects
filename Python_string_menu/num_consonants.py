



def consonants(user):                                                                   # defining consonats method

    numConsonants = 0                                                                   # an integer to keep count of the consonants lcoated
    cons_list = []                                                                      # a list to hold the consonants
    cons_located = False


    for i in range(len(user)):

        if((ord(user[i]) > 64 and ord(user[i]) < 91) or 
           (ord(user[i]) > 96 and ord(user[i]) < 123) and 
           (user[i].lower() != 'a' and user[i].lower() != 'e'and 
           user[i].lower() != 'i' and user[i].lower() != 'u' and 
           user[i].lower() != 'o')):

            numConsonants += 1                                                          # adding 1 to numConsonants
            cons_list += list(user[i])                                                  # adding the consonant in the list
            cons_located = True



    

    if(cons_located):

        print('\nString: ', user)                                                       # printing the string
        print('Number of consonants: ', numConsonants)                                  # printing the number of consonants
        print('Letters: ', end = '')                                                    # printing the letters
   
        for i in cons_list:

            print(i, end = ' ')

        print('\n')

    else:

        print('\nNo consonats located')                                                 # printing message indicating that no consonats were
                                                                                        # located if none in the string






