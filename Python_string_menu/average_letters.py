



def average(user):                                                                      # defining average method with parameter for the string

    count = 1                                                                           # an integer to keep total of the words

    for i in range(len(user)):

        if(user[i] == ' '):

            count += 1                                                                  # adding 1 to count if an empty space is encountered


    average = len(user) / count                                                         # calculating the average letters


    print('\nString: ', user)                                                           # printing the string
    print('Average letters in a word: ', format(average, '.2f'))                        # printing the formatted average


