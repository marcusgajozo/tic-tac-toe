import random

class TicTacToeBoard:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            return True
        return False


class TicTacToeGame:
    def __init__(self):
        self.board = TicTacToeBoard()
        self.current_winner = None

    def available_moves(self):
        return [i for i, spot in enumerate(self.board.board) if spot == " "]

    def continue_game(self):
        if (self.current_winner != None):
            return False
        return " " in self.board.board

    def check_winner(self, square, letter):
        if self._check_row(square, letter):
            return True
        if self._check_column(square, letter):
            return True
        if self._check_diagonals(square, letter):
            return True
        return False

    def _check_row(self, square, letter):
        row_index = square // 3
        row = self.board.board[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        return False

    def _check_column(self, square, letter):
        col_index = square % 3
        column = [self.board.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        return False

    def _check_diagonals(self, square, letter):
        if square % 2 == 0:
            diagonal1 = [self.board.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def make_move(self, square, letter):
        if self.board.make_move(square, letter):
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

class TicTacToePlay:
    def __init__(self):
        self.game = TicTacToeGame()
        self.x_player = HumanPlayer("X")
        self.o_player = None

    def _menu_start(self):
        print("Welcome to Tic Tac Toe!")
        print("1. Play a game alone")
        print("2. Play a game in pairs")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if(choice == "1"):    
            self.o_player = RandomComputerPlayer("O")
            return True
        elif(choice == "2"):
            self.o_player = HumanPlayer("O")
            return True
        else:
            print("Goodbye!")
        return False
    
    def _menu_reset():          
        print("Want to play again?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if(choice == "1"):
            return True
        return False 

    def play_game(self, letter="X"):
        start = self._menu_start()
        while start:
            self.game.board.print_board()
            while self.game.continue_game():
                if letter == "O":
                    square = self.o_player.get_move(self.game)
                else:
                    square = self.x_player.get_move(self.game)
                if self.game.make_move(square, letter):
                    print(letter + f" makes a move to square {square}")
                    self.game.board.print_board()
                    print("")
                    if self.game.current_winner:
                        print(letter + " wins!")
                    letter = "O" if letter == "X" else "X"
            print("It's a tie!")
            print("--------------------")
            start = self._menu_reset()
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
        return square


if __name__ == "__main__":
    tic_tac_toe = TicTacToePlay()
    tic_tac_toe.play_game()