



class Players():                                                                                    # class Players



    def __init__(self):                                                                             # default constructor

        self.__name_pl1 = ' '                                                                       # string ro hold pl1`s name
        self.__name_pl2 = ' '                                                                       # string to hold pl2`s name
        self.__who_first = 0                                                                        # an integer to hold who will begin first
        self.__score_pl1 = 0                                                                        # an integer to hold pl1`s score
        self.__score_pl2 = 0                                                                        # an integer to hold pl2`s score
        self.__ans_pl1 = 0                                                                          # an integer to hold pl1`s answer
        self.__ans_pl2 = 0                                                                          # an integer to hold pl2`s answer



    def set_names(self):                                                                            # setter for the names
                
        self.__name_pl1 = input('\nPlayer 1 enter your name> ')                                     # prompting the user to enter pl1`s name
        self.__name_pl2 = input('Player 2 enter your name> ')                                       # promting the user to enter pl2`s name

        while(self.__name_pl2 == self.__name_pl1):                                                  # validating the input for pl2`s name

            print('Invalid name selected!')
            self.__name_pl2 = input('Player 2 enter your name> ')




    def get_name_pl1(self):                                                                         # getter for pl1`s name

        return self.__name_pl1                                                                      # returning the name



    def get_name_pl2(self):                                                                         # getter for pl2`s name

        return self.__name_pl2                                                                      # returning the name




    def set_who_first(self):                                                                        # setter for who will begin first

        print('\nWho will begin first (1 for pl1 / 2 for pl2)', end = '')                           # promting the user for an input
        self.__who_first = int(input('> '))
        
        while(self.__who_first < 1 or self.__who_first > 2):                                        # validating the input

            print('Invalid input. Try again (1 for pl1 / 2 for pl2)', end = '')
            self.__who_first = int(input('> '))



    def get_who_first(self):                                                                        # getter for who will begin first

        return self.__who_first                                                                     # returning the input



    def set_score_pl1(self):                                                                        # setter for pl1`s score

        self.__score_pl1 += 1                                                                       # adding 1 to pl1`s current score



    def set_score_pl2(self):                                                                        # setter for pl2`s score

        self.__score_pl2 += 1                                                                       # adding 1 to pl2`s current score



    def get_score_pl1(self):                                                                        # getter for pl1`s score

        return self.__score_pl1                                                                     # returning the score


    def get_score_pl2(self):                                                                        # getter for pl2`s score

        return self.__score_pl2                                                                     # returning the score

      

    def set_ans_pl1(self):                                                                          # setter for pl1`s answer

        self.__ans_pl1 = int(input('\n\t>'))                                                        # promting the user to enter integer input

        while(self.__ans_pl1 < 1 or self.__ans_pl1 > 5):                                            # validating the input

            print('\nIncorrect option. Try again')
            self.__ans_pl1 = int(input('\t> '))

        

    def set_ans_pl2(self):                                                                          # setter for pl2`s answer

        self.__ans_pl2 = int(input('\n\t>'))                                                        # promting the user to enter an integer input

        while(self.__ans_pl2 < 1 or self.__ans_pl2 > 5):

            print('\nIncorrect option. Try again')
            self.__ans_pl2 = int(input('\t> '))


    def get_ans_pl1(self):                                                                          # getter for pl1`s answer

        return self.__ans_pl1                                                                       # returning the answer


    def get_ans_pl2(self):                                                                          # getter for pl2`s answer

        return self.__ans_pl2                                                                       # returning the answer



