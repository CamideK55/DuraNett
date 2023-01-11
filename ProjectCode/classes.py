# ****************************************************************************
#  * classes.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of all classes
#  ***************************************************************************
from __future__ import annotations
import matplotlib
import json


class Battery:
    def __init__(self, x: int, y: int, capacity: float, unique_id: int) -> None:
        """ post:  """
        self.coordinates = tuple((x, y))
        self.capacity = capacity
        self.houses = []
        self.id = unique_id

        self.battery_dict = {
            "location": f"{self.coordinates}",
            "capacity": self.capacity,
            "houses": self.houses
        }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    # def __repr__(self) -> str:
    #     return f"{self.battery_dict}"
        


class House:
    def __init__(self, x: int, y: int, max_output: float, unique_id: int) -> None:
        self.coordinates = tuple((x, y))
        self.max_output = max_output
        self.cables = []
        self.id = unique_id

        self.house_dict = {
            "location": f"{self.coordinates}",
            "output": self.max_output,
            "cables": self.cables
        }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    # def __repr__(self) -> str:
    #     return f"{self.house_dict}"


class Cable:
    def __init__(self) -> None:
        """ post: list of coordinates on which the cable runs """
        self.coordinates = []

    def __repr__(self) -> str:
        return f"{self.coordinates}"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Grid:
    def __init__(self, houses: list, batteries: list, district: int) -> None:
        self.houses = houses
        self.batteries = batteries
        self.district_num = district
        self.costs_shared = 0
        
        self.grid_dict = {
            "district": self.district_num,
            "costs-shared": self.costs_shared
        }

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    # def __repr__(self) -> str:
    #     return f"{self.grid_dict}"
