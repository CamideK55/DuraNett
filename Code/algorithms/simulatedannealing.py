# ****************************************************************************
#  * simulatedannealing.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of the Simulated Annealing algorithm
#  *
#  * This algorithm is based on and inspired by the Simulated Annealing 
#  * algorithm which is given on the Radio Russia github that corresponds to 
#  * this course. 
#  ***************************************************************************
import random
import math

from algorithms.hill_climber import HillClimber

class SimulatedAnnealing(HillClimber):
    """ type something """
    def __init__(self, grid, temperature=1):
        # Initilaze the HillClimber class
        super().__init__(grid)
        
        # Starting temperature and current temperature
        self.Temp_start = temperature
        self.Temp = temperature
    
    def update_temperature(self):
        """ Type something """
        self.T = self.Temp_start - (self.Temp_start / self.iterations)

    def check_solution(self, new_grid):
        """ Type something """
        new_value = new_grid.total_costs()
        old_value = self.value
        
        delta = old_value - new_value
        acceptance_probability = math.exp(delta / self.Temp)

        print(f"new value = {new_value} and old value = {old_value}")

        if random.random() < acceptance_probability:
            self.grid = new_grid
            self.value = new_value
        
        self.update_temperature()

        