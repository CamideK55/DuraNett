import json
import random
from classes.cable import Cable


class Grid:
    def __init__(self, batteries: list, houses, district: int) -> None:
        """
        Initialization of instance attributes.
        """
        self.batteries = batteries
        self.houses = houses
        self.district_num = district
        self.costs_shared = 0
        self.total_costs_II = 0
        self.all_cables : set[tuple[int]] = set()

        self.grid_list = [
            self.district_num,
            self.costs_shared,
            [battery for battery in self.batteries]
        ]

    # https://pynative.com/python-json-dumps-and-dump-for-json-encoding/
    # https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
    # https://pynative.com/python-json-dumps-and-dump-for-json-encoding/
    def toJSON(self):
        """
        Takes the grid and converts it to a json
        """
        with open("output.json", "w") as output_file:
            return json.dump(self.grid_list, output_file, indent= 4, default=vars)


    def total_costs(self) -> int:
        """
        Returns the total costs made by the sum of all cables and batteries.
        """
        costs = 0
        for battery in self.batteries:
            costs += battery.cost
            for house in battery.houses:
                costs += sum([cable.cost for cable in house.cables])

        return costs

    def remove_random_house_from_batteries(self, grid):
        """ 
        Removes a random House from a random Battery.
        Updates the neccesary attributes accordingly.
        """
        index = random.choice(range(len(grid.batteries)))
        battery = grid.batteries[index]
        house = battery.houses[random.choice(range(len(battery.houses)))]
        battery.total_output_houses -= house.output
        house.placed = False
        house.empty_cables()
        
        return house, battery
    
    def give_houses_length(self) -> int:
        """
        Gives the amount of the total houses in Grid.
        """
        return len(self.houses)


    def same_cables(self, location) -> bool:
        """
        Checks if given location is in the archive.
        """
        return location in self.all_cables
