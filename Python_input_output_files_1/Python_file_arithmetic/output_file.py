



def o_file():                                                   # declaring the o_file() function

    
    
    print("\n\tEnter series of integers in a file. " + \
        "\n\tTo quit entering type '-1'\n")

        
    try:                                                       # entering the try block

        output = open("numbers.txt", 'w')                      # creating a .txt file

        number = int(input("\nEnter an integer> "))            # prompting the user to enter
                                                               # an integer        
        while(number != -1):                                   # validating the input

            if(number != -1):
                output.write(str(number) + '\n')               # writting the input to the file

            number = int(input("\nEnter an integer> "))        


        output.close()                                         # closing the file

    except ValueError:                                         # entering the exception block
        print("\nInvalid value passed!\n")                     # if an exception is detected


    print("\n\tThe datas`s been written to the file")
    input("\nTo continue press <Enter> . . .")                 # prompting the user to press
                                                               # <Enter> in order to continue










