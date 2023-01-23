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

class Depth_first:
    """
    Depth first algorithm which constructs a stack of grids, each with its own version of houses-batteries assignment
    """

    def __init__(self, batteries, houses):
        self.houses: list = houses
        self.batteries: list = batteries
        self.optional_state = [copy.deepcopy(self.batteries)]


    def next_state(self):
        return self.optional_state.pop()


    def create_children(self, batteries, houses): 

        # get all possibilities for a house
        options = self.get_possibilities(batteries, houses)

        # add a version of the batteries-houses to the stack, with a unique batteries combination
        for option in options:
            new_batteries = copy.deepcopy(batteries)
            new.batteries.  = options
            self.optional_state.append(new_batteries)
    
    # to do:
    # place houses in options of batteries
    # copy state of batteries


    # def batteries_capacity_check(batteries: list): aanroepen

    def run(self):
        pass


    # move to class as method
    def get_possibilities(self, batteries, houses):
        """
        returns a list of available batteries in which the house could be included, based on the current 
        capacity of the battery and total output of the houses 
        """
    
        available_opt = set(batteries)
        unavailable_opt = set()
        for house in houses:
            for battery in batteries:
                if battery.battery_check(house):
                    unavailable_opt.add(battery)
                
        return list(available_opt - unavailable_opt)
        