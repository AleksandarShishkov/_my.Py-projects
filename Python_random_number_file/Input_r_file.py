



def i_file(name_file):                                                              # declaring i_file() function 
                                                                                    # with parameter for the file name

    total = 0                                                                       # an integer to hold the total
    num_read = 0                                                                    # and integer to hold the number read



    n_file = input("\nEnter the name of the file> ")                                # prompting the user to enter the file name

    while(n_file != name_file):                                                     # validating the input
        n_file = input("\nInvalid input. Try again> ")



    print("\nThe numbers are: \n")                                                  
    input_file = open(n_file, 'r')                                                  # opening the file

    try:

        str_num = input_file.readline()                                             # assigning the first line to str_num
        
        while(str_num != ''):

            r_num = int(str_num)                                                    # converting str_num to an integer, assigning
                                                                                    # the valie to r_num

            print(r_num)                                                            # printing the output

            total += r_num                                                          # adding the currnet value to total
            num_read += 1                                                           # adding 1 to num_read

            str_num = input_file.readline()                                         # reading the next line

    except IOError:                                                                 # validating the output
        print("\nError while reading the file\n")
        

    print("\nThe total of the numbers is: ", total)                                 # printing the total
    print("The numbers read are: ", num_read)                                       # printing the number read





