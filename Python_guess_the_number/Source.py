

# ------------------------------------------------------------  # 
# This Python program simulates a game of guessing numbers.     #
# It prompts the user to enter an integer, validates the input  #
# and returns a message indicating whether the number`s been    #
# guessed or not. The program keeps running total for the score.#
#                                                               #
# For randomizing the number is used the random module. It`s    #
# applience can be located int PC_num.py file.                  #
#                                                               #
# Enjoy the game and try to reach 100 points . . .              #
#                                                               #
# ------------------------------------------------------------  #





import Message                                                                      # importing Message.py
import PC_num                                                                       # importing PC_num.py
import User                                                                         # inporting User.py
import NewGame                                                                      # importing NewGame.py
import TotalScore                                                                   # importing TotalScore.py


def main():                                                                         # defining main() function

    
    score = 0                                                                       # an integer to hold the score
    attempt = 0                                                                     # an integer to hold the number of attempts
    
    newgame = True                                                                  # a boolean that is set to True
    Message.showMessage()                                                           # calling showMessage() function
    
    while (newgame):                                                                # entering the outer game loop
        
        pc_number = PC_num.pc_num()                                                 # assigning the pc_num() to pc_number variable
        user_number = User.user_input()                                             # assigning user_input() to user_number variable

        while (user_number != pc_number):                                           # entering the inner game loop


            if(user_number == 0):                                                   # validating the users input
                print('\n\n\tYou have left the game. . . Better luck next time!\n')
                exit(0)                                                             # exiting the program if the number '0' is entered

            elif(user_number > pc_number):
                print('\tTry lower!\n')
                attempt += 1                                                        # adding 1 to attempt
                user_number = User.user_input()                                     # prompting the user for an input
                
            
            elif(user_number < pc_number):
                print('\tTry higher!\n')
                attempt += 1                                                        # adding 1 to attempt
                user_number = User.user_input()                                     # prompting the user for an input
               
            
                                                                                    # exiting the inner game loop
        print('\n\tCongratulations. You have '\
            'guessed the number!\n')
        
        if(attempt < 3):                                                            # validating the number of attempts
            score += 3                                                              # adding 3 to score if the validation is True
            print('\tYour score is ', score, '\n')                                  # validating the score
            TotalScore.totalScore(score)
        else:
            score += 1                                                              # adding 1 to score if validation is False
            print('\tYour score is ', score, '\n')
            TotalScore.totalScore(score)                                            # validating the score
              

        attempt = 0                                                                 # assigning 0 to attempt

        newgame = NewGame.new_game()                                                # promting the user for an input

                                                                                    # exiting the outer gmae loop
                


main()                                                                              # calling the main() function

