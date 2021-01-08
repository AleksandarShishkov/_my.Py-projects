


def score_validation_pl(score_pl):                                                  # defining score_validation_pl() function
                                                                                    # which accepts one argument for the pl`s score
    if(score_pl == 10):                                                             # validating the score
        print('\n\n\t\tYou have won the game.\n\n')
    else:
        print('\nYour score is: ', score_pl)


def score_validation_pc(score_pc):                                                  # defining score_validation_pc() function
                                                                                    # which accepts one argument for the pc`s score
    if(score_pc == 10):                                                             # validating the score
        print('\n\n\t\tThe PC has won the game.\n\n')
    else:
        print('PC`s score is: ', score_pc)


