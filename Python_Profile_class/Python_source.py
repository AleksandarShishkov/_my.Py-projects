
            
import Profile_class                                                                            
import options                                                                                  
import options_                                                                                 


def main():

    choice = 1                                                                                  
                                                                                                

    profName = {}                                                                               
    profDept = {}                                                                               
    profJob = {}                                                                                

    key = ' '                                                                                   

    profile = Profile_class.Profile_class()                                                     

    try:                                                                                        
                                                                                                
        while(choice != 0):                                                                     

            choice = options.options()                                                          

            if(choice == 1):                                                                    


                key = int(input('\nEnter the profile`s ID> '))                                  
                                                                                                

                if(key not in profName):                                                        

                    print('\nYou should create a profile first!')

                else:
                                                                                                
                    print('\nProfile ID:     ', key)
                    print('\nName:           ', profName[key])
                    print('Department:     ', profDept[key])
                    print('Job title:      ', profJob[key])
                    


            elif(choice == 2):

                profile.set_ID()                                                                
                                                                                                
                key = profile.get_ID()                                                          

                if(key not in profName):                                                        

                    profile.set_name()                                                          
                    profile.set_dept()                                                          
                    profile.set_job_title()                                                     

                    profName[key] = profile.get_name()                                          
                    profDept[key] = profile.get_dept()                                          

                    profJob[key] = profile.get_job_title()                                      
                    print('\nThe new profile`s been added!')

                else:

                    print('\nThis ID`s been already registered!')


            elif(choice == 3):

                choice_ = 1                                                                     
                                                                                                

                while(choice_ != 0):                                                            

                    choice_ = options_.options_()                                               

                    if(choice_ == 1):                                                           

                        print('\n')

                        key = int(input('Enter the profile`s ID or 0 to quit> '))               
                                                                                                

                        if(key in profName):                                                    

                            profile.set_name()                                                  
                            profName[key] = profile.get_name()                                  
                                                                                                

                            print('\nThe name`s been changed!')

                        elif(key == 0):

                            print('\nTo the options. . .')                                       
                            continue                                                            
                        else:

                            print('\nNo such a profile!')


                    elif(choice_ == 2):

                        print('\n')

                        key = int(input('Enter the profile`s ID or 0 to quit> '))               
                                                                                                

                        if(key in profDept):                                                    

                            profile.set_dept()                                                  
                            profDept[key] = profile.get_dept()                                  
                                                                                                
                            print('\nThe department`s been changed!')


                        elif(key == 0):

                            print('\nTo the options. . .')                                      
                            continue                                                            
                        else:

                            print('\nNo such a profile!')


                    elif(choice_ == 3):

                        print('\n')

                        key = int(input('Enter the profiles` ID or 0 to quit> '))               
                                                                                                

                        if(key in profJob):                                                     
                            profile.set_job_title()                                              
                                                                                                
                            profJob[key] = profile.get_job_title()                              
                                                                                                
                            print('\nThe job title`s been changed!')

                        elif(key == 0):

                            print('\nTo the options. . .')                                      
                            continue                                                            
                        else:

                            print('\nNo such a profile!')


                    elif(choice_ == 0):

                        print('\nTo the main. . .')                                             
                        break


                    else:

                        print('\nInvalid option!')


            elif(choice == 4):

                key = int(input('\nEnter the profile`s ID> '))                                                          
                                                                                                

                if(key in profName):                                                            

                    print('\nProfile ID:      ', key)                                           
                    print('\nName:            ', profName[key])
                    print('Department:      ', profDept[key])
                    print('Job title:       ', profJob[key])

                    delete = input('\nDelete the pfile (y/n)> ')                                
                                                                                                

                    if(delete.lower() == 'y'):                                                  

                        del profName[key]                                                       
                        del profDept[key]                                                       
                        del profJob[key]                                                        
                        print('\nThe profile`s been deleted!')

                    elif(delete.lower() == 'n'):

                        print('\nNo changes made!')                                             
                        break                                                                   
                            
                    else:

                        print('\nInvalid input!')



            elif(choice == 5):

                print('\nNumber of profiles: ', len(profName))                                  
                                                                                                

            elif(choice == 6):

                count = 0;

                for key in profName:                                                            

                    count += 1
                    print('\n#', count, sep ='')
                    print('Profile ID:      ', key)
                    print('\nName:            ', profName[key])
                    print('Department:      ', profDept[key])
                    print('Job title:       ', profJob[key])
                    print('\n')


    except:

        print('\nAn error has occured!\n')                                                      
                                                                                                
    else:

        print('\nThe program has ended!\n')                                                                                                                                                     # the end of the program


main()



