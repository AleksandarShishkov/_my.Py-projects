
# A program that makes some basic arithmetics calculations using a for loop
# and an inputted value from the user. The program will display the amount of
# dollars collected for 'n' amount of days as on the first day the user has 1 penny
# which doubles every following day


def main():                                                 # main function definition

    days = int(input("\nEnter the number of the days >"))   # an int to hold the number of the days

    calcAmount(days)                                        # calling calcAmount() function


def calcAmount(days):                                       # calcAmount() definition

    total = 1;                                              # setting the total to 1

    for x in range(1, days + 1):                            # setting the for loop

        total *= x                                          # calculating the total in the loop`s body



    total /= 100                                            # deviding the total by 100 to get the 
                                                            # amount in dollars


                                                            # printing the result
    print("\nThe total amount earned for ", days, \
          " days is $", format(total, ',.2f'), sep='')



main()                                                      # calling main()


