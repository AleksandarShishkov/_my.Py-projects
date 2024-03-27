

                                                                                    

def read_file(file_name):

    
    list_numbers = []                                                               
    
    
    print("\nEnter the name of the file> ", end = ' ')                             
    name_file = input()

    while(name_file != file_name):                                                 

        print("\nInvalid file name. Try again> ", end = ' ')
        name_file = input()

    input_file = open(name_file, 'r')                                              

    list_numbers = input_file.readlines()                                          

    
    print("\nThe items are on the list!\n")                                        
                                                                                   

    input_file.close()                                                             

    for index in range(len(list_numbers)):                                          

        list_numbers[index] = int(list_numbers[index])                             


    i = 1

    print("\nThe list is: \n")

    for index in list_numbers:                                                     

        print([index], end = ' ')

        if(i%5 == 0):

            print('\n')

        i += 1

    print('\n')

    return list_numbers                                                            




