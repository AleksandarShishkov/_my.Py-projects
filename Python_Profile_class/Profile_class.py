



class Profile_class():                                                                          # Profile_class

    
    __name = ' '                                                                                # a string to hold the name
    __ID_num = ' '                                                                              # an integer to hold the ID
    __department = ' '                                                                          # a string to hold the dept
    __job_title = ' '                                                                           # a string to hold the job title


    def __init__(self):                                                                         # default constructor

        self.__name = ' '
        self.__ID_num = ' '
        self.__department = ' '
        self.__job_title = ' '



    def set_name(self):                                                                         # setter for the name

        self.__name = input('Enter the name> ')


    def set_ID(self):                                                                           # setter for the ID

        self.__ID_num = int(input('\nEnter the profile`s ID num> '))



    def set_dept(self):                                                                         # setter for the dept

        self.__department = input('Enter the department> ')



    def set_job_title(self):                                                                    # setter for the job title

        self.__job_title = input('Enter the job title> ')



    def get_name(self):                                                                         # getter for the name

        return self.__name


    def get_ID(self):                                                                           # getter for the ID

        return self.__ID_num


    def get_dept(self):                                                                         # getter for the dept

        return self.__department


    def get_job_title(self):                                                                    # getter for the job title

        return self.__job_title








