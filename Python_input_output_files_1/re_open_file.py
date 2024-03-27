


def re_enter():                                                                         

    output_file = open("Names.txt", 'a')                                                
                                                                                        
    name = input("\nEnter a name. Type '0' to quit " + \
        "entering> ")

    while(name != '0'):                                                                 

        output_file.write(name + '\n')                                                  
        name = input("\nEnter a name. Type '0' to quit " +\
                     "entering> ")

        if(name != '0'):
            output_file.write(name + '\n')


    output_file.close()                                                                 
                                                                                        
    print("\n\tThe data`s been added to the " + \
        "file!")

    input("\n\tPress <Enter> to continue. . . ")                                        
                                                                                        



