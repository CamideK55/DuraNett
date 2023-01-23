import sys

sys.path.append('.../')

import random
import copy
from functions import batteries_capacity_check
from classes.battery import Battery
from classes.cable import Cable
from classes.house import House
from classes.grid_format import Grid

class HillClimber:
    def __init__(self, Grid):
        
        self.value = Grid.total_costs()
        print(self.value)

        # Kies een random start state
        self.grid = copy.deepcopy(Grid)


    def mutate_grid(self, new_grid):

    # Doe een kleine random aanpassing
        house = new_grid.remove_random_house_from_batteries()

        index = random.choice(range(len(new_grid.batteries)))
        battery = new_grid.batteries[index]
        house.placing_cable(battery)


    def check_solution(self, new_grid):

        new_value = new_grid.total_costs()
        old_value = self.value

        print(f"new value = {new_value} and old value = {old_value}")
        if new_value <= old_value:
            self.grid = new_grid
            self.value = new_value
        


    def run(self, iterations):
        self.iterations = iterations

        for iterations in range(iterations):
            
            # Creat a copy of the grid to simulate change
            new_grid = copy.deepcopy(self.grid)

            # Mutate the copy to get a different solution 
            self.mutate_grid(new_grid)

            # Accept the mutation if its better
            self.check_solution(new_grid)

            