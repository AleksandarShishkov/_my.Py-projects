



import Car                                                                                      


def main():


    user = 'y'                                                                                  

    car = Car.Car(2010, 'Audi')                                                                 

    car.get_speed()                                                                             
    while(user.lower() != '0'):                                                                 

        user = input('\nIs the car accelerating (y/n or 0 to quit)> ')                          

        if(user.lower() == 'y'):                                                                
                acc = int(input('\nWith how much (km/h)> '))                                    
                car.accelerate(acc)                                                             

                if(car.get_current_speed() > 400):                                              

                    car.set_current_speed_acc()                                                 
                    car.get_speed()                                                             
                    print('\nThe car`s reached it`s maximum speed. Try to slow down!')

                else:

                    car.get_speed()                                                             

        elif(user.lower() == 'n'):

            
            br = int(input('\nWith how much the car is slowing down (km/h)> '))                 
            car.brake(br)
            
            if(car.get_current_speed() <= 0):                                                   

                car.set_current_speed_br()                                                      
                car.get_speed()                                                                 
                print('The car`s stopped. No where to slow more!')

            else:

                car.get_speed()                                                                 

        elif(user.lower() == 0):

            break;                                                                              

        elif(user.lower() != 'y' and user.lower() != 'n' and user.lower() != '0'):

            print('\nInvalid input. Try again\n')                                               



    print('\nThe program has ended!\n')                                                         
   

main()


