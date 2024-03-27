



def i_file():                                                   
    
    print("\n\tThe numbers are: \n")

    input = open("numbers.txt", 'r')                            
    numbersStr = input.readline()                               
                                                                
    while numbersStr != '':                                     
        
        numbers = int(numbersStr)                                
                                                                

        print(numbers, end = ' ')                               
        numbersStr = input.readline()                           
                                                                            
    

    
    input.close()                                               



