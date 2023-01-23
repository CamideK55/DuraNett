import sys

sys.path.append('.../')

import random
import copy
from functions import batteries_capacity_check
from classes.battery import Battery
from classes.cable import Cable
from classes.house import House
from classes.grid_format import Grid

class hill_climber:
    def __init__(self, Grid, Battery, House, Cable):
        
        self.battery = Battery
        self.house = House
        self.cable = Cable

        Kies een random start state
        self.grid = copy.deepcopy(Grid)
        pass

     

    # Herhaal:
    def mutate_grid(self, grid):

    # Doe een kleine random aanpassing
        house = Grid.remove_random_house_from_battery()
        pass


        
        # Als de staat is verslechterd:
        #     Maak de aanpassing ongedaan