



import Car                                                                                      # importing the Car module


def main():


    user = 'y'                                                                                  # setting user to 'y'

    car = Car.Car(2010, 'Audi')                                                                 # an instance of the Car class

    car.get_speed()                                                                             # calling the get_speed() method

    while(user.lower() != '0'):                                                                 # a user controlled loop

        user = input('\nIs the car accelerating (y/n or 0 to quit)> ')                          # promting the user to selec an option

        if(user.lower() == 'y'):                                                                # validating the input

                acc = int(input('\nWith how much (km/h)> '))                                    # promting the user to enter a value
                car.accelerate(acc)                                                             # calling the accelerate() method

                if(car.get_current_speed() > 400):                                              # validating the current speed

                    car.set_current_speed_acc()                                                 # calling the get_current_speed_acc() method
                    car.get_speed()                                                             # printing the result
                    print('\nThe car`s reached it`s maximum speed. Try to slow down!')

                else:

                    car.get_speed()                                                             # printing the result

        elif(user.lower() == 'n'):

            
            br = int(input('\nWith how much the car is slowing down (km/h)> '))                 # promting the user to enter a value
            car.brake(br)
            
            if(car.get_current_speed() <= 0):                                                   # validating the input

                car.set_current_speed_br()                                                      # calling the set_current_speed_br() method
                car.get_speed()                                                                 # printing the result
                print('The car`s stopped. No where to slow more!')

            else:

                car.get_speed()                                                                 # printing the result

        elif(user.lower() == 0):

            break;                                                                              # breaking out of the loop

        elif(user.lower() != 'y' and user.lower() != 'n' and user.lower() != '0'):

            print('\nInvalid input. Try again\n')                                               # printing a message if invalid input



    print('\nThe program has ended!\n')                                                         # printing a message indicating the end of the program
   

main()


