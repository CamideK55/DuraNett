import json
import random


class Grid:
    def __init__(self, batteries: list, costs_shared: int, district: int) -> None:
        self.batteries = batteries
        # self.houses = houses
        self.district_num = district
        self.costs_shared = costs_shared
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
        for battery in self.batteries:
            self.total_costs_II += battery.cost

            for house in battery.houses:
                self.total_costs_II += sum([cable.cost for cable in house.cables])

        return self.total_costs_II

    def remove_random_house_from_batterys(self):
        index = random.randint(len(range(self.batteries)))
        battery = self.batteries[index]
        house = battery.houses[random.randint(len(range(battery.houses)))]
        house.empty_cables()
        return house
    
    def assign_house_to_random_battery(self, house):
        self.batteries



    
    # https://pynative.com/python-json-dumps-and-dump-for-json-encoding/
    # https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
    # https://pynative.com/python-json-dumps-and-dump-for-json-encoding/