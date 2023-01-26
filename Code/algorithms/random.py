# ****************************************************************************
#  * random.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of the Hill Climber algorithm
#  *
#  ***************************************************************************

import sys

sys.path.append('.../')

import random
import copy


class Random:
    def __init__(self, grid):
        self.grid = grid
        self.houses = copy.deepcopy(grid.houses)
        self.counter = 0

    # voor elke batterij
    #     plaats een huis tot dat er geen huis meer bij past
    # controleer of alle huizen zijn geplaatst
    # zo niet probeer opnieuw

    def place_house_into_battery(self, battery, house):
        if battery.battery_check(house):
            return True
        battery.houses.append(house)
        battery.total_output_houses += house.output
        house.placed = True
        return False


    def does_house_fit(self, house):
        pass

    def fill_batteries(self):
        for house in self.houses:
            index = random.choice(range(len(self.grid.batteries)))
            battery = self.grid.batteries[index]
            if self.place_house_into_battery(battery, house) and house.placed:
                print("house does not fit")
                continue
            self.counter += 1
            print(self.counter)
    
    def clear_batteries(self):
        for battery in self.grid.batteries:
            for house in battery.houses:
                house.empty_cables()
            battery.empty_batteries()

    
    def run(self):
        while self.counter != len(self.houses):
            self.counter = 0
            self.clear_batteries()
            self.fill_batteries()
            print(f"NEXT TRY - counter is {self.counter}")
        
        # extra check for overloaded batteries
        for battery in self.grid.batteries:
            x = battery.battery_capacity_overloaded()
            print(x)
        print(self.grid.batteries)
        
    # def check_houses_list(houses):
    #     if len(houses)