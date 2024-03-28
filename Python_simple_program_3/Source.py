
def main():                                                                                 

    print('\n\tThis program will calculate the monthly and the yearly expenses \n\tfor an automobile\n')

    loan = float(input('\nEnter the monthly loan expenses > $'))                            
    insurance = float(input('Enter the monthly insurance expenses > $'))                    
    gas = float(input('Enter the monthly expenses for gas > $'))                            
    oil = float(input('Enter the monthly expenses for the oil > $'))                        
    tires = float(input('Enter the montly expenses for the tires > $'))                     
    maintenance = float(input('Enter the monthly expenses for the maintenance > $'))        



    message()                                                                               
    total_monthly_expenses(loan, insurance, gas, oil, tires, maintenance)                   
    total_yearly_expenses(loan, insurance, gas, oil, tires, maintenance)                    




def message():                                                                              
    print("\nPress 'Enter' to sum the totals : ")

def total_monthly_expenses(_loan, _insurance, _gas, _oil, _tires, _maintenance):             
    
    total_m = _loan + _insurance + _gas + _oil + _tires + _maintenance

    print('\n\tThe monthly total is: $', format(total_m, ',.2f'), sep='')


def total_yearly_expenses(_loan, _insurance, _gas, _oil, _tires, _maintenance):              
                                                                                            
    total_y = (_loan + _insurance + _gas + _oil + _tires + _maintenance) * 12

    print('\tThe yearly total is: $', format(total_y, ',.2f'), sep='')
    print('\n')




main()                                                                                      

