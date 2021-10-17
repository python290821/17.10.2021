import random
import time

# demo code
def print_card(_card = random.randint(2, 14)):
    if _card <= 10:
        print(_card)
    elif _card == 11:
        print('J')
    elif _card == 12:
        print('Q')
    elif _card == 13:
        print('K')
    else: #_card == 14:
        print('A')


my_score = 0
computer_score = 0
while my_score < 5 and computer_score < 5:
    # i draw a card
    card_player = random.randint(2, 14)
    card_computer = random.randint(2, 14)
    print('my card: ', end='')
    print_card(card_player)
    time.sleep(1)
    print('computer card: ', end='')
    print_card(card_computer)
    time.sleep(1)
    if card_player > card_computer:
        print('player won!')
        my_score += 1
    elif card_computer > card_player:
        print('computer won')
        computer_score +=1
    else:
        print('tie ....')
    print('SCORE:')
    print('ME', my_score)
    print('COMPUTER', computer_score)
    print('============================')
    time.sleep(2)


