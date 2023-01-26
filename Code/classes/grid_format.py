import json
import random


class Grid:
    def __init__(self, batteries: list, houses, district: int) -> None:
        self.batteries = batteries
        self.houses = houses
        self.district_num = district
        self.costs_shared = 0
        # self.total_costs = 0
        self.total_costs_II = 0

        self.grid_list = [
            self.district_num,
            self.costs_shared,
            [battery for battery in self.batteries]
        ]

    def toJSON(self):
        with open("output.json", "w") as output_file:
            return json.dump(self.grid_list, output_file, indent= 4, default=vars)


    def total_costs(self):
        costs = 0
        for battery in self.batteries:
            costs += battery.cost
            for house in battery.houses:
                costs += sum([cable.cost for cable in house.cables])

        return costs

    def remove_random_house_from_batteries(self):
        index = random.choice(range(len(self.batteries)))
        battery = self.batteries[index]
        house = battery.houses[random.choice(range(len(battery.houses)))]
        house.empty_cables()
        return house
    
    def assign_house_to_random_battery(self, house):
        self.batteries

    def give_houses_length(self):
        return len(self.houses)

    
    # https://pynative.com/python-json-dumps-and-dump-for-json-encoding/
    # https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
    # https://pynative.com/python-json-dumps-and-dump-for-json-encoding/