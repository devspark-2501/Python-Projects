import random

while True:
    roll = input('Press enter to roll the dice or type (Q) to quit: ')

    if roll.lower() == 'q':
        print('Thanks for playing!')
        break

    dice = random.randint(1, 6)
    print(f'You rolled a {dice}!')

    