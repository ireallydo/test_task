import time
import sys
from typing import NoReturn
from constants import PLAYERS_NUM

# для того, чтобы адаптировать игру под разный размер доски,
# адекватнее было бы генерировать поле в начале в зависимости от заданных параметров,
# и расписать логику как методы класса, структуру - как атрибут.
# но я не успела

# todo: organize in class
# todo: grid parameters to constants, delete hardcode values in grid elements check

grid = [
    # column 0 - 6
    {5: None, 4: None, 3: None, 2: None, 1: None, 0: None},
    {5: None, 4: None, 3: None, 2: None, 1: None, 0: None},
    {5: None, 4: None, 3: None, 2: None, 1: None, 0: None},
    {5: None, 4: None, 3: None, 2: None, 1: None, 0: None},
    {5: None, 4: None, 3: None, 2: None, 1: None, 0: None},
    {5: None, 4: None, 3: None, 2: None, 1: None, 0: None},
    {5: None, 4: None, 3: None, 2: None, 1: None, 0: None}
]

def have_winner(player: int, column: int) -> bool:
    chances = 4
    col = grid[column]
    for row in col:
        if col[row] is not None:
            if col[row] == player:
                chances -= 1
            else:
                break
    if not chances:
        return True
    else:
        return False


def empty_screen() -> NoReturn:
    for _ in range(9):
        sys.stdout.write('\033[F')
        sys.stdout.write("\033[K")


def make_move(player: int, column: int):
    col = grid[column]
    for row in col:
        if row == col[5] and col[row] is not None:
            pass
        else:
            if col[row] is None:
                empty_screen()
                col[row] = player
                if row != 5:
                    col[row+1] = None
                for line in grid:
                    print(line)
                time.sleep(1)
            else:
                break


def get_input(player: int) -> int:
    while True:
        move = input(f'Player {player} move!\nInput column number: ').strip()
        if move.isnumeric():
            if int(move) in range(7):
                return int(move)
        else:
            print('Please, input correct column number.')
            continue

def start_game() -> NoReturn:
    for line in grid:
        print(line)

    while True:
        for player in range(1, PLAYERS_NUM + 1):
            move = get_input(player)
            column = move - 1
            make_move(player, column)
            if have_winner(player, column):
                print(f'Winner winner chicken dinner!\nPlayer {player} won!')
                break


def restart_game() -> NoReturn:
    while True:
        restart = input('\nDo you wanna play again? (y/n): ').strip().lower()
        if 'y' == restart:
            start_game()
        elif 'n' == restart:
            print('\nk, byyyye!\n')
            break
        else:
            print('Sorry, what?')


if __name__ == "__main__":
    start_game()
    restart_game()


# todo: printout logic
#  printout = f"""
#  1 | 2 | 3 | 4 | 5 | 6 |
# _{grid[0][5]}_|_{grid[1][5]}_|_{grid[2][5]}_|_{grid[3][5]}_|_{grid[4][5]}_|_{grid[5][5]}_|_{grid[6][5]}_|
# _{grid[0][4]}_|_{grid[1][4]}_|_{grid[2][4]}_|_{grid[3][4]}_|_{grid[4][4]}_|_{grid[5][4]}_|_{grid[6][4]}_|
# _{grid[0][3]}_|_{grid[1][3]}_|_{grid[2][3]}_|_{grid[3][3]}_|_{grid[4][3]}_|_{grid[5][3]}_|_{grid[6][3]}_|
# _{grid[0][2]}_|_{grid[1][2]}_|_{grid[2][2]}_|_{grid[3][2]}_|_{grid[4][2]}_|_{grid[5][2]}_|_{grid[6][2]}_|
# _{grid[0][1]}_|_{grid[1][1]}_|_{grid[2][1]}_|_{grid[3][1]}_|_{grid[4][1]}_|_{grid[5][1]}_|_{grid[6][1]}_|
# _{grid[0][0]}_|_{grid[1][0]}_|_{grid[2][0]}_|_{grid[3][0]}_|_{grid[4][0]}_|_{grid[5][0]}_|_{grid[6][0]}_|
# """