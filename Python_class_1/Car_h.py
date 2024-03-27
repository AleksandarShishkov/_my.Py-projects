



class Car():                                                                                    
   
    __year = ' '                                                                                
    __make = ' '                                                                                
    __speed = ' '                                                                               




    def __init__(self, year, make):                                                                       
                                                                                                

        self.__year = year                                                                      
        self.__make = make                                                                      
        self.__speed = 0                                                                        


    def accelerate(self, acc):                                                                  
                                                                                                

        self.__speed += acc                                                                     


    def brake(self, br):                                                                        
                                                                                                

        self.__speed -= br                                                                      


    def get_current_speed(self):                                                                
        return self.__speed                                                                     


    def set_current_speed_acc(self):                                                            
        self.__speed = 400                                                                      


    def set_current_speed_br(self):                                                             

        self.__speed = 0                                                                        
        

    def get_speed(self):                                                                        

        print('\nThe speed of the ', self.__make, ', year ', self.__year, ' is: ', self.__speed, 'km/h')


