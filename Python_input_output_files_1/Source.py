


import o_file                                                                           
import i_file                                                                           
import re_open_file                                                                     




def main():                                                                             


    

    o_file.file_output()                                                                
    i_file.file_input()                                                                 

    new_name = input("\n\tDo you want to add a name? (y/n)> ")                           
                                                                                        
    if(new_name == 'y' or new_name == 'Y'):                                             

        re_open_file.re_enter()                                                         
        i_file.file_input()                                                             

    else:
        print("\nThe program has ended!\n")                                             


    exit(0)                                                                             


main()                                                                                  



