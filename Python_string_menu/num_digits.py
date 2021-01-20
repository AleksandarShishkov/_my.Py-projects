



def digits(user):                                                                       # defining digits method with parameter for the string


    numInt = 0                                                                          # an integer to keep total of the integers located
    total = 0                                                                           # an integer to keep the total
    num_digits = []                                                                     # a list to hold the integers
    digits = False                                                                      # a boolean to flag whether an intger is located



    for i in range(len(user)):

        if(ord(user[i]) > 47 and ord(user[i]) < 58):                                    
                
            numInt += 1                                                                 # adding 1 to numInt if an integer is located
            total += int(user[i])                                                       # converting the number to integer and adding it to total
            num_digits += list(user[i])                                                 # adding the number to the num_digits list
            digits = True                                                               # assigning True to digits



    if(digits):                                                                         # valdiating digits

        print('\nString: ', user)                                                       # printing the string
        print("Number of integers: ", numInt)                                           # printing the number of integers
        print('Integers:            ', end = '')                                        # printing the numbers

        for i in num_digits:

            print(i, end = ' ')


        print("\nTotal:              ", total)                                          # printing the total 


    else:

        print("\nNo integers located")                                                  # printing a message indicating that no integers
                                                                                        # were located if none in the string








