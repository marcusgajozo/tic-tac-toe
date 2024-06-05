import random
import time


class TicTacToeBoard:
    def __init__(self):
        self._board = [" " for _ in range(9)]

    def print_board(self):
        for row in [self._board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square, letter):
        if self._board[square] == " ":
            self._board[square] = letter
            return True
        return False

    def get_board(self):
        return self._board

    def reset_board(self):
        self._board = [" " for _ in range(9)]


class TicTacToeGame:
    def __init__(self):
        self._board = TicTacToeBoard()
        self._current_winner = ""
        self._scoreboard = {"O": 0, "X": 0}

    def available_moves(self):
        return [i for i, spot in enumerate(self._board.get_board()) if spot == " "]

    def reset_game(self):
        self._board.reset_board()
        self._current_winner = ""

    def continue_game(self):
        if self._current_winner:
            return False
        return " " in self._board.get_board()

    def get_scoreboard(self):
        return self._scoreboard

    def get_current_winner(self):
        return self._current_winner

    def _check_winner(self, square, letter):
        if self._check_row(square, letter):
            self._scoreboard[letter] += 1
            return True
        if self._check_column(square, letter):
            self._scoreboard[letter] += 1
            return True
        if self._check_diagonals(square, letter):
            self._scoreboard[letter] += 1
            return True
        return False

    def print_board(self):
        self._board.print_board()

    def _check_row(self, square, letter):
        row_index = square // 3
        row = self._board.get_board()[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        return False

    def _check_column(self, square, letter):
        col_index = square % 3
        column = [self._board.get_board()[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        return False

    def _check_diagonals(self, square, letter):
        if square % 2 == 0:
            diagonal1 = [self._board.get_board()[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self._board.get_board()[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def make_move(self, square, letter):
        if self._board.make_move(square, letter):
            if self._check_winner(square, letter):
                self._current_winner = letter
            return True
        return False


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

    def _show_result(self):
        print()
        if self._game.get_current_winner():
            print(self._game.get_current_winner() + " wins!")
        else:
            print("It's a tie!")

    def _show_scoreboard(self):
        print("--------------------")
        for i in self._game.get_scoreboard():
            print(f"{i}: {self._game.get_scoreboard()[i]}")
        print("--------------------")

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

            self._show_result()

            self._print_menu(True)
            option = self._get_user_choice()
            while option == "3":
                self._show_scoreboard()
                self._print_menu(True)
                option = self._get_user_choice()

        print("Goodbye!")


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        print("loading...")
        time.sleep(2)
        return square


if __name__ == "__main__":
    tic_tac_toe = TicTacToePlay()
    tic_tac_toe.play_game()
