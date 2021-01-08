


def main():                                                                                 # main function

    number = int(input("\nEnter an integer 1 trough 10 to convert to roman number > "))

    to_Roman(number)



def to_Roman(number):                                                                       # to_Roman function to check the data and print the result
                                                                                            # with conditional operator
    if number == 1:
        print("\nThe roman for ", number, " is 'I'\n")
    elif number == 2:
        print("\nThe roman for ", number, " is 'II'\n")
    elif number == 3:
        print("\nThe roman for ", number, " is 'III'\n")
    elif number == 4:
        print("\nThe roman for ", number, " is 'IV'\n")
    elif number == 5:
        print("\nThe roman for ", number, " is 'V'\n")
    elif number == 6:
        print("\nThe roman for ", number, " is 'VI'\n")
    elif number == 7:
        print("\nThe roman for ", number, " is 'VII'\n")
    elif number == 8:
        print("\nThe roman for ", number, " is 'VIII'\n")
    elif number == 9:
        print("\nThe roman for ", number, " is 'IX'\n")
    elif number == 10:
        print("\nThe roman for ", number, " is 'X'\n")
    elif number < 1 or number > 10:
        print("\nInvalid input.\n")



main()                                                                                      # calling the main function







