

#This program calculates the monthly and yearly costs for 
#maintening an automobile


def main():                                                                                 # main function definition

    print('\n\tThis program will calculate the monthly and the yearly expenses \n\tfor an automobile\n')

    loan = float(input('\nEnter the monthly loan expenses > $'))                            # a float holding the amount for the loan expences
    insurance = float(input('Enter the monthly insurance expenses > $'))                    # a float holding the amount for the insurance
    gas = float(input('Enter the monthly expenses for gas > $'))                            # a float holding the amount for the gas
    oil = float(input('Enter the monthly expenses for the oil > $'))                        # a float holding the amount for the oil
    tires = float(input('Enter the montly expenses for the tires > $'))                     # a float holding the amount for the tires
    maintenance = float(input('Enter the monthly expenses for the maintenance > $'))        # a float holding the amount for the maintenance



    message()                                                                               # calling message()
    total_monthly_expenses(loan, insurance, gas, oil, tires, maintenance)                   # calling total_monthly_expenses()
    total_yearly_expenses(loan, insurance, gas, oil, tires, maintenance)                    # calling total_yearly_expenses()




def message():                                                                              # a function to print the message
    print("\nPress 'Enter' to sum the totals : ")

def total_monthly_expenses(_loan, _insurance, _gas, _oil, _tires, _maintenance):            # a function to sum the expenses 
    
    total_m = _loan + _insurance + _gas + _oil + _tires + _maintenance

    print('\n\tThe monthly total is: $', format(total_m, ',.2f'), sep='')


def total_yearly_expenses(_loan, _insurance, _gas, _oil, _tires, _maintenance):             # a function to to multiply the sum of the expenses by 12 - 
                                                                                            # (for the months in 1 year of time)
    total_y = (_loan + _insurance + _gas + _oil + _tires + _maintenance) * 12

    print('\tThe yearly total is: $', format(total_y, ',.2f'), sep='')
    print('\n')




main()                                                                                      # running the main()



