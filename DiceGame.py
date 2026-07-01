# fmt: off
import sys
import os

# 1. Dynamically calculate the absolute path to your package folder
package_path = os.path.abspath("Dice_Game_PKG")

# 2. Inject it into Python's module search engine
if package_path not in sys.path:
    sys.path.insert(0, package_path)

from Die import Die
from Player import Player
# fmt: on


class DiceGame:
    def __init__(self, player: Player, computer: Player):
        self._myplayer = player
        self._computer_player = computer

    def play(self):
        print("-----------------------------")
        print("--🎲🎲-Starting the Dice game--🎲🎲----")
        print("-----------------------------")
        while True:
            self.play_round()
            game_over_bool = self.check_game_over_fn()
            if game_over_bool:
                break  # end the game

    def play_round(self):
        # welcome the user:
        print("🎲🎲New round🎲🎲")
        # input("Press any key to roll the die 🎲")
        input("Press any key to roll the die: ")

        # Getting the die value
        player_value_int = self._myplayer.roll_die()
        computer_value_int = self._computer_player.roll_die()

        # show the value
        print('Player value - ', player_value_int)
        print('Computer value - ', computer_value_int)

        # Determine the winner or loser
        if player_value_int > computer_value_int:
            print('Player won the round')
            # self._player.decrement_counter()
            # self._computer.increment_counter()
            self.update_counters(winner=self._myplayer, loser=self._computer_player)

        elif computer_value_int > player_value_int:
            print('Computer won the round')
            # self._computer.decrement_counter()
            # self._player.increment_counter()
            self.update_counters(winner=self._computer_player, loser=self._myplayer)
        else:
            print('************Its a tie************')

        # Print counter
        print('Your counter : ', self._myplayer.counter)
        print('Computer Counter : ', self._computer_player.counter)
        print('***********************')

    # Update counters
    def update_counters(self, winner: Player, loser: Player):
        winner.decrement_counter()
        loser.increment_counter()

    # Check for game over
    def check_game_over_fn(self):
        if self._myplayer.counter == 0:
            self.show_winner(self._myplayer)
            return True

        elif self._computer_player.counter == 0:
            self.show_winner(self._computer_player)
            return True
        else:
            return False

    def show_winner(self, winner):
        print("=========== Game Over=============")
        print(winner)
        print("========================")


die = Die()
my_player = Player(die, is_computer=False)
computer_player = Player(die, is_computer=True)
game = DiceGame(my_player, computer_player)
game.play()
