
def main():

    message()
    classA = int(input('\nThe amount per seat in class A is $15. How many tickets were sold for this class? > '))
    classB = int(input('\nThe amount per seat in class B is $12. How many tickets were sold for this class? > '))
    classC = int(input('\nThe amount per seat in class C is $9. How many tickets were sold for this class? > '))

    calculate_amount(classA,classB,classC)

def message():
    print('\n\t   This program calculates the total income from selling tickets \n\tfor a football game. There are three types of classes:\n')

def calculate_amount(value1, value2, value3):
    
    value1 *= 15.0
    value2 *= 12.0
    value3 *= 9.0

    amount = value1 + value2 + value3

    print('\nThe total inclome is $', format(amount, ',.2f'), sep='')
    print('\n')



main()


