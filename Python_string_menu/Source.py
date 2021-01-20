



        # A Python program that prompts
        # the user to enter a string and to
        # select an action from a menu.
        #
        # It then dispalys a formatted output.
        # The user can input new string or also
        # to quit the program by selecting '0'.






import count_words                                                                      # importing count_words module
import average_letters                                                                  # importing average_letters module
import num_upper                                                                        # importing num_upper module
import num_lower                                                                        # importing num_lowe module
import convert_f_letter_capital                                                         # importing convert_f_letter_capital module
import convert_f_letter_lower                                                           # importing convert_f_letter_lower module
import num_spaces                                                                       # importing num_spaces module
import num_digits                                                                       # importing num_digits module
import num_consonants                                                                   # importing num_consonants module
import menu                                                                             # importing menu module
import num_vowels                                                                       # imporintg num_vowels module





def main():

    user_choice = 1                                                                     # an integer to hold the users choice
    
    user = input('\nEnter a sting> ')                                                   # prompting the user to input a string



    while(user_choice != 0):                                                            # sentinel-controlled loop

        user_choice = menu.user_menu()                                                  # showing the menu

        if(user_choice == 1):                                                           # validating the choice

            count_words.num_words(user)                                                 # calling num_words methond

        elif(user_choice == 2):

            average_letters.average(user)                                               # calling average method

        elif(user_choice == 3):

            num_upper.upper_case(user)                                                  # calling upper_case method

        elif(user_choice == 4):

            num_lower.lower_case(user)                                                  # calling lower_case method

        elif(user_choice == 5):

            convert_f_letter_capital.convert_capital(user)                              # calling convert_capital method

        elif(user_choice == 6):

            convert_f_letter_lower.convert_lower(user)                                  # calling convert_lower method

        elif(user_choice == 7):

            num_spaces.spaces(user)                                                     # calling spaces method

        elif(user_choice == 8):

            num_digits.digits(user)                                                     # calling digits method

        elif(user_choice == 9):

            num_consonants.consonants(user)                                             # calling consonants method

        elif(user_choice == 10):

            num_vowels.vowels(user)                                                     # calling vowels method

        elif(user_choice == 11):

            user = input('\nEnter the new string> ')                                    # prompting the user to enter the new string

        else:

            print('\nThe program has ended!\n')                                         # printing a message indicating that the program
                                                                                        # has ended








main()                                                                                  # calling main





