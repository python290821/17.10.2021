
import random
for i in range(3):
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

