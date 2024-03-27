



def o_file():                                                   

    
    
    print("\n\tEnter series of integers in a file. " + \
        "\n\tTo quit entering type '-1'\n")

        
    try:                                                       

        output = open("numbers.txt", 'w')                      

        number = int(input("\nEnter an integer> "))            
                                                                       
        while(number != -1):                                   

            if(number != -1):
                output.write(str(number) + '\n')               

            number = int(input("\nEnter an integer> "))        


        output.close()                                         

    except ValueError:                                         
        print("\nInvalid value passed!\n")                     


    print("\n\tThe datas`s been written to the file")
    input("\nTo continue press <Enter> . . .")                 
                                                               










