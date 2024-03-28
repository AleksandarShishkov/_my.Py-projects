



import random                                                                       



def a_file(name_file):                                                               
                                                                                    


                                                                                    
    choice = input("\nDo you want to include additional numbers " +\
        "to the file (y/n) > ")

    while(choice != 'y' and choice != 'n'):                                         
        choice = input("\nInvalid input. Try again> ")


    if(choice == 'y'):

                                                                                    
                                                                                    
        print("\nYou have selected to add numbers to " +\
            "the file")

        f_name = input("\nEnter the name of the file> ")                            

        while(f_name != name_file):                                                 
            f_name = input("\nInvalid input. Try again> ")

        add_to_file = open(f_name, 'a')                                             
    

        try:

                                                                                    
                                                                                    
                                                                                    
            num_numbers = int(
                input("\nHow many numbers will be added? > "))

        except ValueError:                                                          
            print("\nInvalid value entered.\n")


        try:

                                                                                    
                                                                                    
            num_limit = int(
                input("\nWhat is the limit (the highest number) > "))

        except ValueError:                                                          
            print("\nInvalid value entered.\n")

            

        for i in range(1, num_numbers + 1):

            r_num = random.randrange(1, num_limit)                                  

            add_to_file.write(str(r_num) + '\n')                                    



        print("\nThe data has been added to the file")                              
                                                                                    

        add_to_file.close()                                                         

        return True                                                                 

    else:

        print("\nNo numbers will be included.")                                      
                                                                                    

        return False                                                                


