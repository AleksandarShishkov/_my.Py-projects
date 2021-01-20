



def user_menu():                                                                        # defining user_menu method


    print('\n\n\tSelect between the following:\n')                                      # printing the menu
    print("'1' for the number of words")
    print("'2' for the average number of letters in word")
    print("'3' for the number of all upper-case letters")
    print("'4' for the number of all lower-case letters")
    print("'5' for converting all the first letters capitals")
    print("'6' for converting all the first letters lower-case")
    print("'7' for the number of white characters")
    print("'8' for the number of digits and their sum")
    print("'9' for the number of consonants")
    print("'10' for the number of vowels")
    print("'11' for new string")
    print("'0' to quit the program")
    choice = int(input("\t> "))                                                         # promting the user to enter the choice

    while(choice < 0 or choice > 11):                                                   # validating the input

        choice = int(input("\n\tInvalid input. Try agian> "))

    return choice                                                                       # returning choice



