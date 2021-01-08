

# A program that prompts the user to enter series of integers
# and displaying their sum trought while loop after a negavie number is provided


def main():                                                    # definition of main()

                                                               # taking an input from the user
    num = int(input("\nEnter and integer." + \
                    " To view the sum enter negative value > "))

    total = 0                                                  # setting the total to '0'

    while (num > 0):                                           # entering the while loop

        total += num                                           # adding num to total

                                                               # taking an input from the user
        num = int(input("\nEnter and integer." + \
                    " To view the sum enter negative value > "))


    print("\nThe total is : ", total, "\n")                    # printing the input


main()                                                         # calling main


