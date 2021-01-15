

                                                                                    

def read_file(file_name):

    
    list_numbers = []                                                               # an empty list of integers
    
    
    print("\nEnter the name of the file> ", end = ' ')                              # prompting the user to enter the file name
    name_file = input()

    while(name_file != file_name):                                                  # validating the input

        print("\nInvalid file name. Try again> ", end = ' ')
        name_file = input()

    input_file = open(name_file, 'r')                                               # opening the file

    list_numbers = input_file.readlines()                                           # reading the data into the list

    
    print("\nThe items are on the list!\n")                                         # printing a message indicating that the
                                                                                    # data`s been read successfully

    input_file.close()                                                              # closing the file

    for index in range(len(list_numbers)):                                          

        list_numbers[index] = int(list_numbers[index])                              # converting the list`s data into integers


    i = 1

    print("\nThe list is: \n")

    for index in list_numbers:                                                      # printing the list on the screen

        print([index], end = ' ')

        if(i%5 == 0):

            print('\n')

        i += 1

    print('\n')

    return list_numbers                                                             # returning the list




