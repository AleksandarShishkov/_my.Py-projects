



class Data_Class():                                         # class Data_Class
    
    __name = ' '                                            # a string to hold the name
    __age = ' '                                             # an integer to hold the age
    __address = ' '                                         # a string to hold the address
    __phone = ' '                                           # an integer to hold the phone

    def __init__(self):                                     # default constructor

        self.__name = ' '
        self.__age = ' '
        self.__address = ' '
        self.__phone = ' '

    def set_name(self):                                     # set_name() method

        self.__name = input('\nEnter the name> ')           # promting the user to enter the name


    def set_age(self):                                      # set_age() method

        print('\nEnter the age of ', self.__name, end = '') # promting the user to enter the age
        self.__age = int(input('> '))


    def set_address(self):                                  # set_address() methtod

        self.__address = input('\nEnter the address> ')     # promting the user to enter the address


    def set_phone(self):                                    # set_phone() method

        self.__phone = int(input('\nEnter the phone> '))    # promting the user to enter the phone


    def get_name(self):                                     # getter for the name

        return self.__name


    def get_age(self):                                      # getter for the age

        return self.__age


    def get_address(self):                                  # getter for the address

        return self.__address


    def get_phone(self):                                    # getter for the phone

        return self.__phone



    def print(self):                                        # print() method
                                                            # printing the output
        print('\nName:        ' + self.__name)
        print('Age:        ', self.__age)
        print('Address:    ', self.__address)
        print('Phone:      ', self.__phone)

        print('\n')


