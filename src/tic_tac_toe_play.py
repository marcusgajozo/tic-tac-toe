from tic_tac_toe_game import TicTacToeGame
from human_player import HumanPlayer


class TicTacToePlay:
    def __init__(self):
        self._game = TicTacToeGame()
        self._human_player = HumanPlayer("X")
        self._opponent = HumanPlayer("O")
        self._letter = "X"

    def _play_turn(self, player_symbol):
        square = (
            self._human_player.get_move(self._game)
            if player_symbol == "X"
            else self._opponent.get_move(self._game)
        )
        if self._game.make_move(square, player_symbol):
            print("----------------")
            print(f"{player_symbol} makes a move to square {square}")
            self._game.print_board()

    def play_game(self):
        self._game.print_board()
        while self._game.continue_game():
            self._play_turn(self._letter)
            self._letter = "O" if self._letter == "X" else "X"
        self._game.show_result()
        print("Goodbye!")
