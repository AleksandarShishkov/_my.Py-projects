



def upper_case(user):                                                                   # defining upper_case method with parameter for 
                                                                                        # the string

    upperCase = 0                                                                       # an integer to keep count for the upper-cas eletters
    upper_case = []                                                                     # a list to hold the upper-case letters

    for i in range(len(user)):

        if(user[i].isupper()):

            upperCase += 1                                                              # adding 1 to upperCase if an upper-case letter is located
            upper_case += list(user[i])                                                 # adding the letter to the list




    print('\nString: ', user)                                                           # printing the string
    print('Number of upper-case letters: ', upperCase)                                  # printing the number of upper-case letters
    print('Letters: ', end = '')                                                        # printing the letters

    for i in upper_case:

        print(i, end =' ')




