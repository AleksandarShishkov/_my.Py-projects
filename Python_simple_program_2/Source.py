

tax_county = 0.02
tax_state = 0.04


def main():

    message()

    amount = float(input('\nWhat is the amount? > $'))

    input("\nPress 'Enter' to calculate the taxes > ")

    county_tax(amount)
    state_tax(amount)
    total_tax(amount)



def county_tax(var):

    tax = var * tax_county
    print('\nThe county tax is: $',format(tax, '.2f'), sep='')


def state_tax(var):

    tax = var * tax_state
    print('The state tax is: $', format(tax, '.2f'), sep='')



def total_tax(var):

    total = (var * tax_county) + (var * tax_state)
    print('The total tax payed is: $', format(total, '.2f'), sep='')
    print('\n')



def message():
    print('\n\tThis program will calculate the taxes for a certain amount inputed by the user.')
    


main()


