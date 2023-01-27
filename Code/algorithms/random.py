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
    """This algorithm randomly assigns houses to batteries. It checks if the 
    the total output of the houses assigned to the battery exceeds the max 
    capacity. If so the algorithm switches houses from batteries until all 
    houses are assigned to a battery and no batteries exceed their capacity """
    def __init__(self, grid):
        self.grid = grid
        self.houses = copy.deepcopy(grid.houses)
        self.counter = 0
        self.best_result = 0


    def place_house_into_battery(self, battery, house):
        """This function places the given house into the given battery if
        it fits."""
        if battery.battery_check(house):
            return True
        battery.houses.append(house)
        battery.total_output_houses += house.output
        house.placed = True
        return False


    def does_house_fit(self, house):
        """Chekcs if the given house fits into one of the batteries."""
        for battery in self.grid.batteries:
            if battery.battery_check(house):
                return False
        return True


    def get_radom_house(self):
        """Returns a randomly chosen house"""
        index = random.choice(range(len(self.grid.houses)))
        house = self.grid.houses[index]
        return house


    def get_random_battery(self):
        """Returns a randomly chosen battery"""
        index = random.choice(range(len(self.grid.batteries)))
        battery = self.grid.batteries[index]
        return battery


    def switch_houses(self, house):
        """Switches the house given with a randomly chosen house
        from a randomly chosen battery."""
        #remove random house from random battery
        battery = self.get_random_battery()
        house = battery.houses[random.choice(range(len(battery.houses)))]
        
        # place into random battery
        if self.place_house_into_battery(battery, house):
            return False
        return True


            

    def fill_batteries(self):
        """Fills the batteries with houses. If a house doesn't fit into one
        of the batteries the switch houses method is called."""
        for house in self.houses:
            index = random.choice(range(len(self.grid.batteries)))
            battery = self.grid.batteries[index]
            if self.does_house_fit(house):
                # print("house fits")
                self.place_house_into_battery(battery, house)
            else:
                # print("house DOES NOT fit")
                while not self.switch_houses(house):
                    # print("Trying to switch houses")
                    continue
            self.counter += 1
       
       
    def clear_batteries(self):
        """Clears all batteries from their houses and empties their cable 
        lists."""
        for battery in self.grid.batteries:
            for house in battery.houses:
                house.empty_cables()
            battery.empty_batteries()

    
    def run(self):
        """Runs the method defined in this class in order to assign all
        houses to a battery without exceeding the batterie's capacity"""
        while self.counter != len(self.houses):
            self.counter = 0
            self.clear_batteries()
            self.fill_batteries()
            # print(f"NEXT TRY - counter is {self.counter}")
        
        # extra check for overloaded batteries
        for battery in self.grid.batteries:
            x = battery.battery_capacity_overloaded()
            # print(x)