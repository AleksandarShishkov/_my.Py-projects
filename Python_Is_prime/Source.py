



        # A Python program that prompts the user
        # for an integer and calculates whether
        # the inputted number is prime or not.
        #
        # The user can also select a range 
        # trough which the numbers will be validated
        # as prime or not




import Menu                                                                                         # importing the Menu module
import Is_prime                                                                                     # importing the Is_prime module




def main():


    choice = Menu.menu()                                                                            # an integer to hold the selected option

    while(choice != 0):                                                                             # validating the option

        if(choice == 1):                                                            

            num = int(input("\nEnter an integer> "))                                                # promting the user to enter an integer
            Is_prime.prime(num)                                                                     # calling the prime() method

        elif(choice == 2):

            print("\nEnter the range:")                                                             # promting the user to enter the starting and the ending
            start = int(input("Start> "))                                                           # numbers for the range
            end = int(input("End> "))

            for i in range(start, end + 1, 1):

                Is_prime.prime(i)                                                                   # calling the prime() method


        choice = Menu.menu()                                                                        # promting the user to select an option


    print("\nThe program has ended\n")                                                              # printing a message indicating the end of the program if
                                                                                                    # opriont '0' is selected






main()                                                                                              # calling main() function



