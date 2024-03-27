



class Profile_class():                                                                          
    
    __name = ' '                                                                                
    __ID_num = ' '                                                                              
    __department = ' '                                                                          
    __job_title = ' '                                                                           


    def __init__(self):                                                                         
        self.__name = ' '
        self.__ID_num = ' '
        self.__department = ' '
        self.__job_title = ' '



    def set_name(self):                                                                         

        self.__name = input('Enter the name> ')


    def set_ID(self):                                                                           

        self.__ID_num = int(input('\nEnter the profile`s ID num> '))



    def set_dept(self):                                                                         

        self.__department = input('Enter the department> ')



    def set_job_title(self):                                                                    

        self.__job_title = input('Enter the job title> ')



    def get_name(self):                                                                         

        return self.__name


    def get_ID(self):                                                                           

        return self.__ID_num


    def get_dept(self):                                                                         

        return self.__department


    def get_job_title(self):                                                                    

        return self.__job_title








