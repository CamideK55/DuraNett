import random
import copy

# https://github.com/minprog/radio_russia_demo/blob/college_1/code/algorithms/randomise.py
possibilities = range(50)


def randomize(batteries: list, houses: list):
    for battery in batteries:
        while battery.battery_capacity_not_overloaded():
            random_assignment(batteries, houses)
        return batteries


def random_assignment(batteries: list, houses: list):
    """
    Randomly assign each cable with one of the possibilities.
    """

    while len(houses) > 0:
        for battery in batteries:
            random.shuffle(houses)
            index = random.choice(range(len(houses)))
            battery.houses.append(houses[index])
            battery.total_output_houses += houses[index].output
            houses.pop(index)
    
    return batteries