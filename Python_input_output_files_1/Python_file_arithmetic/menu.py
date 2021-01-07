



def menu_file():                                                # decalring the menu_file()
                                                                # function


                                                                # printing the options
    print("\n\n\tSelect between the following: " + \
        "\n'w' to re-write the file" +\
        "\n'r' to reviwe the file" +\
        "\n'a' to add data to the file" +\
        "\n'sum' to sum all of the items" +\
        "\n'substr' to substract all of the items" +\
        "\n'multiply' to multiply all of the items" +\
        "\n'divide' to devide the sum of the items" +\
        "\n'avrg' to calculate the average of the items" +\
        "\n'0' to exit the program")

    choice = input("> ")                                        # prompting the user to enter 
                                                                # the choice

                                                                # validating the input
    while(choice != 'w' and choice != 'r'
          and choice != 'a' and choice != "sum"
          and choice != "substr" and choice != "multiply"
          and choice != "divide" and choice != "avrg"
          and choice != '0'):
        
        choice = input("Invalid input. Try again> ")


    return choice                                               # returning choice
