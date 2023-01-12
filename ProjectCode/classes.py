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
        # self.id = unique_id

        self.battery_dict = {
            "location": f"{tuple((x, y))}",
            "capacity": capacity,
            "houses": [] # huizen moeten key worden in battery dict, value is lijst met huis-dicts
        }

    # def toJSON(self):
    #     return json.dumps(self.battery_dict, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def __repr__(self) -> str:
        return f"{self.battery_dict}"
        


class House:
    def __init__(self, x: int, y: int, max_output: float, unique_id: int) -> None:
        # self.id = unique_id - not sure if needed

        self.house_dict = {
            "location": f"{tuple((x, y))}",
            "output": max_output,
            "cables": []
        }

    # def toJSON(self):
    #     return json.dumps(self.house_dict, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    # def __repr__(self) -> str:
    #     return f"{self.house_dict}"


class Cable:
    def __init__(self) -> None:
        """ post: list of coordinates on which the cable runs """
        self.location = []

    def __repr__(self) -> str:
        return f"{self.location}"

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Grid:
    def __init__(self, batteries: list, district: int) -> None:
        self.batteries = batteries
        self.district_num = district
        self.costs_shared = 0
        
        self.grid_dict_char = {
            "district": self.district_num,
            "costs-shared": self.costs_shared
        }

        self.grid_list = [
            self.grid_dict_char,
            *[battery.battery_dict for battery in self.batteries]
        ]

    def toJSON(self):
        return json.dumps(self.grid_list, default=lambda o: o.__dict__, sort_keys=True, skipkeys= True, indent=4)
    
    # def __repr__(self) -> str:
    #     return f"{self.grid_dict}"
