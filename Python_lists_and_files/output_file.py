



def open_file():

                                                                                    # prompting the user to enter the file name
    file_name = input("\nEnter a file name. Make sure " \
        "it ends with '.txt' extension> ")

    output_file = open(file_name, 'w')                                              # crating the file

                                                                                    # prompting the user to enter an integers
    print("\nEnter serie of integers between 1 and 10000." \
        "To quit press '-1'> ")

    num = int(input("> "))

    while(num < -1 or num > 10000):                                                 # validating the input

        print("\nInvalid input. Try again> ", end = ' ')
        num = int(input())


    while(num != -1):                                                               # entering the sentinel-controlled loop

        output_file.write(str(num) + '\n')                                          # writing the data to the file

                                                                                    # promting the user to enter the next integer
        print("\nEnter an integers between 1 and 10000." \
        "To quit press '-1'> ")

        num = int(input("> "))

        while(num < -1 or num > 10000):                                             # validating the input

            print("\nInvalid input. Try again> ", end = ' ')
            num = int(input())


    print("\nThe data`s been written to the file!\n")                               # printing a message indicating the data`s
                                                                                    # been written to the file

    output_file.close()                                                             # closing the file



    return file_name                                                                # returning the file name

