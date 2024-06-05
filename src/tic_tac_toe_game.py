from tic_tac_toe_board import TicTacToeBoard
from scoreboard import Scoreboard


class TicTacToeGame:
    def __init__(self):
        self._board = TicTacToeBoard()
        self._winner = ""
        self._scoreboard = Scoreboard()

    def available_moves(self):
        return self._board.empty_space()

    def reset_game(self):
        self._board.reset_board()
        self._winner = ""

    def continue_game(self):
        if self._winner:
            return False
        if not self._board.empty_space():
            return False
        return True

    def show_result(self):
        if self._winner:
            print(self._winner + " wins!")
        else:
            print("It's a tie!")

    def show_scoreboard(self):
        self._scoreboard.show_scoreboard()

    def print_board(self):
        self._board.print_board()

    def make_move(self, square, letter):
        if self._board.make_move(square, letter):
            if self._board.check_winner(square, letter):
                self._winner = letter
                self._scoreboard.set_vitory(letter)
            return True
        return False
