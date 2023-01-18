import json

class Grid:
    def __init__(self, batteries: list, costs_shared: int, district: int) -> None:
        self.batteries = batteries
        # self.houses = houses
        self.district_num = district
        self.costs_shared = costs_shared

        self.grid_list = [
            self.district_num,
            self.costs_shared,
            [battery for battery in self.batteries]
        ]

    def toJSON(self):
        with open("output.json", "w") as output_file:
            return json.dump(self.grid_list, output_file, indent= 4, default=vars)        

    
    # https://pynative.com/python-json-dumps-and-dump-for-json-encoding/
    # https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
    # https://pynative.com/python-json-dumps-and-dump-for-json-encoding/