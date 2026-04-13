# Kris Kleiner
# CSD-325
# Module 3 Assignment
# This program simulates the Cho-Han dice game.
# Modified from the original chohan.py file.
#
# Changes made:
# 1. Changed the input prompt to "kk:"
# 2. Changed the house fee from 10% to 12%
# 3. Added a notice in the introduction about a 10 mon bonus
#    for rolling a total of 2 or 7
# 4. Added logic to award the 10 mon bonus when the dice
#    total equals 2 or 7
# 5. Added comments to document program flow and changes

import random
import sys

JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total is an even (cho) or odd (han) number.

Bonus: If the total of the dice roll is 2 or 7, you receive a 10 mon bonus.
''')

# Starting amount of money for the player
purse = 5000

while True:
    # Ask the player how much they want to bet
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')

    while True:
        pot = input('kk: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Ask the player to choose CHO or HAN
    while True:
        bet = input('kk: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
        else:
            break

    # Show the dice results
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Check for bonus roll of 2 or 7
    if dice_total == 2 or dice_total == 7:
        print('The total was', dice_total, '- you got a 10 mon bonus!')
        purse = purse + 10

    # Determine whether the total is even or odd
    roll_is_even = (dice_total % 2 == 0)

    if roll_is_even:
        correct_bet = 'CHO'
    else:
        correct_bet = 'HAN'

    player_won = (bet == correct_bet)

    # Update purse based on win or loss
    if player_won:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot

        house_fee = int(pot * 0.12)
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot
        print('You lost!')

    # End the game if the player runs out of money
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()