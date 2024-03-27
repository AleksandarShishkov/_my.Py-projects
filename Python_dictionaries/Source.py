

import Options                                                                                                          





def main():



    choice = 1                                                                                                          
    name_email = {}                                                                                                     
                                                                                                                        

    telephone = {}                                                                                                      

    address = {}                                                                                                        



    while(choice != 0):                                                                                                 

        choice = Options.menu(choice)                                                                                   
        
        
        if(choice == 1):                                                                                                
            name = input("\nEnter a name to create a new contact> ")                                                    

            if(name in name_email):                                                                                     

                print("\n\tThis contact is already on the list!\n")

            else:

                email = input("Enter the e-mail address> ")                                                             
                name_email[name] = email                                                                                
                telephone[name] = ''                                                                                    
                address[name] = ''                                                                                      

                print("\n\tThe contact`s been saved successfully!\n")


        elif(choice == 2):

            name = input("\nEnter the contact`s name> ")                                                                

            if(name in name_email):                                                                                     

                try:                                                                                                    

                    telephone_num = input("\nEnter the contact`s phone number> ")                                       
                    telephone[name] = telephone_num                                                                     
                    print("\n\tThe phone number`s been saved successfully!\n")

                except ValueError:

                    print("'", telephone_num, "' cannot be a valid telephone.")                                         
                    telephone_num = input("Try again> ")


            else:

                print("\n\tNo such name. You should create the contact first!\n")                                       



        elif(choice == 3):

            name = input("\nEnter the contact`s name> ")                                                                

            if(name in name_email):                                                                                     

                contact_address = input("\nEnter the contact`s address> ")                                              
                address[name]= contact_address                                                                          

                print("\n\tThe address`s been saved successfully!\n")

            else:

                print("\n\tNo such name. You should create the contact first!\n")                                       



        elif(choice == 4):

            name = input("\nEnter the contact`s name> ")                                                                

            if(name in name_email):                                                                                     

                print("\nThe current email is: ", name_email[name])                                                      
                change = input("Do you want to change it? (y/n)> ")                                                     

                while(change.lower() != 'y' and change.lower() != 'n'):                                                 

                    print("'", change.lower(), "' cannot be a valid input.")
                    change = input("Try again> ")

                if(change.lower() == 'y'):

                     new_email = input("\nEnter the new e-mail address> ")                                              
                     name_email[name] = new_email                                                                       
                     print("\n\tThe e-mail`s been changed successfully!\n")

                else:

                     print("\n\tNo changes were made!\n")                                                   


            else:

                print("\n\tNo such name. You should create the contact first!\n")                                       




        elif(choice == 5):

            name = input("\nEnter the contact`s name> ")                                                                

            if(name in name_email):                                                                                     

                print("The current tepelhone number is: ", telephone[name])                                             
                change = input("Do you want to change it? (y/n)> ")                                                     

                while(change.lower() != 'y' and change.lower() != 'n'):                                                 

                    print("'", change, "' cannot be a valid input.")
                    change = input("Try again> ")

                if(change == 'y'):

                    new_phone = input("\nEnter the new telephone number> ")                                             
                    telephone[name] = new_phone                                                                         

                    print("\n\tThe phone number`s been changed successfully!\n")

                else:

                    print("\n\tNo changes were made!\n")

            else:

                print("\n\tNo such name. You should create the contact first!\n")                                       




        elif(choice == 6):

            name = input("\nEnter the contact`s name> ")                                                                

            if(name in name_email):                                                                                     

                print("\nThe current address is: ", address[name])                                                      
                change = input("Do you want to change it? (y/n)> ")                                                     

                while(change.lower() != 'y' and change.lower() != 'n'):                                                 

                    print("'", change, "' cannot be a valid input.")
                    change = input("Try again> ")


                if(change.lower() == 'y'):

                    new_address = input("\nEnter the new address> ")                                                    
                    address[name] = new_address                                                                         

                    print("\n\tThe address`s been changed successfully!\n")

                else:

                    print("\n\tNo chamnges were made!\n")

            else:

                print("\n\tNo such name. You should create the contact first!\n")                                       




        elif(choice == 7):

            name = input("\nEnter the contact`s name> ")                                                                

            if(name in name_email):                                                                                     

                print("\n\tContact:\n")                                                                                 
                print("Name:            ", name)
                print("E-mail:          ", name_email[name])
                print("Phone number:    ", telephone[name])
                print("Address:         ", address[name])

                delete = input("\nDelete (y/n)> ")                                                                      
        
                while(delete.lower() != 'y' and delete.lower() != 'n'):                                                 

                    print("'", delete, "' cannot be a valid input.")
                    delete = input("Try agian> ")


                if(delete == 'y'):

                    del name_email[name]                                                                                
                    del telephone[name]                                                                                 
                    del address[name]                                                                                   

                    print("\n\tThe contact`s been deleted successfully!\n")

                else:

                    print("\n\tNo changes were made!\n")

            else:

                print("\n\tNo such name. You should create the contact first!\n")                                       






        elif(choice == 8):

            
            delete = input("\nDo you want to delete all of the contacts? (y/n)> ")                                     
                                                                                                                       

            while(delete.lower() != 'y' and delete.lower() != 'n'):                                                    

                print("'", delete, "' cannot be a valid input")
                delete = input("Try again> ")


            if(delete.lower() == 'y'):

                name_email.clear()                                                                                     
                telephone.clear()                                                                                      
                address.clear()                                                                                        

                print("\nThe contacts has been erased!\n")



        elif(choice == 9):

            print("\n\t", len(name_email), " record/s:\n")                                                             

            count = 0                                                                                                  

            for key in name_email:                                                                                     

                count += 1
                print("#", count, ":")
                print("Name:            ", key)
                print("E-mail:          ", name_email[key])
                print("Phone number:    ", telephone[key])
                print("Address:         ", address[key])
                print('\n')


        else:

            print("\n\tThe program has ended!\n")                                                                      
                                                                                                                       





main()                                                                                                                 






