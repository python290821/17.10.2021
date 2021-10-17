
import random

my_score = 0
computer_score = 0
for i in range(3):

    # i draw a card
    card1 = random.randint(2, 14)
    if card1 <= 10:
        print(card1)
    elif card1 == 11:
        print('J')
    elif card1 == 12:
        print('Q')
    elif card1 == 13:
        print('K')
    else: # card1 == 14:
        print('A')

    #todo:
    # computer draws card

    # print who won or draw
    # update score

    # after 3 rounds print score for player and computer


