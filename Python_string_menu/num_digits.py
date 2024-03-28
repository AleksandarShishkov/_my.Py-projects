



def digits(user):                                                                       


    numInt = 0                                                                          
    total = 0                                                                           
    num_digits = []                                                                     
    digits = False                                                                      



    for i in range(len(user)):

        if(ord(user[i]) > 47 and ord(user[i]) < 58):                                    
                
            numInt += 1                                                                 
            total += int(user[i])                                                       
            num_digits += list(user[i])                                                 
            digits = True                                                               



    if(digits):                                                                         

        print('\nString: ', user)                                                       
        print("Number of integers: ", numInt)                                           
        print('Integers:            ', end = '')                                        

        for i in num_digits:

            print(i, end = ' ')


        print("\nTotal:              ", total)                                           


    else:

        print("\nNo integers located")                                                  
                                                                                        
