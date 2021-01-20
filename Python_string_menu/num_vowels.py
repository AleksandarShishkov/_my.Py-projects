



def vowels(user):                                                                       # defining vowels method with parameter for
                                                                                        # the string

    numVowels = 0                                                                       # an integer to keep count of the number of vowels located
    vowel_list = []                                                                     # a list to hold the vowels
    vowel_located = False                                                               # a boolean to flag whether a vowel was located


    for i in range(len(user)):

        if(user[i].lower() == 'a' or user[i].lower() == 'e' or 
           user[i].lower() == 'i' or user[i].lower() == 'u' or 
           user[i].lower() == 'o'):

            numVowels += 1                                                              # addin 1 to numVowels if a vowel is located
            vowel_list += list(user[i])                                                 # adding the vowel to the list
            vowel_located = True                                                        # assigning true to vowel_located





    if(vowel_located):

        print('\nString: ', user)                                                       # printing the string
        print('Number of vowels: ', numVowels)                                          # printing the number of vowels
        print('Letters: ', end = '')                                                    # printing the vowels
   
        for i in vowel_list:

            print(i, end = ' ')

        print('\n')


    else:

        print('\nNo vowels were located!')                                              # printing a message indicating that no vowels
                                                                                        # were located if none in the string


