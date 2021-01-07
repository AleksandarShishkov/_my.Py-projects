



def user_option(choice):                                        # declaring the user_option()
                                                                # function, passing the user`s
                                                                # choice as a parameter

   if(choice == 'w'):                                           # validating the user`s input
       print("\n\tYou have selected to re-write " +\
           "\n\tthe file. Enter the new digits or " +\
           "\n\ttype '-1' to quit entering> ")

       try:                                                     # entering the try block

           output = open("numbers.txt", 'w')                    # opening the file
           num = int(input("\nEnter an integer> "))             # prompting the user to enter
                                                                # an integer
        
           while(num != -1):                                    # validating the input

               if(num != -1):
                   output.write(str(num) + '\n')                # writing the input to the
                                                                # file

               num = int(input("\nEnter an integer> "))


           output.close()                                       # closing the .txt file

       except ValueError:                                       # entering the exception block
           print("\nInvalid value passed!\n")                   # if an exception is detected

       print("\nThe file has been re-written " +\
           "\nsuccessfully\n")

   elif(choice == 'r'):                                         # validating the user`s input
        
       print("\n\tYou have selected to review " +\
           "\n\tthe file. The numbers are: \n")

       input_file = open("numbers.txt", 'r')                    # opening the .txt file for
                                                                # reading

       numbersStr = input_file.readline()                       # assigning the first line to 
                                                                # the numbersStr variable

       while numbersStr != '':                                  # validating the .txt content
        
           numbers = int(numbersStr)                            # converting numbersStr to an
                                                                # integer
           print(numbers, end = ' ')                            # printing the result
           numbersStr = input_file.readline()                   # redeing the next line
            
    

    
       input_file.close()                                       # closing the .txt file
       print('\n')

   
   elif(choice == 'a'):                                         # validating the user`s input
       print("\n\tYou have selected to add data " +\
           "\n\tto the file. Add the new digits or " +\
           "\n\ttype '-1' to quit adding> ")

       try:                                                     # entering the try block

           output = open("numbers.txt", 'a')                    # opening the .txt file with 
                                                                # 'a' mode

           number = int(input("\nAdd an integer> "))            # prompting the user to add
                                                                # an integer
        
           while(number != -1):                                 # validating the input

               if(number != -1):
                   output.write(str(number) + '\n')             # writing the input to the file

               number = int(input("\nEnter an integer> "))      # promting the user to enter
                                                                # another integer

               
           output.close()                                       # closing the .txt file


       except ValueError:                                       # entering the exception block
           print("\nInvalid value passed!\n")                   # if an exception is detected

       print("\nThe new data has been added "+\
           "\nsuccessfully\n")


   elif(choice == "sum"):                                       # valdiating the user`s input
      print("\n\tYou have selected to sum the data. " +\
          "\n\n\tThe result is:", end = ' ')

      input_file = open("numbers.txt", 'r')                     # opening the .txt file for 
                                                                # reading

      numbersStr = input_file.readline()                        # assigning the first line to
                                                                # the numbersStr variable

      total = 0                                                 # an integer to hold the total
                                                                # of the summed integers

      while numbersStr != '':                                   # validating the file`s content
        
          numbers = int(numbersStr)                             # converting numbersStr to an
                                                                # integer
          total += numbers                                      # adding every next number to
                                                                # the total variable
          numbersStr = input_file.readline()                    # reading the next line
      
      print("'", total, "'\n")                                  # printing the output
    
      input_file.close()                                        # closing the file


   elif(choice == "substr"):                                    # validating the user`s input
     print("\n\tYou have selected to substract " +\
         "\n\t the file`s data. " +\
         "\n\tThe result is:", end = ' ')

     input_file = open("numbers.txt", 'r')                      # opening the .txt file for
                                                                # reading

     numbersStr = input_file.readline()                         # reading the first line

     substr = int(numbersStr)                                   # assigning the first line
                                                                # to the subtr variable

     while numbersStr != '':                                    # validating the file`s content
        
         numbers = int(numbersStr)                              # converting numbersStr to
                                                                # an integer
         substr -= numbers                                      # substracting substr by numbers
         numbersStr = input_file.readline()                     # reading the next line
      
     print("'", substr, "'\n")                                  # printing the output
    
     input_file.close()                                         # closing the .txt file
    

   elif(choice == "multiply"):                                  # validating the user`s input
    print("\n\tYou have selected to multiply " +\
        "\n\tthe file`s data. " +\
        "\n\tThe result is:", end = ' ')

    input_file = open("numbers.txt", 'r')                       # opening the .txt file for
                                                                # reding

    numbersStr = input_file.readline()                          # assigning the firts line to 
                                                                # numberStr variable

    mult = int(numbersStr)                                      # assigning the first number
                                                                # to the mult variable

    while numbersStr != '':                                     # validating the file`s content
        
        numbers = int(numbersStr)                               # converting numbersStr to an
                                                                # integer
        mult *= numbers                                         # multiplying mult by numbers
        numbersStr = input_file.readline()                      # reading the next line
      
    print("'", mult, "'\n")                                     # printing the result

    input_file.close()                                          # closing the .txt file


   elif(choice == "divide"):                                    # validating the user`s input
    print("\n\tYou have selected to divide " +\
        "\n\t the file`s data. " +\
        "\n\tThe result is:", end = ' ')

    input_file = open("numbers.txt", 'r')                       # opening the .txt file for
                                                                # reading

    numbersStr = input_file.readline()                          # reading the first line
       
    divide = float(numbersStr)                                  # assigning the furst line to 
                                                                # diuvide variable

    while numbersStr != '':                                     # validating the file`s content
        
        numbers = float(numbersStr)                             # converting numbersStr to a
                                                                # float
        divide /= numbers                                       # dividing divide by numbers
        numbersStr = input_file.readline()                      # reading the next line
      
    print("'", format(divide, '.10f'), "'\n")                    # printing the result

    input_file.close()                                          # closing the .txt file


   elif(choice == "avrg"):                                      # validating the user`s input
    print("\n\tYou have selected to calculate " +\
       "\n\tthe file`s data average. " +\
       "\n\tThe result is:", end = ' ')
    
    input_file = open("numbers.txt", 'r')                       # opening the .txt file for
                                                                # reading

    numbersStr = input_file.readline()                          # reading the first line

    count = 0                                                   # an integer to hold a running
                                                                # total for the file`s contents
    total = 0                                                   # a float to hold the average of
                                                                # the numbers

    while numbersStr != '':                                     # validating the file`s content
        
        numbers = int(numbersStr)                               # converting numbersStr to an
                                                                # integer
        total += numbers                                        # adding numbers to total
        numbersStr = input_file.readline()                      # reading the next line
        count += 1                                              # adding 1 to count
    
    average = float(total / count)                              # calculating the average
    print("'", format(average, '.2f'), "'\n")                   # pringing the formatted
                                                                # output

    input_file.close()                                          # closing the file


   elif(choice == '0'):                                         # validating the user`s input

                                                                # printing a message
    print("\n\tYou have selected to quit " +\
       "\n\tthe program. \n\n")

