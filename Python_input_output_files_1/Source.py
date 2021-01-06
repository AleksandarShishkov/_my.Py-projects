



        # # # # # # # # # # # # # # # # # # # # # # # # #
        # 
        #  This Python program prompts the user to enter 
        #  series of string on a newly created .txt file.
        #  It provides a sentinel value to control the   
        #  number of entered data, validates the input   
        #  and prints the output on the screen.           
        #                                               
        #  The program also asks the user to choose      
        #  whether another string will be added to the   
        #  existing file.                                
        #                                               
        # # # # # # # # # # # # # # # # # # # # # # # # #





import o_file                                                                           # importing the o_file module
import i_file                                                                           # importing the i_file module
import re_open_file                                                                     # importing the re_open_file module




def main():                                                                             # delcaring the main() fumnction


    

    o_file.file_output()                                                                # callingthe file_output() function
    i_file.file_input()                                                                 # calling the file_input() function

    new_name = input("\n\tDo you want to add a name? (y/n)> ")                          # prompting the user to select whether 
                                                                                        # another name will be added
    if(new_name == 'y' or new_name == 'Y'):                                             # validating the input

        re_open_file.re_enter()                                                         # calling re_enter() function
        i_file.file_input()                                                             # calling the file_input() function

    else:
        print("\nThe program has ended!\n")                                             # printing message that the program`s ended


    exit(0)                                                                             # exiting the program


main()                                                                                  # calling the main() function



