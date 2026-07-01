class Player:
    def __init__(self, die, is_computer=True):
        self._die = die
        # self._is_computer = is_computer
        if is_computer:
            self.name = "Computer_Player"
        else:
            self.name = "myplayer"

        self._counter = 10

    # getting all the variables
    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    # increment and decrement counters
    def increment_counter(self):
        self._counter += 1
        # print('Counter : ', self.counter)

    def decrement_counter(self):
        self._counter -= 1
        # print('Counter : ', self.counter)

    def roll_die(self):
        return self._die.roll()

    def __str__(self):

        return f'============================\n{self.name} won🏆the game🎉🎉🎉\n============================'


# die = Die()
# player = Player(die, False)
# # print(player.is_computer)
# print(player.die.value)
# print(player.roll_die())

# print(player.counter)
# player.increment_counter()
# print('Counter : ', player.counter)
# print(player)
