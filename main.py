from console import console
from game_board import GameBoard
from game import Game


def start_game():
    board = GameBoard(console)
    game = Game(console, board)
    game.start_game()
    if game.restart_game():
        start_game()


if __name__ == "__main__":
    start_game()
