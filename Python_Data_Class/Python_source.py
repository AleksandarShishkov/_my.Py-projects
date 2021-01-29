


        # A Python program that prompts the
        # user to create an instance of Data_Class
        # class trough a list of options.
        #
        # The user can review the new profile or
        # to create new one.
        #
        # To exit the program option '0'
        # shold be selected.



import Data_Class                                           # importing Data_Class 
import options                                              # importing options


def main():


    choice = 1                                              # an integer to hold the choice
    exsProfile = False                                      # a boolean for an exsisting profile

     

    while(choice != 0):                                     # cotrolled while loop

        choice = options.options()                          # calling options() method

        if(choice == 1):                                    # validating the input

            exsProfile = True                               # setting exsProfile to True
            profile = Data_Class.Data_Class()               # creating an instance of Data_Class class

            profile.set_name()                              # calling set_name() method
            profile.set_age()                               # calling set_age() method
            profile.set_address()                           # calling set_address() method
            profile.set_phone()                             # calling set_phone() method


        elif(choice == 2 and exsProfile):

            print('\nThe profile you`ve selected is:')
            profile.print()                                 # calling print() method


        elif(choice == 0):

            break;                                          # breaking out of the loop

       
        else:

            print('\nInvalid input')


    print('\nThe program has ended!\n')                     # a message indicating that the program
                                                            # has ended


main()                                                      # calling main() function


