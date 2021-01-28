



class Car():                                                                                    # class Car
   
    __year = ' '                                                                                # a private integer to hold the year
    __make = ' '                                                                                # a private string to hold the make
    __speed = ' '                                                                               # a private integer to hold the speed




    def __init__(self, year, make):                                                             # constructor with parameters for the year          
                                                                                                # and the make

        self.__year = year                                                                      # setting __year to year
        self.__make = make                                                                      # setting __make to make
        self.__speed = 0                                                                        # setting __speed to speed


    def accelerate(self, acc):                                                                  # setter for the acceleration with an argument for
                                                                                                # the value

        self.__speed += acc                                                                     # adding value to __speed


    def brake(self, br):                                                                        # setter for the break with an argument for
                                                                                                # the value

        self.__speed -= br                                                                      # substracting the value to __speed


    def get_current_speed(self):                                                                # getter for the current speed

        return self.__speed                                                                     # returning __speed


    def set_current_speed_acc(self):                                                            # setter for the acceleration maximum

        self.__speed = 400                                                                      # assigning 400 to __speed


    def set_current_speed_br(self):                                                             # setter for the breaking minimum

        self.__speed = 0                                                                        # assignin 0 to __speed
        

    def get_speed(self):                                                                        # getter for the result

        print('\nThe speed of the ', self.__make, ', year ', self.__year, ' is: ', self.__speed, 'km/h')


