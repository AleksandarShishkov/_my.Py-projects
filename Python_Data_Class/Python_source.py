

import Data_Class                                                                        
import options                                                                          


def main():


    choice = 1                                                                          
    exsProfile = False                                                                  

     

    while(choice != 0):                                                                 

        choice = options.options()                                                      

        if(choice == 1):                                                                

            exsProfile = True                                                           
            profile = Data_Class.Data_Class()                                           

            profile.set_name()                                                          
            profile.set_age()                                                           
            profile.set_address()                                                       
            profile.set_phone()                                                         


        elif(choice == 2 and exsProfile):

            print('\nThe profile you`ve selected is:')
            profile.print()                                                             


        elif(choice == 0):

            break;                                                                      

       
        else:

            print('\nInvalid input')


    print('\nThe program has ended!\n')                                                 
                                                                                        


main()                                                                                  


