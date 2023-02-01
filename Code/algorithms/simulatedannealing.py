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
    """ 
    Simulated Annealing is an iterative algorithem that builds on the HillClimber.
    This algorithem is capable to go to states with a higher value (lower is better) 
    to break out of local minima. It uses a probabilty that increases when iterations 
    increase.
    """
    def __init__(self, grid, temperature=1):

        # Initilaze the HillClimber class
        super().__init__(grid)
        
        # initialize the instance atributes
        self.Temp_start = temperature
        self.Temp = temperature
        self.best_value = self.value


    def update_temperature(self):
        """ 
        This method updates the temperature which is used for the accaptance probabilty.
        """

        self.T = self.Temp_start - (self.Temp_start / self.iterations)


    def check_solution(self, new_grid):
        """ Update the grid and value to the best value found. """

        # calculate the value of the new grid
        new_value = new_grid.total_costs()

        # set best value found to old and best value
        old_value = self.value
        best_value = old_value
        
        # use difference between best value found and the new value 
        # to use for the accaptance probability.
        delta = old_value - new_value

        # acceptance probability is a exponential formula used to break out 
        # of local minima
        acceptance_probability = math.exp(delta / self.Temp)

        # if a random float between 0 and 1 is less than the accaptance probability
        # the new state will be set as the current state
        if random.random() < acceptance_probability:
            self.grid = new_grid
            self.value = new_value
        
        # check if the new value is better than the current best value and if so
        # redefine the best value
        if new_value < best_value:
            self.best_value = new_value
        
        # updates the temperature for the new iteration
        self.update_temperature()

        return self.grid