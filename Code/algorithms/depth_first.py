# ****************************************************************************
#  * depth_first.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of a depth_first algoritm
#  ***************************************************************************
# inspired by Radio Russia: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/depth_first.py

from __future__ import annotations
import copy
from classes.house import House
from classes.battery import Battery
from classes.grid_format import Grid
from functions import place_cables


class Depth_first:
    """
    Depth first algorithm which uses a recursive function to find the first solution of a valid grid
    """

    def __init__(self, grid: Grid):
        """
        Initialization of instance attributes.
        """
        self.grid = copy.deepcopy(grid)
        self.houses = self.grid.houses
        self.batteries = self.grid.batteries
        self.optional_state = [copy.deepcopy(self.batteries)]
        self.best_solution = [Battery]
        self.lowest_cost = float('inf')
        self.states_visted = 0
        self.archive = set()
        self.done = False

    def depth_first_recursive(self, batteries, houses, house_index):
        """
        A recursive Depth-first function that takes batteries, houses, and index.
        It returns the first complete valid solution with all houses placed.
        """
        # check if all houses are placed into a battery
        if house_index == len(houses):
            self.done = True
        
        # devide houses over batteries
        if not self.done:
            self.states_visted += 1
            for index in range(house_index,len(houses)):
                for b in batteries:
                    if not self.done and not b.battery_check(houses[house_index]):
                        b.houses.append(houses[index])
                        b.total_output_houses += houses[house_index].output
                        return self.depth_first_recursive(batteries, houses, house_index + 1)
    
        
    def run(self)  -> Grid:
        """
        Runs the algorithm untill all houses are placed, and the solution is found and valid.
        """
        self.depth_first_recursive(self.batteries, self.houses, 0)
        return self.grid
        