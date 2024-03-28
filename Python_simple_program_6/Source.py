
def main():                                                 

    days = int(input("\nEnter the number of the days >"))   

    calcAmount(days)                                        


def calcAmount(days):                                       

    total = 1;                                              

    for x in range(1, days + 1):                            

        total *= x                                          



    total /= 100                                             
                                                            


                                                            
    print("\nThe total amount earned for ", days, \
          " days is $", format(total, ',.2f'), sep='')



main()                                                      
