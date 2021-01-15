



        # A Python program that prompts
        # the user to initialize a list of
        # integers with user-defined size.
        #
        # It then shows a menu with different
        # arithmetic operations as options.
        #
        # The program outputs the calculations
        # in dependance of the oprion selected.




import menu                                                                     # importing the menu module



def main():




    aList = []                                                                  # an empty list
    
    select = 1                                                                  # an integer to hold the selected option

    while (select != 0):                                                        # validating the option serlected in outer loop
    
        size = int(input(                                                       # prompting the user to select the size of the list
            "\nEnter the size of the list> "))

        print('\nEnter the elements:')                                          # prompting the user to enter integers on the list

        for i in range(0, size):

            print("Element ", i + 1, "> ", end = ' ')
            num = int(input())
            aList += [num]


        select = menu.menu_option()                                             # calling the menu_option() function


        while(select != 5 and select != 0):                                     # validating the option selected in inner loop

            

            if(select == 1):

                find_num = int(input("\nWhich number you are " \
                "searching for?> "))                                            # prompting the user to select the searched integer

                if(find_num in aList):                                          # validating the input
                    print("\nThe number`s on the list!\n")
                else:
                    print("\nThe number`s not on the list!\n")


            elif(select == 2):

                sum_list = sum(aList)                                           # summing the list`s elements

                print("\nThe sum of the elements is: ", sum_list)               # printing the result


            elif(select == 3):
            
                product = 1                                                     # aninteger with default value assigned 

                for element in aList:

                    product *= element                                          # calculating the product

                print("\nThe product is: ", product)                            # printing the result


            elif(select == 4):

                avrg = sum(aList) / size                                        # calculating the average
                
                print("\nThe average is: ", format(avrg, '.2f'))                # printing the result


            elif(select == 5):

                print("\nYou have created a new list!\n")
                break;


            elif(select == 6):
                print("\nThe list is: ")

                for element in aList:                                             # printing the elements on the list

                    print(element, end = ' ')

                print('\n')

            elif(select == 0):

                print("\nYou have exited the menu!\n")                             # printing message indicating that the menu`s been
                                                                                   # exited
           
            else:

                print("\nInvalid input!\n")

            select = menu.menu_option()                                             # printing the menu


    print("\nThe program has ended!\n")




main()                                                                              # calling the main() function


