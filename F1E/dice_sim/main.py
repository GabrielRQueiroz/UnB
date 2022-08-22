import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)


def roll_dice(dice: Dice, rolls: int) -> int:
    total = 0
    for i in range(rolls):
        result = dice.roll()
        total += result
    return total


def roll_count(dice: Dice, rolls: int, number: int or str = "all") -> int or dict:
    count = {}

    for i in range(rolls):
        result = dice.roll()
        count[result] = count.get(result, 0) + 1

    if number == "all":
        return dict(sorted(count.items()))

    if count.__contains__(number):
        return count[number]

    return 0


def launch_experiment(dice: Dice = Dice(6), rolls: int = 10, number: int = 1) -> dict:
    """Launches n dices and excludes all with the specified number facing up. Repeats it until there are less than 6 dices left."""
    gen = 1
    gens = {0: int(rolls)}

    while True:
        undesired = roll_count(dice, rolls, number)
        rolls -= undesired
        gens[gen] = int(rolls)
        gen += 1
        if rolls < 6:
            # Return gens with no decimal spaces
            return gens
