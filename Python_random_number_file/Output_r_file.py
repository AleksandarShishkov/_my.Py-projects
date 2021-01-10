



import random                                                                       # importing the random module


def o_file():

                                                                                    # prompting the user to enter a name for
                                                                                    # the file
    name_file = input("\nEnter the name of the file and " +\
        "make sure it ends with .txt > ")

    
    print("\nThe file name is set to '", name_file, "'")                            # printing a message confirming the
                                                                                    # file name wa selected

    output_file = open(name_file, 'w')                                              # opening the file for writing
    
    
    try:

                                                                                    # prompting the user to enter the number
                                                                                    # of the random numbers that`s going to be
                                                                                    # writen to the file
        num_numbers = int(
            input("\nHow many numbers will be written " + \
                "to the file? > "))

    except ValueError:                                                              # validating the input
        print("\nInvalid value entered.\n")


    try:

                                                                                    # prompting the user to enter the limit
                                                                                    # to which the random numbers will be generated
        num_limit = int(
            input("\nWhat is the limit (the highest number) > "))

    except ValueError:                                                              # validating the input
        print("\nInvalid value entered.\n")




    for i in range(1, num_numbers + 1):

        r_num = random.randrange(1, num_limit)                                      # generating random number, assigning it to r_num

        output_file.write(str(r_num) + '\n')                                        # writing the number into the file



    print("\nThe numbers`s been written to the file")                               # printing message indicating that the numbers`
                                                                                    # been writen to the file

    output_file.close()                                                             # closing the file

    return name_file                                                                # returning name_file





