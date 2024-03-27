


def file_input():                                                                       
    input_file = open("Names.txt", 'r')                                                 

    name = input_file.readline()                                                        

    while (name != ''):                                                                 

        name = name.rstrip('\n')
        print(name)
        name = input_file.readline()


    input_file.close()                                                                  


