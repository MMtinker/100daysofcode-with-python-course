from rpc_class import *
import random


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    count = 1
    while count < 4:
        p2_roll = random.choice(rolls)
        p1_roll = user_roll(rolls)

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        print(f'Computer rolled: {p2_roll}')
        print(f'You rolled: {p1_roll}')

        # display winner for this round

        count += 1

    # Compute who won


def print_header():
    print('--------------------------------')
    print('     Rock, Paper, Scissors')
    print('--------------------------------')


def get_players_name():
    name = input('What is your name?')
    return name

def build_the_three_rolls():
    return ['rock', 'paper', 'scissors']


def user_roll(rolls):
    print()
    for idxRoll in rolls:
        print(f'{rolls.index(idxRoll)} - {idxRoll} ')

    while True:
        roll = input(' Please select your roll: ')
        if roll.isdigit():
            if int(roll) <= len(rolls):
                break
        print('\n Incorrect input, please try again \n')

    return rolls[int(roll)]



main()
