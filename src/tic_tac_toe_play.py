from tic_tac_toe_game import TicTacToeGame
from human_player import HumanPlayer
from random_computer_player import RandomComputerPlayer


class TicTacToePlay:
    def __init__(self):
        self._game = TicTacToeGame()
        self._human_player = HumanPlayer("X")
        self._opponent = None
        self._letter = "X"

    def _print_menu(self, again=False):
        print("--------------------")
        if again:
            print("Do you want to play again?")
        else:
            print("Welcome to Tic Tac Toe!")
        print("1. Play a game alone")
        print("2. Play a game in pairs")
        print("3. Show Scoreboard")
        print("0. Exit")

    def _get_user_choice(self):
        while True:
            choice = input("Enter your choice: ")
            if choice in ("1", "2", "3", "0"):
                return choice
            else:
                print("Invalid choice. Please enter 0, 1, 2, or 3.")

    def _choose_opponent(self, option):
        if option == "1":
            self._opponent = RandomComputerPlayer("O")
        else:
            self._opponent = HumanPlayer("O")

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

    def _show_scoreboard(self):
        self._game.show_scoreboard()

    def play_game(self):
        self._print_menu()
        option = self._get_user_choice()

        while option == "3":
            self._show_scoreboard()
            self._print_menu()
            option = self._get_user_choice()

        while option == "1" or option == "2":
            self._choose_opponent(option)
            self._game.reset_game()
            self._game.print_board()

            while self._game.continue_game():
                self._play_turn(self._letter)
                self._letter = "O" if self._letter == "X" else "X"

            self._game.show_result()

            self._print_menu(True)
            option = self._get_user_choice()
            while option == "3":
                self._show_scoreboard()
                self._print_menu(True)
                option = self._get_user_choice()

        print("Goodbye!")
