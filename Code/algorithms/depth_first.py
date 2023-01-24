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

    def __init__(self, batteries, houses):
        self.houses: list = houses
        self.batteries: list = copy.deepcopy(batteries)         #deepcopy?
        self.optional_state = [copy.deepcopy(self.batteries)]
        self.best_solution = None
        self.lowest_cost = float('inf')


    def next_state(self):
        return self.optional_state.pop()


    def create_children(self, batteries, house): 
        # get all possibilities for a house
        options = self.get_possibilities(batteries, house)

        # add a version of the batteries-houses to the stack, with a unique batteries combination
        for battery in options:
            new_batteries = copy.deepcopy(batteries)
            
            battery.houses.append(house)

            if new_batteries.battery.unique_id == battery.unique_id:
                new_batteries.battery = battery

            self.optional_state.append(new_batteries)
    
    
    def check_solutions(self, new_batteries):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = place_cables(new_batteries)[1]
        old_value = self.lowest_cost

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.best_solution = new_batteries
            self.lowest_cost = new_value
            print(f"New lowest cost: {self.lowest_cost}")
        

    # def batteries_capacity_check(batteries: list): aanroepen

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """


        while self.optional_state:
            new_batteries = self.next_state() 
            # grid_run = Grid(new_batteries, 0, 0)
        
            for house in self.houses:
                if not house.placed:
                    self.create_children(new_batteries, house)
                    house.placed = True
                else:
                    continue
            
            self.check_solutions(new_batteries)
        self.batteries = self.best_solution
                
        
    # move to class as method
    def get_possibilities(self, batteries, house):
        """
        returns a list of available batteries in which the house could be included, based on the current 
        capacity of the battery and total output of the houses 
        """
    
        available_opt = set(batteries)
        unavailable_opt = set()
        for battery in batteries:
            if battery.battery_check(house):
                unavailable_opt.add(battery)
                
        return list(available_opt - unavailable_opt)
        