class Scoreboard:
    def __init__(self):
        self.x = 0
        self.o = 0

    def set_vitory(self, letter):
        if letter == "X":
            self.x += 1
        else:
            self.o += 1

    def show_scoreboard(self):
        print("--------------------")
        print(f"X: {self.x}")
        print(f"O: {self.o}")
        print("--------------------")
