


def re_enter():                                                                         # declaration of the re_enter() function

    output_file = open("Names.txt", 'a')                                                # oppening the .txt file for writing and addition
                                                                                        # prompting the user to enter a name
    name = input("\nEnter a name. Type '0' to quit " + \
        "entering> ")

    while(name != '0'):                                                                 # validating the input

        output_file.write(name + '\n')                                                  # writing the name in the file
        name = input("\nEnter a name. Type '0' to quit " +\
                     "entering> ")

        if(name != '0'):
            output_file.write(name + '\n')


    output_file.close()                                                                 # closing the .txt file
                                                                                        # printing confirmation that the data`s on the file
    print("\n\tThe data`s been added to the " + \
        "file!")

    input("\n\tPress <Enter> to continue. . . ")                                        # prompting the user to press enter in order
                                                                                        # to continue



