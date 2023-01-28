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
        self.grid = copy.deepcopy(grid)
        self.houses = self.grid.houses
        self.counter = 0
        self.best_result = 0
        self.available_opt = set(self.grid.batteries)
        self.unavailable_opt = set()


    def place_house_into_battery(self, battery, house):
        """This function places the given house into the given battery if
        it fits."""
        if battery.battery_check(house):
            return True
        # print("house adding to battery")
        battery.houses.append(house)
        battery.total_output_houses += house.output
        house.placed = True
        self.houses.remove(house)
        return False


    def does_house_fit(self, house):
        """Chekcs if the given house fits into one of the batteries."""
        self.unavailable_opt.clear()
        for battery in self.grid.batteries:
            if battery.battery_check(house):
                # print("house does not fit into battery")
                self.unavailable_opt.add(battery)
                # print(self.unavailable_opt)
        # print(f"unavailable options are {self.unavailable_opt} available optiions are {self.available_opt}")
        difference = list(self.available_opt - self.unavailable_opt)
        # print(difference)
        
        return difference


    def get_radom_house(self):
        """Returns a randomly chosen house"""
        index = random.choice(range(len(self.grid.houses)))
        house = self.houses[index]
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
        index = random.choice(range(len(battery.houses)))
        removed_house = battery.houses.pop(index)
        battery.total_output_houses -= removed_house.output
        
        # place into random battery
        if self.place_house_into_battery(battery, house):
            # print("house can not be switched")
            battery.houses.append(removed_house)
            return False
        # print("House is switched")
        self.houses.append(removed_house)
        return True


    def fill_batteries(self):
        """Fills the batteries with houses. If a house doesn't fit into one
        of the batteries the switch houses method is called."""
        # while self.houses:
        for house in self.houses:
            # index = random.choice(range(len(self.grid.batteries)))
            # battery = self.grid.batteries[index]
            battery_options = self.does_house_fit(house)
            # print(battery_options)
            if battery_options != []:
                # print("house fits")
                self.place_house_into_battery(battery_options[random.choice(range(len(battery_options)))], house)
            else:
                while not self.switch_houses(house):
                    # print("Trying to switch houses")
                    continue
                # print("house DOES NOT fit")
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
        while self.houses:
            self.counter = 0
            self.fill_batteries()
            
        # extra check for overloaded batteries
        # for battery in self.grid.batteries:
        #     # x = battery.battery_capacity_overloaded()
        #     print(battery.total_output_houses)

        return self.grid