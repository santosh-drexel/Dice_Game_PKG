import random


class Die:
    def __init__(self, value=None):
        self._value = value

    @property  # getter
    def value(self):
        return self._value

    def get_value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        # new_value = self.get_value()
        self._value = new_value
        return new_value


# die = Die()
# new_value = die.roll()
# print(new_value, die.value, die.get_value())
################
