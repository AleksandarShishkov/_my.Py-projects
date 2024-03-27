

import menu                                                                     



def main():




    aList = []                                                                  
    
    select = 1                                                                  
    while (select != 0):                                                        
    
        size = int(input(                                                       
            "\nEnter the size of the list> "))

        print('\nEnter the elements:')                                          

        for i in range(0, size):

            print("Element ", i + 1, "> ", end = ' ')
            num = int(input())
            aList += [num]


        select = menu.menu_option()                                             


        while(select != 5 and select != 0):                                     

            

            if(select == 1):

                find_num = int(input("\nWhich number you are " \
                "searching for?> "))                                            
                if(find_num in aList):                                          
                    print("\nThe number`s on the list!\n")
                else:
                    print("\nThe number`s not on the list!\n")


            elif(select == 2):

                sum_list = sum(aList)                                           

                print("\nThe sum of the elements is: ", sum_list)               


            elif(select == 3):
            
                product = 1                                                      

                for element in aList:

                    product *= element                                          

                print("\nThe product is: ", product)                            


            elif(select == 4):

                avrg = sum(aList) / size                                        
                
                print("\nThe average is: ", format(avrg, '.2f'))                


            elif(select == 5):

                print("\nYou have created a new list!\n")
                break;


            elif(select == 6):
                print("\nThe list is: ")

                for element in aList:                                           

                    print(element, end = ' ')

                print('\n')

            elif(select == 0):

                print("\nYou have exited the menu!\n")                             
                                                                                              
            else:

                print("\nInvalid input!\n")

            select = menu.menu_option()                                             


    print("\nThe program has ended!\n")




main()                                                                              


