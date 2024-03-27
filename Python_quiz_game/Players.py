



class Players():                                                                                    



    def __init__(self):                                                                             
        self.__name_pl1 = ' '                                                                       
        self.__name_pl2 = ' '                                                                       
        self.__who_first = 0                                                                        
        self.__score_pl1 = 0                                                                        
        self.__score_pl2 = 0                                                                        
        self.__ans_pl1 = 0                                                                          
        self.__ans_pl2 = 0                                                                          



    def set_names(self):                                                                            
                
        self.__name_pl1 = input('\nPlayer 1 enter your name> ')                                     
        self.__name_pl2 = input('Player 2 enter your name> ')                                       

        while(self.__name_pl2 == self.__name_pl1):                                                  

            print('Invalid name selected!')
            self.__name_pl2 = input('Player 2 enter your name> ')




    def get_name_pl1(self):                                                                         

        return self.__name_pl1                                                                      


    def get_name_pl2(self):                                                                         

        return self.__name_pl2                                                                      




    def set_who_first(self):                                                                        
        print('\nWho will begin first (1 for pl1 / 2 for pl2)', end = '')                           
        self.__who_first = int(input('> '))
        
        while(self.__who_first < 1 or self.__who_first > 2):                                        

            print('Invalid input. Try again (1 for pl1 / 2 for pl2)', end = '')
            self.__who_first = int(input('> '))



    def get_who_first(self):                                                                        

        return self.__who_first                                                                     



    def set_score_pl1(self):                                                                        

        self.__score_pl1 += 1                                                                       



    def set_score_pl2(self):                                                                        

        self.__score_pl2 += 1                                                                       


    def get_score_pl1(self):                                                                        

        return self.__score_pl1                                                                     


    def get_score_pl2(self):                                                                        

        return self.__score_pl2                                                                     

      

    def set_ans_pl1(self):                                                                          

        self.__ans_pl1 = int(input('\n\t>'))                                                        
        while(self.__ans_pl1 < 1 or self.__ans_pl1 > 5):                                            

            print('\nIncorrect option. Try again')
            self.__ans_pl1 = int(input('\t> '))

        

    def set_ans_pl2(self):                                                                          

        self.__ans_pl2 = int(input('\n\t>'))                                                        

        while(self.__ans_pl2 < 1 or self.__ans_pl2 > 5):

            print('\nIncorrect option. Try again')
            self.__ans_pl2 = int(input('\t> '))


    def get_ans_pl1(self):                                                                          

        return self.__ans_pl1                                                                       


    def get_ans_pl2(self):                                                                          

        return self.__ans_pl2                                                                       



