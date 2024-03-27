

import message                                                                                          
import Question                                                                                         
import Players                                                                                          



def main():


    message.message()                                                                                   

    q = Question.Question()                                                                             
    pl = Players.Players()                                                                              

    newGame = True                                                                                      


    try:                                                                                                

        while(newGame):                                                                                 

            pl.set_names()                                                                              

            pl.set_who_first();                                                                         

            q.set_questions_pl1()                                                                       
            q.set_answers_pl1()                                                                         
            q.set_questions_pl2()                                                                       
            q.set_answers_pl2()                                                                         

            q.set_keys_pl1()                                                                            
            q.set_keys_pl2()                                                                            
    
            questions_pl1 = q.get_questions_pl1()                                                       
            answers_pl1 = q.get_answers_pl1()                                                           
            questions_pl2 = q.get_questions_pl2()                                                       
            answers_pl2 = q.get_answers_pl2()                                                                              
    
            count_max = 6                                                                               
        
            while(pl.get_score_pl1() != 5 or pl.get_score_pl2() != 5):                                  
    

                count = q.get_count()                                                                   

            


                if(pl.get_who_first() == 1):                                                            


                    if(count in questions_pl1):                                                         

                        print("\n'", pl.get_name_pl1(), "' answer the question...\n")
                        print(questions_pl1[count])                                                     
                        print(answers_pl1[count])                                                       

                        pl.set_ans_pl1()                                                                

                
                        if(pl.get_ans_pl1() != q.get_keys_pl1(count)):                                  

                            print('\nIncorrect answer. Better luck next time!')
                            print("'", pl.get_name_pl1(), "' points: ", pl.get_score_pl1(), '\n')

                        else:

                            pl.set_score_pl1()                                                          

                            print('The correct answer is: ', pl.get_ans_pl1(), ' You`ve gained a point!\n')
                            print("'", pl.get_name_pl1(), "' points: ", pl.get_score_pl1(), '\n')

                            if(pl.get_score_pl1() == 5):                                                
                                break

                            q.if_correct_answer_pl1(count)                                              
                    
                

                    if(count in questions_pl2):                                                         


                        print("\n'", pl.get_name_pl2(), "' answer the question...\n")
                        print(questions_pl2[count])                                                                         
                        print(answers_pl2[count])                                                       
                                                                                                        
                        pl.set_ans_pl2()

                
                        if(pl.get_ans_pl2() != q.get_keys_pl2(count)):
                            print('\nIncorrect answer. Better luck next time!')
                            print("'", pl.get_name_pl2(), "' points: ", pl.get_score_pl2(), '\n')

                        else:

                            pl.set_score_pl2()                                                          

                            print('The correct answer is: ', pl.get_ans_pl2(), '. You`ve gained a point!\n')
                            print("'", pl.get_name_pl2(), "' points: ", pl.get_score_pl2(), '\n')

                            if(pl.get_score_pl2() == 5):                                                
                                break

                            q.if_correct_answer_pl2(count)                                              
                    
        


                else:

                    if(count in questions_pl2):                                                         

                        print("\n'", pl.get_name_pl2(), "' answer the question...\n")
                        print(questions_pl2[count])                                                     
                        print(answers_pl2[count])                                                       

                        pl.set_ans_pl2()                                                                

                        if(pl.get_ans_pl2() != q.get_keys_pl2(count)):
                            print('\nIncorrect answer. Better luck next time!')
                            print("'", pl.get_name_pl2(), "' points: ", pl.get_score_pl2(), '\n')

                        else:

                            pl.set_score_pl2()                                                          

                            print('The correct answer is: ', pl.get_ans_pl2(), '. You`ve gained a point!\n')
                            print("'", pl.get_name_pl2(), "' points: ", pl.get_score_pl2(), '\n')

                            if(pl.get_score_pl2() == 5):                                                
                                break

                            q.if_correct_answer_pl2(count)                                              
                    


                    if(count in questions_pl1):                                                         
            
                        print("\n'", pl.get_name_pl1(), "' answer the question...\n")
                        print(questions_pl1[count])                                                     
                        print(answers_pl1[count])                                                       

                        pl.set_ans_pl1()                                                                

                        if(pl.get_ans_pl1() != q.get_keys_pl1(count)):                                       

                            print('\nIncorrect answer. Better luck next time!')
                            print("'", pl.get_name_pl1(), "' points: ", pl.get_score_pl1(), '\n')

                        else:

                            pl.set_score_pl1()                                                          

                            print('The correct answer is: ', pl.get_ans_pl1(), '. You`ve gained a point!\n')
                            print("'", pl.get_name_pl1(), "' points: ", pl.get_score_pl1(), '\n')

                            if(pl.get_score_pl1() == 5):                                                
                                break

                            q.if_correct_answer_pl1(count)                                                                  




                q.set_count()                                                                           


                if(count == count_max):                                                                 

                    q.null_count()                                                                      

                    
                print('\n')



            if(pl.get_score_pl1() == 5):                                                                
                print("'", pl.get_name_pl1(), "' has won the game! Congrats!\n")                        

            else:

                print("'", pl.get_name_pl2(), "' has won the game! Congrats!\n")


            anotherGame = input('New game? (y/n)> ')                                                    

            while(anotherGame != 'y' and anotherGame != 'n'):                                           

                print('\nInvalid input. Try again> ')
                anotherGame = input('(y/n)> ')

            if(anotherGame == 'y'):
                print("\nYou`ve selected another game.\n")
                newGame = True                                                                          

            else:

                print('\nThe program has ended!\n')                                                     
                newGame = False                                                                         




    except:                                                                                             

        print('\nAn error has occurred!\n')                                                             




main()




