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
import numpy as np


class Battery:
    def __init__(self, district: int, x: int, y: int, capacity: float, unique_id: int) -> None:
        """ post:  """
        self.district = district
        self.coordinates = tuple((x, y))
        # self.x = x
        # self.y = y
        self.capacity = capacity
        self.houses = []
        self.id = unique_id

        self.battery_dict = {
            "location": f"{self.coordinates}",
            "capacity": self.capacity,
            "houses": self.houses
        }
    
    def __repr__(self) -> str:
        self.battery_dict


class House:
    def __init__(self, district: int, x: int, y: int, max_output: float) -> None:
        self.district = district
        self.coordinates = tuple((x, y))
        # self.x = x
        # self.y = y
        self.max_output = max_output
        self.cables = []

        self.house_dict = {
            "location": f"{self.coordinates}",
            "output": self.max_output,
            "cables": self.cables
        }
    
    def __repr__(self) -> str:
        self.house_dict


class Cable:
    def __init__(self) -> None:
        """ post: list of coordinates on which the cable runs """
        # nog onzeker of het een tuple moet zijn
        self.coordinates = []

    def __repr__(self) -> str:
        pass


class Grid:
    def __init__(self, houses: list, batteries: list, district: int) -> None:
        self.houses = houses
        self.batteries = batteries
        self.district_num = district
        self.costs_shared = 0
    
    def __repr__(self) -> str:
        pass
