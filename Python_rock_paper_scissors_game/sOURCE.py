





        # This Python program simulates a game of Rock-Paper-Scissors.     
        # It prompts the user to select an option from a menu and validates
        # the input. It also keeps running total for the score of both player
        # and pc.
         
        # The pc is selecting options 1 - 3 randomly.    
                
        # The winner is the furst to make 10 points




import PC_choice                                                                    # importing PC_choice.py
import ShowMessage                                                                  # importing ShowMessage.py
import User                                                                         # importing User.py
import NewGame                                                                      # importing NewGame.py
import ValidateScore                                                                # inporting ValidationScore.py



def main():                                                                         # defining main() function


    score_pl = 0;                                                                   # an integer to hold the pl`s current score
    score_pc = 0;                                                                   # an integer to hold the pc`s current score
    total_score_pl = 0                                                              # an integer to hold the pl`s total score
    total_score_pc = 0                                                              # an integer to hold the pc`s total score

    ShowMessage.show_message()                                                      # calling show_message() function
    game_play = True                                                                # a boolean to hold True or False for the game-loop`s validation

    while(game_play):                                                               # entering the game-loop

        pc = PC_choice.pc_input()                                                   # assigning pc_input() to pc
        pl = User.user_input()                                                      # assigning user_input() to pl

        if(pl == 0):                                                                # validating the input
            print('\nThe program has ended. Better luck next time!\n\n')
            exit(0)                                                                 # exiting the program if the user selects '0'
        elif(pl == 1 and pc == 3):
            print("\nYou have selected 'rock'.")
            print("\nThe PC has selected 'scissors'. The 'rock' wins.\n")
            score_pl += 1                                                           # adding 1 to pl`s current score
            if(score_pl == 10):                                                     # validating the score
                ValidateScore.score_validation_pl(score_pl)                         
                score_pl = 0                                                        # re-setting the score_pl variable
                score_pc = 0                                                        # re-setting the score_pc variable
                total_score_pl += 1                                                 # adding 1 to the total_score_pl
                game_play = NewGame.new_game()                                      # calling new_game()
            else:
                ValidateScore.score_validation_pl(score_pl)                         # calling score_validation_pl(), passing score_pl as an argument
                ValidateScore.score_validation_pc(score_pc)                         # calling score_validation_pc(), assing score_pc as an argument
        elif(pl == 3 and pc == 2):
            print("\nYou have selected 'scissors'.")
            print("\nThe PC has selected 'paper'. The 'scissors' win.\n")
            score_pl += 1                                                           # adding 1 to pl`s current score
            if(score_pl == 10):                                                     # validating the score
                ValidateScore.score_validation_pl(score_pl)                         
                score_pl = 0                                                        # re-setting the score_pl variable
                score_pc = 0                                                        # re-setting the score_pc variable
                total_score_pl += 1                                                 # adding 1 to the total_score_pl
                game_play = NewGame.new_game()                                      # calling new_game()                                     
            else:
                ValidateScore.score_validation_pl(score_pl)                         # calling score_validation_pl(), passing score_pl as an argument  
                ValidateScore.score_validation_pc(score_pc)                         # calling score_validation_pc(), passing score_pc as an argument
        elif(pl == 2 and pc == 1):
            print("\nYou have selected 'paper'.")
            print("\nThe PC has selected 'rock'. The 'paper' wins.\n")
            score_pl += 1                                                           # adding 1 to pl`s current score
            if(score_pl == 10):                                                     # validating the score
                ValidateScore.score_validation_pl(score_pl)
                score_pl = 0                                                        # re-setting the score_pl variable
                score_pc = 0                                                        # re-setting the score_pc variable
                total_score_pl += 1                                                 # adding 1 to the total_score_pl
                game_play = NewGame.new_game()                                      # calling new_game()
            else:
                ValidateScore.score_validation_pl(score_pl)                         # calling score_validation_pl(), passing score_pl as an argument 
                ValidateScore.score_validation_pc(score_pc)                         # calling score_validation_pc(), passing score_pc as an argument
        elif(pl == 3 and pc == 1):
            print("\nYou have selected 'scissors'.")
            print("\nThe PC has selected 'rock'. The 'rock' wins.\n")
            score_pc += 1                                                           # adding 1 to pc`s current score
            if(score_pc == 10):                                                     # validating the score
                ValidateScore.score_validation_pc(score_pc)
                score_pl = 0                                                        # re-setting the score_pl variable
                score_pc = 0                                                        # re-setting the score_pc variable
                total_score_pc += 1                                                 # adding 1 to the total_score_pc
                game_play = NewGame.new_game()                                      # calling new_game()
            else:
                ValidateScore.score_validation_pl(score_pl)                         # calling score_validation_pl(), passing score_pl as an argument
                ValidateScore.score_validation_pc(score_pc)                         # calling score_validation_pc(), passing score_pc as an argument
        elif(pl == 2 and pc == 3):
            print("\nYou have selected 'paper'.")
            print("\nThe PC has selected 'scissors'. The 'scissors' win.\n")
            score_pc += 1                                                           # adding 1 to pc`s current score
            if(score_pc == 10):                                                     # validating the score
                ValidateScore.score_validation_pc(score_pc)
                score_pl = 0                                                        # re-setting the score_pl variable
                score_pc = 0                                                        # re-setting the score_pc variable
                total_score_pc += 1                                                 # adding 1 to the total_score_pc
                game_play = NewGame.new_game()                                      # calling new_game()
            else:
                ValidateScore.score_validation_pl(score_pl)                         # calling score_validation_pl(), passing score_pl as an argument
                ValidateScore.score_validation_pc(score_pc)                         # calling score_validation_pc(), passing score_pc as an argument
        elif(pl == 1 and pc == 2):
            print("\nYou have selected 'rock'.")
            print("\nThe PC has selected 'paper'. The 'paper' wins")
            score_pc += 1                                                           # adding 1 to pc`s current score
            if(score_pc == 10):                                                     # validating the score
                ValidateScore.score_validation_pc(score_pc)
                score_pl = 0                                                        # re-setting the score_pl variable
                score_pc = 0                                                        # re-setting the score_pc variable
                total_score_pc += 1                                                 # adding 1 to the total_score_pc
                game_play = NewGame.new_game()                                      # calling new_game()
            else:
                ValidateScore.score_validation_pl(score_pl)                         # calling score_validation_pl(), passing score_pl as an argument
                ValidateScore.score_validation_pc(score_pc)                         # calling score_validation_pc(), passing score_pc as an argument
        elif(pl == 1 and pc == 1):
            print("\nThe PC has selected 'rock'. Draw!\n")
        elif(pl == 2 and pc == 2):
            print("\nThe PC has selected 'paper'. Darw!\n")
        elif(pl == 3 and pc == 3):
            print("\nThe PC has selected 'scissors'. Draw!\n")
            
                                                                                     # exiting the game-loop, printing the total score
    print('\nThe program has ended. Overall result: \n\n'\
        'Player: ', total_score_pl, '\n'\
        'PC:     ', total_score_pc, '\n')


main()                                                                               # calling main()

