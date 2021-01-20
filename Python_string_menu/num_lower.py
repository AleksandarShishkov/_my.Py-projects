



def lower_case(user):                                                                   # defining ower_case method with parameter for the string


    lowerCase = 0                                                                       # an integer to keep count of the lower-case letters
    lower_case = []                                                                     # a list to hold the lower-case letters

    for i in range(len(user)):

        if(user[i].islower()):

            lowerCase += 1                                                              # adding 1 to lowerCase if a lower-case letter is located
            lower_case += list(user[i])                                                 # adding the letter to the lower_case list




    print('\nString: ', user)                                                           # printing the stirng
    print('Number of lower-case letters: ', lowerCase)                                  # printing the number of lower-case letters
    print('Letters: ', end = '')                                                        # printing the letters

    for i in lower_case:

        print(i, end = ' ')




