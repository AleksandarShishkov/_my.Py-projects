



class Data_Class():                                                         
    
    __name = ' '                                                            
    __age = ' '                                                             
    __address = ' '                                                         
    __phone = ' '                                                           

    def __init__(self):                                                     

        self.__name = ' '
        self.__age = ' '
        self.__address = ' '
        self.__phone = ' '

    def set_name(self):                                                     

        self.__name = input('\nEnter the name> ')                           


    def set_age(self):                                                      

        print('\nEnter the age of ', self.__name, end = '')                 
        self.__age = int(input('> '))


    def set_address(self):                                                  

        self.__address = input('\nEnter the address> ')                     


    def set_phone(self):                                                    

        self.__phone = int(input('\nEnter the phone> '))                    


    def get_name(self):                                                     

        return self.__name


    def get_age(self):                                                      

        return self.__age


    def get_address(self):                                                  

        return self.__address


    def get_phone(self):                                                    

        return self.__phone



    def print(self):                                                        
                                                                            
        print('\nName:        ' + self.__name)
        print('Age:        ', self.__age)
        print('Address:    ', self.__address)
        print('Phone:      ', self.__phone)

        print('\n')


