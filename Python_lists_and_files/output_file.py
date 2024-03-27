



def open_file():

                                                                                    
    file_name = input("\nEnter a file name. Make sure " \
        "it ends with '.txt' extension> ")

    output_file = open(file_name, 'w')                                              

                                                                                    
    print("\nEnter serie of integers between 1 and 10000." \
        "To quit press '-1'> ")

    num = int(input("> "))

    while(num < -1 or num > 10000):                                                 

        print("\nInvalid input. Try again> ", end = ' ')
        num = int(input())


    while(num != -1):                                                               
        output_file.write(str(num) + '\n')                                          

                                                                                    
        print("\nEnter an integers between 1 and 10000." \
        "To quit press '-1'> ")

        num = int(input("> "))

        while(num < -1 or num > 10000):                                             

            print("\nInvalid input. Try again> ", end = ' ')
            num = int(input())


    print("\nThe data`s been written to the file!\n")                               
                                                                                    

    output_file.close()                                                             



    return file_name                                                                

