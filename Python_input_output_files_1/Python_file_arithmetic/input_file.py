



def i_file():                                                   # deckaring the i_file() function

    
    print("\n\tThe numbers are: \n")

    input = open("numbers.txt", 'r')                            # opening the file for reading
    numbersStr = input.readline()                               # assigning a line to the
                                                                # numbersStr variable

    while numbersStr != '':                                     # validating the file content
        
        numbers = int(numbersStr)                               # converting numbersStr to an 
                                                                # integer

        print(numbers, end = ' ')                               # printing the numbers
        numbersStr = input.readline()                           # assigning the next line to the
                                                                # numbersStr variable
            
    

    
    input.close()                                               # closing the file



