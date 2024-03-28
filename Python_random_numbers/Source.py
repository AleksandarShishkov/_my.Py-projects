
import random                                                   




def main():                                                     

    showMessage()                                               

    newGame = True

    while(newGame):


        choice = showMenu()                                     
        reply, num1, num2 = getData(choice)                     
        validateReply(reply, num1, num2, choice)                
        nreGame = nextTry()



def showMessage():                                              

    print("\n This is a math quiz. You are about to " \
        "be shown two integers. Guess the outcome\n\n")



def showMenu():                                                 

    print("\n\tMENU")
    print("\nSelect between the following : ")
    print("1 - addition")
    print("2 - substraction")
    print("3 - multiplication")
    print("4 - division")
    print("5 - exit")

    choice = int(input("\nEnter your choice> "))                

    while(choice < 1 and choice > 5):                           
        print("\nInvalid choice. Try again (1 - 5)> ")
        choice = int()

    return choice                                               




def getData(choice):                                            


    
    num1 = random.randrange(1, 100)                             
    num2 = random.randrange(1, 100)                             

                                                                
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

    return reply, num1, num2                                    


def validateReply(reply, num1, num2, choice):                   


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

    


def nextTry():                                                  

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




main()                                                          


