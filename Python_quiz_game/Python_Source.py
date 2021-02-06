


                # This Python program simulates a quiz game.
                # It it splayed by two players, the first to
                # reach 5 points wins the game.
                # 
                # The program then promts the user to select
                # whether new game will be loaded. If not
                # the program terminates.




import message                                                                                          # importing the message module
import Question                                                                                         # importing the Question class
import Players                                                                                          # importing the Players class



def main():


    message.message()                                                                                   # calling the message() method

    q = Question.Question()                                                                             # an instance of the Question class
    pl = Players.Players()                                                                              # an isnace of the Players class

    newGame = True                                                                                      # a boolean to control the outer game loop


    try:                                                                                                # try clause to check for exceptions

        while(newGame):                                                                                 

            pl.set_names()                                                                              # calling the set_names() method

            pl.set_who_first();                                                                         # calling the set_who_first() method

            q.set_questions_pl1()                                                                       # setting the questions for pl1
            q.set_answers_pl1()                                                                         # setting the answers for pl1
            q.set_questions_pl2()                                                                       # setting the questions for pl2
            q.set_answers_pl2()                                                                         # setting the answers for pl2

            q.set_keys_pl1()                                                                            # setting the keys for pl1
            q.set_keys_pl2()                                                                            # setting the keys for pl2
    
            questions_pl1 = q.get_questions_pl1()                                                       # a variable to hold the questions dict for pl1
            answers_pl1 = q.get_answers_pl1()                                                           # a variable to hold the answers dict for pl1
            questions_pl2 = q.get_questions_pl2()                                                       # a variable to hold the questions dict for pl2
            answers_pl2 = q.get_answers_pl2()                                                           # a variable to hold the answers dict for pl2                   
    
            count_max = 6                                                                               # a variable to hold the max count for the disctionaries
        
            while(pl.get_score_pl1() != 5 or pl.get_score_pl2() != 5):                                  # sentinel controlled inner game loop
    

                count = q.get_count()                                                                   # a variable to hold the count

            


                if(pl.get_who_first() == 1):                                                            # validating who will begin first


                    if(count in questions_pl1):                                                         # validating the key

                        print("\n'", pl.get_name_pl1(), "' answer the question...\n")
                        print(questions_pl1[count])                                                     # printing the question
                        print(answers_pl1[count])                                                       # printing the options

                        pl.set_ans_pl1()                                                                # promting the user to enter an option

                
                        if(pl.get_ans_pl1() != q.get_keys_pl1(count)):                                  # validating the input

                            print('\nIncorrect answer. Better luck next time!')
                            print("'", pl.get_name_pl1(), "' points: ", pl.get_score_pl1(), '\n')

                        else:

                            pl.set_score_pl1()                                                          # adding 1 to the total score for pl1

                            print('The correct answer is: ', pl.get_ans_pl1(), ' You`ve gained a point!\n')
                            print("'", pl.get_name_pl1(), "' points: ", pl.get_score_pl1(), '\n')

                            if(pl.get_score_pl1() == 5):                                                # validating the number of points earned
                                break

                            q.if_correct_answer_pl1(count)                                              # setting the dictionaries with the correct amount of keys
                    
                

                    if(count in questions_pl2):                                                         # validating the key


                        print("\n'", pl.get_name_pl2(), "' answer the question...\n")
                        print(questions_pl2[count])                                                     # printing the question                    
                        print(answers_pl2[count])                                                       # printing the options
                                                                                                        # promting the user to select an option
                        pl.set_ans_pl2()

                
                        if(pl.get_ans_pl2() != q.get_keys_pl2(count)):
                            print('\nIncorrect answer. Better luck next time!')
                            print("'", pl.get_name_pl2(), "' points: ", pl.get_score_pl2(), '\n')

                        else:

                            pl.set_score_pl2()                                                          # adding 1 to the total score for pl2

                            print('The correct answer is: ', pl.get_ans_pl2(), '. You`ve gained a point!\n')
                            print("'", pl.get_name_pl2(), "' points: ", pl.get_score_pl2(), '\n')

                            if(pl.get_score_pl2() == 5):                                                # validating the number of points earned
                                break

                            q.if_correct_answer_pl2(count)                                              # setting the dictionaries with the correct amount of keys
                    
        


                else:

                    if(count in questions_pl2):                                                         # validating the key

                        print("\n'", pl.get_name_pl2(), "' answer the question...\n")
                        print(questions_pl2[count])                                                     # printing the question
                        print(answers_pl2[count])                                                       # printing the option

                        pl.set_ans_pl2()                                                                # prompting the user to select an option

                        if(pl.get_ans_pl2() != q.get_keys_pl2(count)):
                            print('\nIncorrect answer. Better luck next time!')
                            print("'", pl.get_name_pl2(), "' points: ", pl.get_score_pl2(), '\n')

                        else:

                            pl.set_score_pl2()                                                          # adding 1 to the total score for pl2

                            print('The correct answer is: ', pl.get_ans_pl2(), '. You`ve gained a point!\n')
                            print("'", pl.get_name_pl2(), "' points: ", pl.get_score_pl2(), '\n')

                            if(pl.get_score_pl2() == 5):                                                # validating the number of points earned
                                break

                            q.if_correct_answer_pl2(count)                                              # setting the dictionarie swith the correct amount of keys
                    


                    if(count in questions_pl1):                                                         # validating the key
            
                        print("\n'", pl.get_name_pl1(), "' answer the question...\n")
                        print(questions_pl1[count])                                                     # printing the question
                        print(answers_pl1[count])                                                       # printing the option

                        pl.set_ans_pl1()                                                                # promting the user to select an option

                        if(pl.get_ans_pl1() != q.get_keys_pl1(count)):                                  # validating the input     

                            print('\nIncorrect answer. Better luck next time!')
                            print("'", pl.get_name_pl1(), "' points: ", pl.get_score_pl1(), '\n')

                        else:

                            pl.set_score_pl1()                                                          # adding 1 to the total score for player1

                            print('The correct answer is: ', pl.get_ans_pl1(), '. You`ve gained a point!\n')
                            print("'", pl.get_name_pl1(), "' points: ", pl.get_score_pl1(), '\n')

                            if(pl.get_score_pl1() == 5):                                                # validating the number of points earned
                                break

                            q.if_correct_answer_pl1(count)                                              # setting the dictionaries with the correct amount of keys
                    




                q.set_count()                                                                           # adding one to count


                if(count == count_max):                                                                 # validating the count

                    q.null_count()                                                                      # re-setting the counter if counter = 6

                    
                print('\n')



            if(pl.get_score_pl1() == 5):                                                                # validating the winner, printing a message

                print("'", pl.get_name_pl1(), "' has won the game! Congrats!\n")                        

            else:

                print("'", pl.get_name_pl2(), "' has won the game! Congrats!\n")


            anotherGame = input('New game? (y/n)> ')                                                    # promting the user to select new game

            while(anotherGame != 'y' and anotherGame != 'n'):                                           # validating the input

                print('\nInvalid input. Try again> ')
                anotherGame = input('(y/n)> ')

            if(anotherGame == 'y'):
                print("\nYou`ve selected another game.\n")
                newGame = True                                                                          # setting newGame to true

            else:

                print('\nThe program has ended!\n')                                                     # printing a message indicating that the program has ended
                newGame = False                                                                         # setting newGame to fale




    except:                                                                                             # an except clause to catch exceptions

        print('\nAn error has occurred!\n')                                                             # printing an erroneus message




main()




