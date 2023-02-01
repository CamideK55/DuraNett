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
    """ 
    This algorithm randomly assigns houses to batteries. It checks if the 
    the total output of the houses assigned to the battery exceeds the max 
    capacity. If so the algorithm switches houses from batteries until all 
    houses are assigned to a battery and no batteries exceed their capacity. 
    """
    def __init__(self, grid):

        # create a deep copy of the grid which can be
        self.grid = copy.deepcopy(grid)
        
        # initialize the instance atributes
        self.houses = self.grid.houses
        self.best_result = 0
        self.state_counter = 0
        self.all_opt = set(self.grid.batteries)
        self.unavailable_opt = set()


    def place_house_into_battery(self, battery, house):
        """
        This function places the given house into the given battery if
        it fits.
        """

        # check if the battery's capacity will not be exceded by adding the new house
        if battery.battery_check(house):
            return True

        # Connect house to battery by placing a cable
        battery.houses.append(house)
        house.placing_cable(battery)
        battery.total_output_houses += house.output
        house.placed = True
        self.houses.remove(house)
        
        # add a new state to the counter
        self.state_counter += 1
    
        return False


    def does_house_fit(self, house):
        """
        Checks if the given house fits into one of the batteries.
        """

        # reset the unavailable options to 0
        self.unavailable_opt.clear()

        # loop over all the batteries in the grid
        for battery in self.grid.batteries:

            # check if the house can be added to the battery without exceeding
            # the maximum capacity
            if battery.battery_check(house):

                # place the battery into the set of unavailable options
                self.unavailable_opt.add(battery)
        
        # create a list of all available options for the given house
        available_opt = list(self.all_opt - self.unavailable_opt)
        

        return available_opt


    def get_radom_house(self):
        """
        Returns a randomly chosen house.
        """

        index = random.choice(range(len(self.grid.houses)))
        house = self.houses[index]
        
        return house


    def get_random_battery(self):
        """
        Returns a randomly chosen battery.
        """
        
        index = random.choice(range(len(self.grid.batteries)))
        battery = self.grid.batteries[index]

        return battery


    def switch_houses(self, house):
        """
        Switches the house given with a randomly chosen house
        from a randomly chosen battery.
        """

        # remove random house from a random battery
        battery = self.get_random_battery()
        index = random.choice(range(len(battery.houses)))
        removed_house = battery.houses.pop(index)
        battery.total_output_houses -= removed_house.output
        
        # place house into randomly chosen battery
        if self.place_house_into_battery(battery, house):

            # house does not fit into the battery and therefor the 
            # removed house needs to be placed back into its original 
            # battery
            battery.houses.append(removed_house)
            removed_house.placing_cable(battery)

            # add a new state to the counter
            self.state_counter += 1

            return False

        # house is placed into its new battery and thus removed house 
        # needs to be added 
        self.houses.append(removed_house)

        # add a new state to the counter
        self.state_counter += 1

        return True


    def fill_batteries(self):
        """
        Fills the batteries with houses. If a house doesn't fit into one
        of the batteries the switch houses method is called.
        """

        # loop over all the houses
        for house in self.houses:

            # create a list of battery options for the given house
            battery_options = self.does_house_fit(house)

            # check if their are battery options for the house
            if battery_options != []:

                # place house into a randomly chosen house from the possible options
                self.place_house_into_battery(battery_options[random.choice(range(len(battery_options)))], house)
            
            # switch the house with a random other house when their are no possible options
            else:
                while not self.switch_houses(house):
                    continue

            # add a new state to the counter
            self.state_counter += 1


    def run(self):
        """
        Runs the method defined in this class in order to assign all
        houses to a battery without exceeding the batterie's capacity
        for as long as the houses list is not empty.
        """

        while self.houses:
            self.fill_batteries()
       
        return self.grid