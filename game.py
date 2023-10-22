from game_board import GameBoard
from console import Console
from typing import NoReturn, Union
from constants import PLAYERS_NUM, ROWS_NUM


class Game:
    def __init__(self, console: Console, board: GameBoard, players: int = PLAYERS_NUM):
        self.__console = console
        self.__board = board
        self.__players = players
        self.winner = None

    def start_game(self) -> NoReturn:
        """Prints out the initial game board state to the CLI
        and iteratively passes the move to each player;
        invokes getting input from CLI for each player,
        then invokes the move on the game board,
        and then checks if the move resulted in having a winner;
        if not, passes the move to the next player"""
        self.__board.make_printout()

        while not self.winner:
            for player in range(1, PLAYERS_NUM + 1):
                # check for full columns (to be passed to input check)
                full_columns = []
                for col in range(len(self.__board.grid)):
                    if self.__board.grid[col][ROWS_NUM - 1] is not None:
                        full_columns.append(col)

                move = self.__console.get_move(player, full_columns)
                # clears old data from the screen before the move animation
                self.__console.empty_screen(9)
                column = move - 1
                row = self.__board.make_move(player, column)
                # prints out current board state after the move animation
                self.__board.make_printout()
                # winner check
                if self.__board.have_winner(player, column, row):
                    self.winner = player
                    self.__console.print_winner(self.winner)
                    break

    def restart_game(self) -> Union[bool, NoReturn]:
        """Invokes the game restart option;
        if it gets positive answer from CLI, invokes start_game()"""
        if self.__console.ask_for_restart():
            return True
        else:
            print('\nk, byyyye!\n')
