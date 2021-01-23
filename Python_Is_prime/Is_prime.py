



def prime(num):                                                                                     # defining the prime() method with an argument
                                                                                                    # for the number

    if (num > 1):                                                                                   # validating the input

        for i in range(2, num):

            if(num % i == 0):

                print("'", num, "' is not a prime number")                                          # printing a message indicating that the number isn`t
                                                                                                    # prime since divisable not only by 1 and itself

                break;                                                                              # breaking out of the loop

            else:
               
                print("'", num, "' is a prime number")                                              # printing a message indicating that the number is
                                                                                                    # prime

                break;                                                                              # breaking out of the loop

    else:

        print("'", num, "' is not a prime number")                                                  # printing a message if the number is less than 1




