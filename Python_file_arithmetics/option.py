



def user_option(choice):                                        
                                                                
                                                                

   if(choice == 'w'):                                           
       print("\n\tYou have selected to re-write " +\
           "\n\tthe file. Enter the new digits or " +\
           "\n\ttype '-1' to quit entering> ")

       try:                                                     

           output = open("numbers.txt", 'w')                    
           num = int(input("\nEnter an integer> "))             
                                                                
        
           while(num != -1):                                    

               if(num != -1):
                   output.write(str(num) + '\n')                
                                                                

               num = int(input("\nEnter an integer> "))


           output.close()                                       

       except ValueError:                                       
           print("\nInvalid value passed!\n")                   

       print("\nThe file has been re-written " +\
           "\nsuccessfully\n")

   elif(choice == 'r'):                                         
        
       print("\n\tYou have selected to review " +\
           "\n\tthe file. The numbers are: \n")

       input_file = open("numbers.txt", 'r')                    
                                                                

       numbersStr = input_file.readline()                        
                                                                
       while numbersStr != '':                                  
        
           numbers = int(numbersStr)                            
                                                                
           print(numbers, end = ' ')                            
           numbersStr = input_file.readline()                   
            
    

    
       input_file.close()                                       
       print('\n')

   
   elif(choice == 'a'):                                         
       print("\n\tYou have selected to add data " +\
           "\n\tto the file. Add the new digits or " +\
           "\n\ttype '-1' to quit adding> ")

       try:                                                     

           output = open("numbers.txt", 'a')                     
                                                                

           number = int(input("\nAdd an integer> "))            
                                                                
        
           while(number != -1):                                 

               if(number != -1):
                   output.write(str(number) + '\n')             

               number = int(input("\nEnter an integer> "))                                                                      # another integer

               
           output.close()                                       


       except ValueError:                                       
           print("\nInvalid value passed!\n")                   

       print("\nThe new data has been added "+\
           "\nsuccessfully\n")


   elif(choice == "sum"):                                       
      print("\n\tYou have selected to sum the data. " +\
          "\n\n\tThe result is:", end = ' ')

      input_file = open("numbers.txt", 'r')                      
                                                                
      numbersStr = input_file.readline()                        
                                                                
      total = 0                                                 
                                                                

      while numbersStr != '':                                   
        
          numbers = int(numbersStr)                             
                                                                
          total += numbers                                      
                                                                
          numbersStr = input_file.readline()                    
      
      print("'", total, "'\n")                                  
    
      input_file.close()                                        


   elif(choice == "substr"):                                    
     print("\n\tYou have selected to substract " +\
         "\n\t the file`s data. " +\
         "\n\tThe result is:", end = ' ')

     input_file = open("numbers.txt", 'r')                      
                                                                

     numbersStr = input_file.readline()                         

     substr = int(numbersStr)                                   
                                                                

     while numbersStr != '':                                    
        
         numbers = int(numbersStr)                              
                                                                
         substr -= numbers                                      
         numbersStr = input_file.readline()                     
      
     print("'", substr, "'\n")                                      
     input_file.close()                                         
    

   elif(choice == "multiply"):                                  
    print("\n\tYou have selected to multiply " +\
        "\n\tthe file`s data. " +\
        "\n\tThe result is:", end = ' ')

    input_file = open("numbers.txt", 'r')                       
                                                                

    numbersStr = input_file.readline()                           
                                                                
    mult = int(numbersStr)                                      
                                                                

    while numbersStr != '':                                     
        
        numbers = int(numbersStr)                               
                                                                
        mult *= numbers                                         
        numbersStr = input_file.readline()                      
      
    print("'", mult, "'\n")                                     

    input_file.close()                                          


   elif(choice == "divide"):                                    
    print("\n\tYou have selected to divide " +\
        "\n\t the file`s data. " +\
        "\n\tThe result is:", end = ' ')

    input_file = open("numbers.txt", 'r')                       
                                                                
    numbersStr = input_file.readline()                          
       
    divide = float(numbersStr)                                   
                                                                

    while numbersStr != '':                                     
        
        numbers = float(numbersStr)                             
                                                                
        divide /= numbers                                       
        numbersStr = input_file.readline()                      
      
    print("'", format(divide, '.10f'), "'\n")                   

    input_file.close()                                          


   elif(choice == "avrg"):                                      
    print("\n\tYou have selected to calculate " +\
       "\n\tthe file`s data average. " +\
       "\n\tThe result is:", end = ' ')
    
    input_file = open("numbers.txt", 'r')                       
                                                                
    numbersStr = input_file.readline()                          

    count = 0                                                   
                                                                
    total = 0                                                   
                                                                

    while numbersStr != '':                                     
        
        numbers = int(numbersStr)                               
                                                                
        total += numbers                                        
        numbersStr = input_file.readline()                      
        count += 1                                              
    
    average = float(total / count)                              
    print("'", format(average, '.2f'), "'\n")                   
                                                                

    input_file.close()                                          


   elif(choice == '0'):                                         

                                                                
    print("\n\tYou have selected to quit " +\
       "\n\tthe program. \n\n")

