

import output_file                                                                  
import input_file                                                                   
import Search_list                                                                  


def main():


    file_name = output_file.open_file()                                             
                                                                                    

    list_num = input_file.read_file(file_name)                                      
                                                                                    
                                                                                    


    print("\nEnter the number you are searching for or press '-1' to quit> ")        
    num = int(input())                                                              

    while(num != -1):                                                               


        Search_list.serch(list_num, num)                                            
                                                                                    

        print("\nEnter the number you are searching for or press '-1' to quit> ")   
        num = int(input())



    print("\nThe program has ended!\n")                                             




main()                                                                              


