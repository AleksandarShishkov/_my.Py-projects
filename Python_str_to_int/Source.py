

import convert_str                                                      
import convert_int                                                      
import menu                                                             




def main():


    user_choice = 1                                                     

    while(user_choice != 0):                                            

        user_choice = menu.menu()                                       

        if(user_choice == 1):                                           
            
            user_str = input("\nEnter the string > ")                   
            convert_str.convert_string(user_str)                        

        elif(user_choice == 2):                            
            
            user_num = input('Enter an integer> ')                      
            convert_int.convert_integer(user_num)                       


        else:

            print('\nThe program has ended!\n')                         
                                                                        
   
    
       



main()                                                                  



