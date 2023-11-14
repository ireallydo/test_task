from console import Console
from constants import COLUMNS_NUM, ROWS_NUM
from typing import NoReturn
import time


class GameBoard:
    def __init__(self, console: Console, columns: int = COLUMNS_NUM, rows: int = ROWS_NUM):
        self.__columns = columns
        self.__rows = rows
        self.grid = [{i: None for i in range(self.__rows - 1, -1, -1)} for _ in range(self.__columns)]
        self.__console = console

    def make_move(self, player: int, column: int) -> int:
        """Checks how low a tile can fall in the given column;
        invokes animation of the tile fall;
        takes player number and column from CLI input as arguments;
        returns the number of the row on which the tile landed in the column"""
        col = self.grid[column]
        for row in col:
            if col[row] is None:
                col[row] = player
                # check for first row from the top
                if row != (self.__rows - 1):
                    col[row + 1] = None
                # prints out the current state of each "drop" of tile
                self.make_printout()
                # and clears console for next stage of animation
                self.__console.empty_screen(len(self.grid) + 1)
                time.sleep(0.2)
            else:
                break
            last_row = row
        # return of last row is used in horizontal check for winner (by rows)
        return last_row

    def have_winner(self, player: int, column: int, cur_row: int) -> bool:
        """Checks if there is a sequence of 4 consequent tiles of the given player
        in a given column or in a given row;
        if 4 consequent tiles are found, return True, else - returns False"""
        chances = 4
        col = self.grid[column]
        # check columns
        for row in col:
            if col[row] is not None:
                if col[row] == player:
                    chances -= 1
                else:
                    break
        if not chances:
            return True
        else:
            chances = 4

        # check rows
        previous_row = self.grid[0]
        for c in self.grid:
            if c[cur_row] is not None:
                if c[cur_row] == player and previous_row[cur_row] == player:
                    chances -= 1
                elif c[cur_row] == player:
                    chances = 4
                    chances -= 1
            previous_row = c
        if not chances:
            return True
        else:
            return False

    def make_printout(self) -> NoReturn:
        """Prints out the current state of tiles on the game board to the command line"""
        first_row = ''.join(f'| {num + 1} ' for num in range(len(self.grid)))
        print(first_row + f"\n{'_'*4*len(self.grid)}")
        for row in range(len(self.grid[0]) - 1, -1, -1):
            row = ''.join(f'|_{self.grid[i][row]}_' for i in range(len(self.grid))).replace('None', '_')
            if row == 0:
                print(row, end='\n')
            else:
                print(row)
