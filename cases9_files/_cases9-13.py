from random import randint


class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """Initialize the number of sides."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides."""
        print(randint(1, self.sides))


d10 = Die(10)
d20 = Die(20)

print("Rolling a 10-sided die:")
for _ in range(10):
    d10.roll_die()

print("\nRolling a 20-sided die:")
for _ in range(10):
    d20.roll_die()