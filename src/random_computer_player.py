import random
import time

from player import Player


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        print("loading...")
        time.sleep(2)
        return square
