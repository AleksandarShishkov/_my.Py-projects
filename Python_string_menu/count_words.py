



def num_words(user):                                                                    # defining num_words method with parameter for
                                                                                        # the string


    countWords = 1                                                                      # an integer to keep count for the words

    for i in range(len(user)):

        if(user[i] == ' '):
            countWords += 1                                                             # adding 1 to countWords if space is encountered

        else:
            continue

    
    print('\nString: ', user)                                                           # printing the string
    print('Number of words: ', countWords)                                              # printing the number of words

   



