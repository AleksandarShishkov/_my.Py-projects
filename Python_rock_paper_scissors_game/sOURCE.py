
import PC_choice                                                                    
import ShowMessage                                                                  
import User                                                                         
import NewGame                                                                      
import ValidateScore                                                                



def main():                                                                         

    score_pl = 0;                                                                   
    score_pc = 0;                                                                   
    total_score_pl = 0                                                              
    total_score_pc = 0                                                              

    ShowMessage.show_message()                                                      
    game_play = True                                                                

    while(game_play):                                                               

        pc = PC_choice.pc_input()                                                   
        pl = User.user_input()                                                      

        if(pl == 0):                                                                
            print('\nThe program has ended. Better luck next time!\n\n')
            exit(0)                                                                 
        elif(pl == 1 and pc == 3):
            print("\nYou have selected 'rock'.")
            print("\nThe PC has selected 'scissors'. The 'rock' wins.\n")
            score_pl += 1                                                           
            if(score_pl == 10):                                                     
                ValidateScore.score_validation_pl(score_pl)                         
                score_pl = 0                                                        
                score_pc = 0                                                        
                total_score_pl += 1                                                 
                game_play = NewGame.new_game()                                      
            else:
                ValidateScore.score_validation_pl(score_pl)                         
                ValidateScore.score_validation_pc(score_pc)                         
        elif(pl == 3 and pc == 2):
            print("\nYou have selected 'scissors'.")
            print("\nThe PC has selected 'paper'. The 'scissors' win.\n")
            score_pl += 1                                                           
            if(score_pl == 10):                                                     
                ValidateScore.score_validation_pl(score_pl)                         
                score_pl = 0                                                        
                score_pc = 0                                                        
                total_score_pl += 1                                                 
                game_play = NewGame.new_game()                                                                           
            else:
                ValidateScore.score_validation_pl(score_pl)                           
                ValidateScore.score_validation_pc(score_pc)                         
        elif(pl == 2 and pc == 1):
            print("\nYou have selected 'paper'.")
            print("\nThe PC has selected 'rock'. The 'paper' wins.\n")
            score_pl += 1                                                           
            if(score_pl == 10):                                                     
                ValidateScore.score_validation_pl(score_pl)
                score_pl = 0                                                        
                score_pc = 0                                                        
                total_score_pl += 1                                                 
                game_play = NewGame.new_game()                                      
            else:
                ValidateScore.score_validation_pl(score_pl)                          
                ValidateScore.score_validation_pc(score_pc)                         
        elif(pl == 3 and pc == 1):
            print("\nYou have selected 'scissors'.")
            print("\nThe PC has selected 'rock'. The 'rock' wins.\n")
            score_pc += 1                                                           
            if(score_pc == 10):                                                     
                ValidateScore.score_validation_pc(score_pc)
                score_pl = 0                                                        
                score_pc = 0                                                        
                total_score_pc += 1                                                 
                game_play = NewGame.new_game()                                      
            else:
                ValidateScore.score_validation_pl(score_pl)                         
                ValidateScore.score_validation_pc(score_pc)                         
        elif(pl == 2 and pc == 3):
            print("\nYou have selected 'paper'.")
            print("\nThe PC has selected 'scissors'. The 'scissors' win.\n")
            score_pc += 1                                                           
            if(score_pc == 10):                                                     
                ValidateScore.score_validation_pc(score_pc)
                score_pl = 0                                                        
                score_pc = 0                                                        
                total_score_pc += 1                                                 
                game_play = NewGame.new_game()                                      
            else:
                ValidateScore.score_validation_pl(score_pl)                         
                ValidateScore.score_validation_pc(score_pc)
        elif(pl == 1 and pc == 2):
            print("\nYou have selected 'rock'.")
            print("\nThe PC has selected 'paper'. The 'paper' wins")
            score_pc += 1                                                           
            if(score_pc == 10):                                                     
                ValidateScore.score_validation_pc(score_pc)
                score_pl = 0                                                        
                score_pc = 0                                                        
                total_score_pc += 1                                                 
                game_play = NewGame.new_game()                                      
            else:
                ValidateScore.score_validation_pl(score_pl)                         
                ValidateScore.score_validation_pc(score_pc)                         
        elif(pl == 1 and pc == 1):
            print("\nThe PC has selected 'rock'. Draw!\n")
        elif(pl == 2 and pc == 2):
            print("\nThe PC has selected 'paper'. Darw!\n")
        elif(pl == 3 and pc == 3):
            print("\nThe PC has selected 'scissors'. Draw!\n")
            
                                                                                    
    print('\nThe program has ended. Overall result: \n\n'\
        'Player: ', total_score_pl, '\n'\
        'PC:     ', total_score_pc, '\n')


main()                                                                              

