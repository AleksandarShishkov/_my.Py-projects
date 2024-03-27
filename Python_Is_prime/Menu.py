



def menu():                                                                                         


    print("\n\tSelect between the follwiong:\n")                                                    
    print("'1' to input a number")
    print("'2' to input range of numbers")
    print("'0' to quit")

    try:                                                                                            

        choice = int(input("\n> "))                                                                 

        while(choice < 0 or choice > 2):                                                            

            print("\nInvalid input")
            choice = int(input("Try again> "))


        return choice                                                                               

    except ValueError:

        print("\nInvalid input.")                                                                   
        choice = int(input("Try again> "))                                                          
                                                                                                    



