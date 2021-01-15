



def menu_option():                                                  
    

    print("\n\tSelect between the following: \n")                               # printing the options in the menu                                            
    print("\t'1' to search an element on the list")
    print("\t'2' to sum the elements on the list")
    print("\t'3' to find the product of the elements on the list")
    print("\t'4' to find the average of the elements on the list")
    print("\t'5' to create a new list")
    print("\t'6' to review the list")
    print("\t'0' to quit")


    select = int(input("> "))                                                   # prompting the user to select an option

    while(select < 0 or select > 6):                                            # validaing the input
        print("\nInvalid input. Try again> ", end = ' ')
        select = int(input("> "))

    return select                                                               # returning the input


