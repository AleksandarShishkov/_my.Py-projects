



def average(user):                                                                      

    count = 1                                                                           

    for i in range(len(user)):

        if(user[i] == ' '):

            count += 1                                                                  


    average = len(user) / count                                                         


    print('\nString: ', user)                                                           
    print('Average letters in a word: ', format(average, '.2f'))                        


