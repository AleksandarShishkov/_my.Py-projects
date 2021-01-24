



        # A Python program that promts the user
        # to enter the details for user defined number
        # of contacts. The program stores the
        # data in three dictionaries.
        #
        # Trough a menu the user can
        # add new contacts or to modify the
        # current records. The user can also
        # delete some of the contacts or all of them.
        #
        # The program terminates once the user
        # selects option '0'





import Options                                                                                              # importing Options module





def main():



    choice = 1                                                                                              # an integer to hold the choice
    name_email = {}                                                                                         # an empty dictionary to hold the names as keys and
                                                                                                            # the emails as values

    telephone = {}                                                                                          # an empty dictionary to hold the phone numbers as values

    address = {}                                                                                            # an empty dictionary to hold the addresses as values



    while(choice != 0):                                                                                     # user controlled loop

        choice = Options.menu(choice)                                                                       # calling the menu() method
        
        
        if(choice == 1):                                                                                    # validating the choice

            name = input("\nEnter a name to create a new contact> ")                                        # promting the user to enter a name for the new contact

            if(name in name_email):                                                                         # validating the name

                print("\n\tThis contact is already on the list!\n")

            else:

                email = input("Enter the e-mail address> ")                                                 # promting the user to enter the email address
                name_email[name] = email                                                                    # stroting the email address in name_email dict
                telephone[name] = ''                                                                        # stroing default value in telephone dict
                address[name] = ''                                                                          # string default value in address dict

                print("\n\tThe contact`s been saved successfully!\n")


        elif(choice == 2):

            name = input("\nEnter the contact`s name> ")                                                    # promting the user to enter the contact`s name

            if(name in name_email):                                                                         # validating the name

                try:                                                                                        # validating the input with try-except blocks

                    telephone_num = input("\nEnter the contact`s phone number> ")                           # promting the user to enter the phone number
                    telephone[name] = telephone_num                                                         # storing it in telephone dict

                    print("\n\tThe phone number`s been saved successfully!\n")

                except ValueError:

                    print("'", telephone_num, "' cannot be a valid telephone.")                             # printing error message if an exception is caught
                    telephone_num = input("Try again> ")


            else:

                print("\n\tNo such name. You should create the contact first!\n")                           # printing a message if no such name excists



        elif(choice == 3):

            name = input("\nEnter the contact`s name> ")                                                    # promting the user to enter the contact`s name

            if(name in name_email):                                                                         # validating the input

                contact_address = input("\nEnter the contact`s address> ")                                  # promting the user to enter the address
                address[name]= contact_address                                                              # storing the input in address dict

                print("\n\tThe address`s been saved successfully!\n")

            else:

                print("\n\tNo such name. You should create the contact first!\n")                           # printing a message if no such name located



        elif(choice == 4):

            name = input("\nEnter the contact`s name> ")                                                    # promting the user to enter the contat`s name

            if(name in name_email):                                                                         # validating the input

                print("\nThe current email is: ", name_email[name])                                         # displaying the current email 
                change = input("Do you want to change it? (y/n)> ")                                         # promting the user to select whether to change it

                while(change.lower() != 'y' and change.lower() != 'n'):                                     # validating the input

                    print("'", change.lower(), "' cannot be a valid input.")
                    change = input("Try again> ")

                if(change.lower() == 'y'):

                     new_email = input("\nEnter the new e-mail address> ")                                  # promting the user to enter the new email
                     name_email[name] = new_email                                                           # modifying the value in name_email dict

                     print("\n\tThe e-mail`s been changed successfully!\n")

                else:

                     print("\n\tNo changes were made!\n")                                                   


            else:

                print("\n\tNo such name. You should create the contact first!\n")                           # printing a message if no such name located




        elif(choice == 5):

            name = input("\nEnter the contact`s name> ")                                                    # promting the user to enter the contact`s name

            if(name in name_email):                                                                         # validating the input

                print("The current tepelhone number is: ", telephone[name])                                 # displaying the current telephone number
                change = input("Do you want to change it? (y/n)> ")                                         # promting the user to select whether to change it

                while(change.lower() != 'y' and change.lower() != 'n'):                                     # validating the input

                    print("'", change, "' cannot be a valid input.")
                    change = input("Try again> ")

                if(change == 'y'):

                    new_phone = input("\nEnter the new telephone number> ")                                 # promting the user to enter new telephone number
                    telephone[name] = new_phone                                                             # modifying the value in telephone dict

                    print("\n\tThe phone number`s been changed successfully!\n")

                else:

                    print("\n\tNo changes were made!\n")

            else:

                print("\n\tNo such name. You should create the contact first!\n")                           # printing a message if no such name located




        elif(choice == 6):

            name = input("\nEnter the contact`s name> ")                                                    # promting the user to enter the contact`s name

            if(name in name_email):                                                                         # validating the input

                print("\nThe current address is: ", address[name])                                          # displaying the current address
                change = input("Do you want to change it? (y/n)> ")                                         # promting the user to select whether to change it

                while(change.lower() != 'y' and change.lower() != 'n'):                                     # validating the input

                    print("'", change, "' cannot be a valid input.")
                    change = input("Try again> ")


                if(change.lower() == 'y'):

                    new_address = input("\nEnter the new address> ")                                        # prompting the user to enter the new address
                    address[name] = new_address                                                             # modifying the value in address dict

                    print("\n\tThe address`s been changed successfully!\n")

                else:

                    print("\n\tNo chamnges were made!\n")

            else:

                print("\n\tNo such name. You should create the contact first!\n")                           # printing a message if no such name located




        elif(choice == 7):

            name = input("\nEnter the contact`s name> ")                                                    # promting the user to enter the contact`s name

            if(name in name_email):                                                                         # validating the input

                print("\n\tContact:\n")                                                                     # printing the contact`s details
                print("Name:            ", name)
                print("E-mail:          ", name_email[name])
                print("Phone number:    ", telephone[name])
                print("Address:         ", address[name])

                delete = input("\nDelete (y/n)> ")                                                          # prompting the user to select whether to delete it

                while(delete.lower() != 'y' and delete.lower() != 'n'):                                     # validating the input

                    print("'", delete, "' cannot be a valid input.")
                    delete = input("Try agian> ")


                if(delete == 'y'):

                    del name_email[name]                                                                    # deleting the record in name_email dict
                    del telephone[name]                                                                     # deleting the record in telephone dict
                    del address[name]                                                                       # deleting the record in address dict

                    print("\n\tThe contact`s been deleted successfully!\n")

                else:

                    print("\n\tNo changes were made!\n")

            else:

                print("\n\tNo such name. You should create the contact first!\n")                           # printing a messsage if no such name located






        elif(choice == 8):

            
            delete = input("\nDo you want to delete all of the contacts? (y/n)> ")                          # promting the user to select whether to keep or
                                                                                                            # to delete all of the contacts

            while(delete.lower() != 'y' and delete.lower() != 'n'):                                         # validating the input

                print("'", delete, "' cannot be a valid input")
                delete = input("Try again> ")


            if(delete.lower() == 'y'):

                name_email.clear()                                                                          # deleting the records in name_email dict
                telephone.clear()                                                                           # deleting the records in telephone dict
                address.clear()                                                                             # deleting the recordds in address dict

                print("\nThe contacts has been erased!\n")



        elif(choice == 9):

            print("\n\t", len(name_email), " record/s:\n")                                                  # printing a message with the number of the records

            count = 0                                                                                       # an integer to keep count of the contacts

            for key in name_email:                                                                          # dispalying the details for each record

                count += 1
                print("#", count, ":")
                print("Name:            ", key)
                print("E-mail:          ", name_email[key])
                print("Phone number:    ", telephone[key])
                print("Address:         ", address[key])
                print('\n')


        else:

            print("\n\tThe program has ended!\n")                                                           # printing a message indicating that the program
                                                                                                            # has ended





main()                                                                                                      # calling the main function






