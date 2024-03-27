

import Message                                                                      
import PC_num                                                                       
import User                                                                         
import NewGame                                                                      
import TotalScore                                                                   


def main():                                                                         

    
    score = 0                                                                       
    attempt = 0                                                                     
    
    newgame = True                                                                  
    Message.showMessage()                                                           
    
    while (newgame):                                                                
        
        pc_number = PC_num.pc_num()                                                 
        user_number = User.user_input()                                             

        while (user_number != pc_number):                                           


            if(user_number == 0):                                                   
                print('\n\n\tYou have left the game. . . Better luck next time!\n')
                exit(0)                                                             

            elif(user_number > pc_number):
                print('\tTry lower!\n')
                attempt += 1                                                        
                user_number = User.user_input()                                     
                
            
            elif(user_number < pc_number):
                print('\tTry higher!\n')
                attempt += 1                                                        
                user_number = User.user_input()                                     
               
            
                                                                                    
        print('\n\tCongratulations. You have '\
            'guessed the number!\n')
        
        if(attempt < 3):                                                            
            score += 3                                                              
            print('\tYour score is ', score, '\n')                                  
            TotalScore.totalScore(score)
        else:
            score += 1                                                              
            print('\tYour score is ', score, '\n')
            TotalScore.totalScore(score)                                            
              

        attempt = 0                                                                 

        newgame = NewGame.new_game()                                                

                                                                                                    


main()                                                                              

