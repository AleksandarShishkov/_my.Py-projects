



def num_words(user):                                                                    
                                                                                        


    countWords = 1                                                                      

    for i in range(len(user)):

        if(user[i] == ' '):
            countWords += 1                                                             

        else:
            continue

    
    print('\nString: ', user)                                                           
    print('Number of words: ', countWords)                                              

   
