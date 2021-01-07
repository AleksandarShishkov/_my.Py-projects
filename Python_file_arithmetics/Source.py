


        # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #  
        #  This program prompts the user to create a .txt
        #  file and to write series of integers to it. A menu
        #  of options is then shown and asks the user to
        #  select one of them. A result is calculated and shown.
        #
        #  The user exits the program once option '0' is 
        #  selected from the menu.
        #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 




import output_file                                              # importing the output_file module
import input_file                                               # importing the input_file module
import menu                                                     # importing the menu module
import option                                                   # importing the option module


def main():                                                     # declaring the main() function


    output_file.o_file()                                        # calling the o_file() function
    input_file.i_file()                                         # calling he i_file() function

    choice = menu.menu_file()                                   # calling the menu_file() function
                                                                # and assigning the returned
                                                                # value to the choice variable
    
    while choice != '0':                                        # entering the program loop

        option.user_option(choice)                              # calling the user_option()
                                                                # function, passing choice as
                                                                # a parameter

        choice = menu.menu_file()                               # calling the menu_file() function
                                                                # and assigning the returned
                                                                # value to the choice variable
    

    print("The program has ended!\n\n")                         # printing message that the
                                                                # program`s ended

  





main()                                                          # calling the main() function


