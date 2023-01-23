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

class Depth_first:
    """
    Depth first algorithm which constructs a stack of grids, each with its own version of houses-batteries assignment
    """

    def __init__(self, batteries, houses):
        self.houses: list = houses
        self.batteries: list = batteries
        self.state = [copy.deepcopy(self.batteries)]


    def next_state(self):
        return self.state.pop()

    def create_children(self): 


    # def batteries_capacity_check(batteries: list): aanroepen

    def run(self):
        pass


    def get_possibilities():