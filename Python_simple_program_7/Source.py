

def main():                                                    

                                                               
    num = int(input("\nEnter and integer." + \
                    " To view the sum enter negative value > "))

    total = 0                                                  

    while (num > 0):                                           

        total += num                                           

                                                               
        num = int(input("\nEnter and integer." + \
                    " To view the sum enter negative value > "))


    print("\nThe total is : ", total, "\n")                    


main()                                                         
