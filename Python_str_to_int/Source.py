



        # A Python program which prompts
        # the user to select between
        # three option from a menu
        # and convert string to integers
        # or integers to a string in
        # regard to the user`s choice




import convert_str                                      # importing convert_str module
import convert_int                                      # importing convert_int module
import menu                                             # importing menu modlue




def main():


    user_choice = 1                                     # an integer to hold the user`s choice

    while(user_choice != 0):                            # entering the sentinel-controlled loop

        user_choice = menu.menu()                       # printing the menu

        if(user_choice == 1):                           # validating the input
            
            user_str = input("\nEnter the string > ")   # prompting the user to enter a string
            convert_str.convert_string(user_str)        # calling convert_string method

        elif(user_choice == 2):                            
            
            user_num = input('Enter an integer> ')      # prompting the user to enter an integer
            convert_int.convert_integer(user_num)       # calling convert_integer method


        else:

            print('\nThe program has ended!\n')         # a message indicating that the program
                                                        # has ended
   
    
       



main()                                                  # calling the main() function



