



import random                                                                       


def o_file():

                                                                                    
                                                                                    
    name_file = input("\nEnter the name of the file and " +\
        "make sure it ends with .txt > ")

    
    print("\nThe file name is set to '", name_file, "'")                            
                                                                                    

    output_file = open(name_file, 'w')                                              
    
    
    try:

                                                                                    
                                                                                    
                                                                                    
        num_numbers = int(
            input("\nHow many numbers will be written " + \
                "to the file? > "))

    except ValueError:                                                              
        print("\nInvalid value entered.\n")


    try:

                                                                                    
                                                                                    
        num_limit = int(
            input("\nWhat is the limit (the highest number) > "))

    except ValueError:                                                              
        print("\nInvalid value entered.\n")




    for i in range(1, num_numbers + 1):

        r_num = random.randrange(1, num_limit)                                      

        output_file.write(str(r_num) + '\n')                                        



    print("\nThe numbers`s been written to the file")                               
                                                                                    

    output_file.close()                                                             

    return name_file                                                                




