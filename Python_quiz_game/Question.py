



class Question():                                                                                   # class Question


    def __init__(self):                                                                             # default constructor

        self.__answer_D_pl1 = {}                                                                    # an empty disctinary for pl1`s answers
        self.__quest_D_pl1 = {}                                                                     # an empty disctionary for pl1`s questions
        self.__quest_D_pl2 = {}                                                                     # an empty dictionary for pl2`s questions
        self.__answer_D_pl2 = {}                                                                    # an empty dictionary for pl2`s answers
        self.__keys_pl1 = {}                                                                        # an empty dictionary for the pl1`s keys
        self.__keys_pl2 = {}                                                                        # an empty dictionary for the pl2`s keys
        self.__count = 1                                                                            # a counter set to 1
        
        



    def set_questions_pl1(self):                                                                    # setter for pl1`s questions                              
                                                                                                    # setting the questions in the disctionary

        self.__quest_D_pl1[1] = '\tHow many soccer players should each team have \n\ton the field at the start of each match?>'
        self.__quest_D_pl1[2] = '\tWhich Williams sister has won more \n\tGrand Slam titles?>'
        self.__quest_D_pl1[3] = '\tWhat country won the very first \n\tFIFA World Cup in 1930?>'
        self.__quest_D_pl1[4] = '\tWhat is the symbol for potassium?>'
        self.__quest_D_pl1[5] = '\tWhich planet is the hottest in the solar system?>'


    def get_questions_pl1(self):                                                                    # getter for pl1`s uestions

        return self.__quest_D_pl1                                                                   # returning the dictionary



    def set_answers_pl1(self):                                                                      # setter for pl1`s answers
                                                                                                    # setting the options in the dictionary

        self.__answer_D_pl1[1] = '\n\t1. 10\n\t2. 11\n\t3. 13\n\t4. 15\n\t5. 20'
        self.__answer_D_pl1[2] = '\n\t1. Amy\n\t2. Serena\n\t3. Sam\n\t4. Vanesssa\n\t5. Kate'
        self.__answer_D_pl1[3] = '\n\t1. Uruguay\n\t2. Andorra\n\t3. Benin\n\t4. Italy\n\t5. Australia'
        self.__answer_D_pl1[4] = '\n\t1. A\n\t2. Sn\n\t3. K\n\t4. U\n\t5. Br'
        self.__answer_D_pl1[5] = '\n\t1. Mercury\n\t2. Earth\n\t3. Venus\n\t4. Jupiter\n\t5. Neptune'



    def get_answers_pl1(self):                                                                      # getter for pl1`s answers

        return self.__answer_D_pl1                                                                  # returning the dictionary



    def set_questions_pl2(self):                                                                    # setter for pl2`s questions
                                                                                                    # setting the questions in the dictionary

        self.__quest_D_pl2[1] = '\tWhat year was the very first model of the iPhone released?>'
        self.__quest_D_pl2[2] = "\tWhat`s the shortcut for the `copy` function on most computers?>"
        self.__quest_D_pl2[3] = '\tWhat is often seen as the smallest unit of memory?>'
        self.__quest_D_pl2[4] = '\tWhat is the name of the man who launched eBay back in 1995?>'
        self.__quest_D_pl2[5] = '\tWhich email service is owned by Microsoft?>'


    def get_questions_pl2(self):                                                                    # getter for pl2`s questions
            
        return self.__quest_D_pl2                                                                   # returning the dictionary



    def set_answers_pl2(self):                                                                      # setter for pl2`s answers
                                                                                                    # setting the options in the dictionary

        self.__answer_D_pl2[1] = '\n\t1. 2019\n\t2. 2000\n\t3. 2005\n\t4. 2007\n\t5. None of the above'
        self.__answer_D_pl2[2] = '\n\t1. Ctr + C\n\t2. Shift + C\n\t3. Esc\n\t4. Ctr + K\n\t5. C'
        self.__answer_D_pl2[3] = '\n\t1. MB\n\t2. GB\n\t3. KB\n\t4. Mb\n\t5. b'
        self.__answer_D_pl2[4] = '\n\t1. Cornelius Boone\n\t2. Jeff Bezzos\n\t3. Pierre Omidyar\n\t4. Marie Huber\n\t5. Andy Cring'
        self.__answer_D_pl2[5] = '\n\t1. GMail\n\t2. Hotmail\n\t3. Yahoo\n\t4. Outlook\n\t5. None of the above'


    def get_answers_pl2(self):                                                                      # getter for pl2`s answers

        return self.__answer_D_pl2                                                                  # returning the dictionary



    def set_keys_pl1(self):                                                                         # setter for pl1`s correct answers
                                                                                                    # setting the answers in the dictionary

        self.__keys_pl1[1] = 2
        self.__keys_pl1[2] = 2
        self.__keys_pl1[3] = 1
        self.__keys_pl1[4] = 3
        self.__keys_pl1[5] = 3


    def get_keys_pl1(self, key):                                                                    # getter for pl1`s correct answers with parameter for the key

        return self.__keys_pl1[key]                                                                 # returning the key



    def set_keys_pl2(self):                                                                         # setter for pl2`s correct answers
                                                                                                    # setting the answers in the dictionary

        self.__keys_pl2[1] = 4
        self.__keys_pl2[2] = 1
        self.__keys_pl2[3] = 3
        self.__keys_pl2[4] = 3
        self.__keys_pl2[5] = 2


    def get_keys_pl2(self, key):                                                                    # getter for pl2`s correct answers with parameter for the key

        return self.__keys_pl2[key]                                                                 # returning the key



   


    def if_correct_answer_pl1(self, key):                                                           # setter for for the number of keys in the dictionaries for pl1
                                                                                                    # with parameter for the current key

        del self.__answer_D_pl1[key]                                                                # deleting the record in __answer_D_pl1
        del self.__quest_D_pl1[key]                                                                 # deleting the record in __quest_D_pl1
        del self.__keys_pl1[key]                                                                    # deleting the record in __keys_pl1
        



    def if_correct_answer_pl2(self, key):                                                           # setter for the number of keys in the dictionaries for pl2
                                                                                                    # with parameter for the kye

        del self.__quest_D_pl2[key]                                                                 # deleting the record in __quest_D_pl2
        del self.__answer_D_pl2[key]                                                                # deleting the record in __answer_d_pl2
        del self.__keys_pl2[key]                                                                    # deleting the record in __keys_pl2
        


    def null_count(self):                                                                           # re-setting the counter

        self.__count = 1                                                                            # setting __count to 1


    def set_count(self):                                                                            # setting the counter

        self.__count += 1                                                                           # adding 1 to __count


    def get_count(self):                                                                            # getter for the counter
            
        return self.__count                                                                         # returning the current counter





