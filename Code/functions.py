# ****************************************************************************
#  * functions.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of all functions
#  ***************************************************************************

from __future__ import annotations
from classes import Battery, House, Grid
import json
import matplotlib as mpl


def load(filename: str): 
    with open(filename) as f:
        list = []

        line_counter = 0
        unique_id = 1

        while True:
            line = f.readline().replace('\"', '').strip()

            if line == "":
                break
            elif line_counter == 0:
                line_counter += 1
                continue

            line_list = line.split(',')
            x = int(line_list[0])
            y = int(line_list[1])
            capacity_output = float(line_list[2])

            if "batteries" in filename:
                battery = Battery(x, y, capacity_output, unique_id)
                list.append(battery)
            elif "houses" in filename:
                house = House(x, y, capacity_output, unique_id)
                list.append(house)
            else:
                raise ValueError('file is invalid')

            
            unique_id += 1
            line_counter += 1
    
    return list


def output(grid: Grid):
    """Convert to JSON file"""
    grid.toJSON()


def visualize():
    pass


def house_into_batteries(batteries: list, houses: list):
    for battery in range(len(batteries)):
        for index, house in enumerate(houses):
            if index == 5:
                break
            batteries[battery].battery_dict["houses"].append(house.house_dict)
        # 30 houses per battery, implement for representation


def is_solution():
    pass


def calc_value():
    pass


def get_violations():
    pass
