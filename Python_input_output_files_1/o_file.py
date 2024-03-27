


def file_output():                                                                      

    print("\n\tWrite series of names to " + \
        "\n\ta file. To quit entering type '0'\n")


    output = open("Names.txt", 'w')                                                     
    name = input("\nEnter a name> ")                                                    
    output.write(name + '\n')                                                           
    
    while name != '0':                                                                  
            
        name = input("\nEnter a name> ")
        
        if(name != '0'):
            output.write(name + '\n')



    output.close()                                                                      
                                                                                        
    print("\n\tThe data`s been written to the " + \
        "file!")

    input("\n\tPress <Enter> to continue. . . ")                                        
                                                                                        

