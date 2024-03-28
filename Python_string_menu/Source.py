

import count_words                                                                      
import average_letters                                                                  
import num_upper                                                                        
import num_lower                                                                        
import convert_f_letter_capital                                                         
import convert_f_letter_lower                                                           
import num_spaces                                                                       
import num_digits                                                                       
import num_consonants                                                                   
import menu                                                                             
import num_vowels                                                                       





def main():

    user_choice = 1                                                                     
    
    user = input('\nEnter a sting> ')                                                   



    while(user_choice != 0):                                                            

        user_choice = menu.user_menu()                                                  

        if(user_choice == 1):                                                           

            count_words.num_words(user)                                                 

        elif(user_choice == 2):

            average_letters.average(user)                                               

        elif(user_choice == 3):

            num_upper.upper_case(user)                                                  

        elif(user_choice == 4):

            num_lower.lower_case(user)                                                  

        elif(user_choice == 5):

            convert_f_letter_capital.convert_capital(user)                              

        elif(user_choice == 6):

            convert_f_letter_lower.convert_lower(user)                                  

        elif(user_choice == 7):

            num_spaces.spaces(user)                                                     

        elif(user_choice == 8):

            num_digits.digits(user)                                                     

        elif(user_choice == 9):

            num_consonants.consonants(user)                                             

        elif(user_choice == 10):

            num_vowels.vowels(user)                                                     

        elif(user_choice == 11):

            user = input('\nEnter the new string> ')                                    

        else:

            print('\nThe program has ended!\n')                                         
                                                                                        


main()                                                                                  


