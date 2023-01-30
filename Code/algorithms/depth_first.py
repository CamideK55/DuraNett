# ****************************************************************************
#  * depth_first.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of a depth_first algoritm
#  ***************************************************************************
# inspired by Radio Russia: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/depth_first.py

import copy
from classes.house import House
from classes.battery import Battery
from classes.grid_format import Grid
from functions import place_cables


class Depth_first:
    """
    Depth first algorithm which constructs a stack of grids, each with its own version of houses-batteries assignment
    """

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.houses = self.grid.houses
        self.batteries = self.grid.batteries
        self.optional_state = [copy.deepcopy(self.batteries)]
        self.best_solution = [Battery]
        self.lowest_cost = float('inf')
        self.states_visted = 0
        self.archive = set()
        self.done = False


    def next_state(self):
        return self.optional_state.pop()


    def create_children(self, batteries, house): 
        # get all possibilities for a house

        #print("create child:",batteries,"house:",house)
        for index, battery in enumerate(batteries):
            #print("battery:",batteries[index])
            if not batteries[index].battery_check(house):
                new_batteries = copy.deepcopy(batteries)
                new_batteries[index].houses.append(house)
                print("child:",new_batteries)
                self.optional_state.append(new_batteries)

    
    # def check_solutions(self, new_batteries):
    #     """
    #     Checks and accepts better solutions than the current solution.
    #     """
    #     new_value = place_cables(new_batteries)[1]
    #     old_value = self.lowest_cost

    #     # We are looking for grids that cost less
    #     if new_value <= old_value:
    #         self.best_solution = new_batteries
    #         self.lowest_cost = new_value
    #         print(f"New lowest cost: {self.lowest_cost}")


    def depth_first_recursive(self, batteries, houses, house_index):
        if house_index == len(houses):
            # print("batteries:",batteries,"house_index:",house_index)
            self.done = True
        #for index,h in enumerate(houses):
        if not self.done:
            self.states_visted += 1
            for index in range(house_index,len(houses)):
                for b in batteries:
                    if not self.done and not b.battery_check(houses[house_index]):
                        b.houses.append(houses[index])
                        b.total_output_houses += houses[house_index].output
                        return self.depth_first_recursive(batteries,houses,house_index+1)
        
        
    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        self.depth_first_recursive(self.batteries, self.houses, 0)
        return self.grid
        
    # move to class as method
    # def get_possibilities(self, batteries, house):
    #     """
    #     returns a list of available batteries in which the house could be included, based on the current 
    #     capacity of the battery and total output of the houses 
    #     """
    #     available_opt = set(batteries)
    #     unavailable_opt = set()
    #     for battery in batteries:
    #         if battery.battery_check(house):
    #             unavailable_opt.add(battery)
                
    #     return list(available_opt - unavailable_opt)
        