
import random                                                   # importing the random module




def main():                                                     # definition of main() function

    showMessage()                                               # calling showMessage() function

    newGame = True

    while(newGame):


        choice = showMenu()                                     # an int to hold the returned from the showMenu() function value
        reply, num1, num2 = getData(choice)                     # assigning the value from getData() function to reply, num1 and num2
        validateReply(reply, num1, num2, choice)                # calling validateReply() function
        nreGame = nextTry()



def showMessage():                                              # showMessage() function which prints the message on the top of the program

    print("\n This is a math quiz. You are about to " \
        "be shown two integers. Guess the outcome\n\n")



def showMenu():                                                 # showMenu() function to display menu and returns selected operation or exit

    print("\n\tMENU")
    print("\nSelect between the following : ")
    print("1 - addition")
    print("2 - substraction")
    print("3 - multiplication")
    print("4 - division")
    print("5 - exit")

    choice = int(input("\nEnter your choice> "))                # prompting the user to enter the choice

    while(choice < 1 and choice > 5):                           # validation of the input
        print("\nInvalid choice. Try again (1 - 5)> ")
        choice = int()

    return choice                                               # returning the value




def getData(choice):                                            # getData() function with 1 parameter for the selected arithmetic operation


    
    num1 = random.randrange(1, 100)                             # randomizing the first integer
    num2 = random.randrange(1, 100)                             # randomizing the second integer

                                                                # an if-elif-else statement for choice selection
    if(choice == 1):
        print("\n\t", num1)
        print("\t+")
        print("\t", num2, '\n')

        reply = int(input("\nEnter your answer whenever ready> "))
    elif(choice == 2):
        print("\n\t", num1)
        print("\t-")
        print("\t", num2, '\n')

        reply = int(input("\nEnter your answer whenever ready> "))
    elif(choice == 3):
        print("\n\t", num1)
        print("\t*")
        print("\t", num2, '\n')

        reply = int(input("\nEnter your answer whenever ready> "))
    elif(choice == 4):
        print("\n\t", num1)
        print("\t/")
        print("\t", num2, '\n')

        reply = float(input("\nEnter your answer whenever ready> "))
    else:
        print("\nYou`ve exited the program!\n")
        exit(0)

    return reply, num1, num2                                    # returntning three values



def validateReply(reply, num1, num2, choice):                   # validateReply() function to validate the reply


    if(choice == 1):
        if(reply == (num1 + num2)):
            print("\nCongrats. This is the correct answer!\n")
        else:
            print("\nThe correct answer is ", num1 + num2, ". Better luck next time!\n")
    elif(choice == 2):
        if(reply == (num1 - num2)):
            print("\nCongrats. This is the correct answer!\n")
        else:
            print("\nThe correct answer is ", num1 - num2, ". Better luck next time!\n")
    elif(choice == 3):
         if(reply == (num1 * num2)):
            print("\nCongrats. This is the correct answer!\n")
         else:
            print("\nThe correct answer is ", num1 * num2, ". Better luck next time!\n")
    elif(choice == 4):
         if(reply == (format(num1 / num2), '.2f')):
            print("\nCongrats. This is the correct answer!\n")
         else:
            print("\nThe correct answer is ", format(num1 / num2, '.2f'), ". Better luck next time!\n")

    


def nextTry():                                                  # prompting the user to choose whether to try again

    nextTry = True

    next = input("\nAnother try (y/n) : ")
    while(next != 'y' and next != 'n'):
        next = input("\nInvalid input. Try again (y/n) : ")

    if(next == 'y'):
        nextTry = True
    else:
        print("\nYou`ve exited the program!\n")
        nextTry = False


    return nextTry




main()                                                          # calling the main function


