class Scoreboard:
    def __init__(self):
        self._x = 0
        self._o = 0

    def set_vitory(self, letter):
        if letter == "X":
            self._x += 1
        else:
            self._o += 1

    def show_scoreboard(self):
        print("--------------------")
        print(f"X: {self._x}")
        print(f"O: {self._o}")
        print("--------------------")
