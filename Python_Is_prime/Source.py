

import Menu                                                                                         
import Is_prime                                                                                     




def main():


    choice = Menu.menu()                                                                            

    while(choice != 0):                                                                             

        if(choice == 1):                                                            

            num = int(input("\nEnter an integer> "))                                                
            Is_prime.prime(num)                                                                     

        elif(choice == 2):

            print("\nEnter the range:")                                                             
            start = int(input("Start> "))                                                           
            end = int(input("End> "))

            for i in range(start, end + 1, 1):

                Is_prime.prime(i)                                                                   


        choice = Menu.menu()                                                                        


    print("\nThe program has ended\n")                                                              
                                                                                                    






main()                                                                                              



