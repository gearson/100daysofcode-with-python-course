from rps_classes import Player
import random


def print_header():
    print()
    print('-------------------------------')
    print('    Rock, Paper, Scissors      ')
    print('-------------------------------')
    print()

def get_players_name():
    return input("What's your name? ")

def build_the_three_rolls():
    return three_rolls


def main():
    print_header()

    rolls = build_the_three_rolls()
    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Computer")

    game_loop(player1, player2, rolls)


# actual game loop

def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:
        p2_roll = None # TODO: get random roll
        p1_roll = Roll(input('Rock, Paper or Scissors? ')) # TODO: have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        # display winner for this round

        count += 1

    # Compute who won



if __name__ == "__main__":
    main()