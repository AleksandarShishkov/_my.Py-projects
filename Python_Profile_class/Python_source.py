


        # A Python program that creates an instance 
        # of a class and promts the user to set it`s
        # attributes so they can be
        # stored in a dictionary. 
        # 
        # Trough a menu the user can manipulate
        # the enrtered data. 
        #
        # Once done, the user can exit the program
        # by sleecting '0' from the options.





            
import Profile_class                                                                            # importing Profile_class
import options                                                                                  # importing options
import options_                                                                                 # importing options_


def main():

    choice = 1                                                                                  # an integer to hold the selected
                                                                                                # option form the outer menu

    profName = {}                                                                               # an empty dictionary for the names
    profDept = {}                                                                               # an empty dictionary for the depts
    profJob = {}                                                                                # an empty dictionary for the job titles

    key = ' '                                                                                   # an integer to hold the key

    profile = Profile_class.Profile_class()                                                     # an instance of Profile_class

    try:                                                                                        # try - except statement for input
                                                                                                # validation

        while(choice != 0):                                                                     # entering the outer loop

            choice = options.options()                                                          # calling options() method

            if(choice == 1):                                                                    # validating the input


                key = int(input('\nEnter the profile`s ID> '))                                  # prompting ther user to enter
                                                                                                # the profile`s ID

                if(key not in profName):                                                        # validating the input

                    print('\nYou should create a profile first!')

                else:
                                                                                                # printing the output
                    print('\nProfile ID:     ', key)
                    print('\nName:           ', profName[key])
                    print('Department:     ', profDept[key])
                    print('Job title:      ', profJob[key])
                    


            elif(choice == 2):

                profile.set_ID()                                                                # promting the user to set
                                                                                                # the ID
                key = profile.get_ID()                                                          # assigning the value to key

                if(key not in profName):                                                        # validating the key

                    profile.set_name()                                                          # calling the setter for the name
                    profile.set_dept()                                                          # calling the setter for the dept
                    profile.set_job_title()                                                     # calling the setter for the job title

                    profName[key] = profile.get_name()                                          # adding the name to profName dictionary

                    profDept[key] = profile.get_dept()                                          # adding the dept to profDept dictionary

                    profJob[key] = profile.get_job_title()                                      # adding the job title to profJob dictionary

                    print('\nThe new profile`s been added!')

                else:

                    print('\nThis ID`s been already registered!')


            elif(choice == 3):

                choice_ = 1                                                                     # an integer to hold the selected
                                                                                                # option from the inner menu

                while(choice_ != 0):                                                            # validating the selected option

                    choice_ = options_.options_()                                               # calling options_() method

                    if(choice_ == 1):                                                           

                        print('\n')

                        key = int(input('Enter the profile`s ID or 0 to quit> '))               # promting the user to enter the
                                                                                                # profile`s ID

                        if(key in profName):                                                    # valdiating the key

                            profile.set_name()                                                  # calling the setter for the name
                            profName[key] = profile.get_name()                                  # assigning the input to the
                                                                                                # key value in profName

                            print('\nThe name`s been changed!')

                        elif(key == 0):

                            print('\nTo the options. . .')                                      # exiting the if-elif-else 
                            continue                                                            # statement

                        else:

                            print('\nNo such a profile!')


                    elif(choice_ == 2):

                        print('\n')

                        key = int(input('Enter the profile`s ID or 0 to quit> '))               # promting the user to enter the
                                                                                                # profile`s ID

                        if(key in profDept):                                                    # validating  input

                            profile.set_dept()                                                  # calling the setter for the dept
                            profDept[key] = profile.get_dept()                                  # assigning the input to the
                                                                                                # key value in profDept

                            print('\nThe department`s been changed!')


                        elif(key == 0):

                            print('\nTo the options. . .')                                      # exiting the if-elif-else
                            continue                                                            # statement

                        else:

                            print('\nNo such a profile!')


                    elif(choice_ == 3):

                        print('\n')

                        key = int(input('Enter the profiles` ID or 0 to quit> '))               # promting the user to enter the
                                                                                                # profile`s ID

                        if(key in profJob):                                                     # validating the input

                            profile.set_job_title()                                             # calling the setter for the 
                                                                                                # job title
                            profJob[key] = profile.get_job_title()                              # assigning the input to the
                                                                                                # key value in profJob

                            print('\nThe job title`s been changed!')

                        elif(key == 0):

                            print('\nTo the options. . .')                                      # exiting the if-elif-else
                            continue                                                            # statement

                        else:

                            print('\nNo such a profile!')


                    elif(choice_ == 0):

                        print('\nTo the main. . .')                                             # exiting the inner loop
                        break


                    else:

                        print('\nInvalid option!')


            elif(choice == 4):

                key = int(input('\nEnter the profile`s ID> '))                                  # promting the user to enter the                        
                                                                                                # profile`s ID

                if(key in profName):                                                            # validating the input

                    print('\nProfile ID:      ', key)                                           # printing the result
                    print('\nName:            ', profName[key])
                    print('Department:      ', profDept[key])
                    print('Job title:       ', profJob[key])

                    delete = input('\nDelete the pfile (y/n)> ')                                # promting the user to select
                                                                                                # whether  the datawill be deleted

                    if(delete.lower() == 'y'):                                                  # validating the input

                        del profName[key]                                                       # deleting the key in profName
                        del profDept[key]                                                       # deleting the key in profDept
                        del profJob[key]                                                        # deleting the key in profJob

                        print('\nThe profile`s been deleted!')

                    elif(delete.lower() == 'n'):

                        print('\nNo changes made!')                                             # exiting the if-elif-else
                        break                                                                   # statement
                            
                    else:

                        print('\nInvalid input!')



            elif(choice == 5):

                print('\nNumber of profiles: ', len(profName))                                  # printing the number of
                                                                                                # the records

            elif(choice == 6):

                count = 0;

                for key in profName:                                                            # printing the records

                    count += 1
                    print('\n#', count, sep ='')
                    print('Profile ID:      ', key)
                    print('\nName:            ', profName[key])
                    print('Department:      ', profDept[key])
                    print('Job title:       ', profJob[key])
                    print('\n')


    except:

        print('\nAn error has occured!\n')                                                      # a message if an exception
                                                                                                # is caught
    else:

        print('\nThe program has ended!\n')                                                     # a messsage indicating
                                                                                                # the end of the program


main()



