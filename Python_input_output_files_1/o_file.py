


def file_output():                                                                      # declaration of the file_output() function

    print("\n\tWrite series of names to " + \
        "\n\ta file. To quit entering type '0'\n")


    output = open("Names.txt", 'w')                                                     # creating a .txt file for writing
    name = input("\nEnter a name> ")                                                    # prompting the user to enter a name
    output.write(name + '\n')                                                           # writing the name in the file
    
    while name != '0':                                                                  # validating the input
            
        name = input("\nEnter a name> ")
        
        if(name != '0'):
            output.write(name + '\n')



    output.close()                                                                      # closing the .txt file
                                                                                        # printing confirmation that the data`s on the file
    print("\n\tThe data`s been written to the " + \
        "file!")

    input("\n\tPress <Enter> to continue. . . ")                                        # prompting the user to press enter in order
                                                                                        # to continue

