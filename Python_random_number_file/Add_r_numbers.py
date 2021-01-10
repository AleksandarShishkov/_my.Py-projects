



import random                                                                       # importing the random module



def a_file(name_file):                                                              # declaring a_file() function 
                                                                                    # with parameter for the file name


                                                                                    # prompting the user to select between two options
    choice = input("\nDo you want to include additional numbers " +\
        "to the file (y/n) > ")

    while(choice != 'y' and choice != 'n'):                                         # validating the input
        choice = input("\nInvalid input. Try again> ")


    if(choice == 'y'):

                                                                                    # printing message indicating which option
                                                                                    # is selected
        print("\nYou have selected to add numbers to " +\
            "the file")

        f_name = input("\nEnter the name of the file> ")                            # prompting the user to enter the file name

        while(f_name != name_file):                                                 # validating the input
            f_name = input("\nInvalid input. Try again> ")

        add_to_file = open(f_name, 'a')                                             # opening the file for re-writing
    

        try:

                                                                                    # prompting the user to enter the number
                                                                                    # of the random numbers that`s going to be
                                                                                    # writen to the file
            num_numbers = int(
                input("\nHow many numbers will be added? > "))

        except ValueError:                                                          # validating the input
            print("\nInvalid value entered.\n")


        try:

                                                                                    # prompting the user to enter the limit
                                                                                    # to which the random numbers will be generated
            num_limit = int(
                input("\nWhat is the limit (the highest number) > "))

        except ValueError:                                                          # validating the input
            print("\nInvalid value entered.\n")

            

        for i in range(1, num_numbers + 1):

            r_num = random.randrange(1, num_limit)                                  # generating random number, assigning it to r_num

            add_to_file.write(str(r_num) + '\n')                                    # writing the number into the file



        print("\nThe data has been added to the file")                              # printing message indicating that the numbers`
                                                                                    # been added to the file

        add_to_file.close()                                                         # closing the file

        return True                                                                 # returning True

    else:

        print("\nNo numbers will be included.")                                     # printing message indicating which 
                                                                                    # option is selected

        return False                                                                # returning False


