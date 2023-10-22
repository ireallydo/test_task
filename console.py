import sys
from typing import NoReturn
from constants import COLUMNS_NUM
import time


class Console:
    def __init__(self):
        pass

    def get_move(self, player: int, full_columns: list) -> int:
        """Gets the move input from the CLI from the current player;
        checks if the move can be made and if yes - returns the input of the player"""
        while True:
            move = input(f'Player {player} move! Input column number: ').strip()
            if move.isnumeric() and int(move) in range(1, COLUMNS_NUM + 1) and (int(move) - 1) not in full_columns:
                return int(move)
            else:
                sys.stdout.write("\033[K")
                sys.stdout.write('\033[F')
                print('Please, input correct column number!         ', end='\r')
                time.sleep(2)
                sys.stdout.write("\033[K")
                continue

    def empty_screen(self, rows: int) -> NoReturn:
        """Clears the given number of rows from CLI"""
        for _ in range(rows):
            sys.stdout.write("\033[K")
            sys.stdout.write('\033[F')

    def ask_for_restart(self):
        """Asks for option to restart game and returns True or False"""
        while True:
            restart = input('\nDo you wanna play again? (y/n): ').strip().lower()
            if 'y' == restart:
                return True
            elif 'n' == restart:
                return False
            else:
                print('Sorry, what?')

    def print_winner(self, winner: int) -> NoReturn:
        """Prints out the winner to the CLI"""
        print(f'Winner winner chicken dinner!\nPlayer {winner} won!')


console = Console()
