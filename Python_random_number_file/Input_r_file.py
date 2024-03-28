



def i_file(name_file):                                                               
                                                                                    

    total = 0                                                                       
    num_read = 0                                                                    



    n_file = input("\nEnter the name of the file> ")                                

    while(n_file != name_file):                                                     
        n_file = input("\nInvalid input. Try again> ")



    print("\nThe numbers are: \n")                                                  
    input_file = open(n_file, 'r')                                                  

    try:

        str_num = input_file.readline()                                             
        
        while(str_num != ''):

            r_num = int(str_num)                                                    
                                                                                    

            print(r_num)                                                            

            total += r_num                                                          
            num_read += 1                                                           

            str_num = input_file.readline()                                         

    except IOError:                                                                 
        print("\nError while reading the file\n")
        

    print("\nThe total of the numbers is: ", total)                                 
    print("The numbers read are: ", num_read)                                       





