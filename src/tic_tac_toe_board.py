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

    def empty_space(self):
        return [i for i, spot in enumerate(self._board) if spot == " "]

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
        row = self._board[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        return False

    def _check_column(self, square, letter):
        col_index = square % 3
        column = [self._board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        return False

    def _check_diagonals(self, square, letter):
        if square % 2 == 0:
            diagonal1 = [self._board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self._board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
