


def file_input():                                                                       # declaring the file_input() function

    input_file = open("Names.txt", 'r')                                                 # opening the .txt file for reading

    name = input_file.readline()                                                        # reading a line to the variable name

    while (name != ''):                                                                 # validating the lines read

        name = name.rstrip('\n')
        print(name)
        name = input_file.readline()


    input_file.close()                                                                  # closing the .txt file



