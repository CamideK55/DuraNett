# ****************************************************************************
#  * hill_climber.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of the Hill Climber algorithm
#  *
#  * This algorithm is based on and inspired by the Hill Climber algorithm
#  * which is given on the Radio Russia github that corresponds to this 
#  * course.
#  ***************************************************************************

import sys

sys.path.append('.../')

import random
import copy

class HillClimber:
    """ HillClimber is an iterative algorithm that generates states of the system 
    by mutation of a randomly created initiale state. The algorithm mutates the 
    the system by way of placing a randomly chosen house to a randomly chosen
    battery. The algorithem saves the state with the lowest costs as the systems 
    current state. """
    def __init__(self, Grid):
        self.value = Grid.total_costs()

        # creat a copy of the grid to work with in this class
        self.grid = copy.deepcopy(Grid)

        # initialize the state counter
        self.states_counter = 0


    def mutate_grid(self, new_grid):
        """ Mutate the current grid by reassigning a random
        house to a random battery. """

        # randomly switch two houses from their batteries
        while not self.swich_houses(new_grid):
            continue

        self.states_counter += 1


    def check_solution(self, new_grid):
        """ Check if the new generated state is better than the current state 
        if so, set the current state equal to the new state. """
        
        # calculate the results from the new state
        new_value = new_grid.total_costs()
        current_value = self.value

        # print(f"new value = {new_value} and old value = {current_value}")
        
        # check if the new state has better results than the current state
        if new_value <= current_value:

            # change the current state to the new state
            self.grid = new_grid
            self.value = new_value


    def run(self, iterations):
        """ Runs the HillClimber algorithm for a user defined amount of iterations."""
        
        # initialize iteratons
        self.iterations = iterations

        # loop for the amount of iterations 
        for iterations in range(iterations):

            # Creat a copy of the grid to simulate change
            new_grid = copy.deepcopy(self.grid)

            # Mutate the copy to get a different solution 
            self.mutate_grid(new_grid)

            # Accept the mutation if its better
            self.check_solution(new_grid)

        return self.grid


    def swich_houses(self, new_grid):
        """ This method randomly choses two houses from two randomly chosen batteries. 
        It than switch the houses and places them by the other battery if these houses
        fit. When the houses do not fit they will be sat back to their original battery.
        """

        # get two random houses and their corresponding batteries
        house_1, battery_1 = new_grid.remove_random_house_from_batteries(new_grid)
        house_2, battery_2 = new_grid.remove_random_house_from_batteries(new_grid)

        # check if the the houses fit into the other battery
        if not battery_1.battery_check(house_2) and not battery_2.battery_check(house_1):

            # place the houses into their new batteries
            battery_1.houses.append(house_2)
            battery_1.total_output_houses += house_2.output
            house_2.placed = True
            house_2.placing_cable(battery_1)

            battery_2.houses.append(house_1)
            battery_2.total_output_houses += house_1.output
            house_1.placed = True
            house_1.placing_cable(battery_2)

            return True

        else:

            # place the houses back to their original battery 
            battery_1.houses.append(house_1)
            battery_1.total_output_houses += house_1.output
            house_1.placed = True
            house_1.placing_cable(battery_1)

            battery_2.houses.append(house_2)
            battery_2.total_output_houses += house_2.output
            house_2.placed = True
            house_2.placing_cable(battery_2)

            return False