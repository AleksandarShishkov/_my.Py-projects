

import output_file                                              
import input_file                                               
import menu                                                     
import option                                                   


def main():                                                     


    output_file.o_file()                                        
    input_file.i_file()                                         

    choice = menu.menu_file()                                   
                                                                
                                                                
    
    while choice != '0':                                        

        option.user_option(choice)                              
                                                                
                                                                

        choice = menu.menu_file()                               
                                                                
                                                                
    

    print("The program has ended!\n\n")                         
                                                                

  





main()                                                          


