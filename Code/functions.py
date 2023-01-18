# ****************************************************************************
#  * functions.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of all functions
#  ***************************************************************************

from __future__ import annotations
from classes import Battery, House, Grid, Cable
import json
import matplotlib as mpl
# import jsonpickle


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
    return batteries


def place_cables(batteries):
    for battery in batteries:
        location_battery = list(battery.battery_dict["location"])
        battery_x = location_battery[0]
        battery_y = location_battery[1]
        cable_list = []

        for house in battery.battery_dict["houses"]:
            location_house = list(house["location"])
            location_cable = location_house
            house_x = location_house[0]
            house_y = location_house[1]

            # search for an equal x
            while location_cable[0] != location_battery[0]:
                if location_cable[0] > location_battery[0]:
                    house["cables"].append(Cable(location_cable[0], location_cable[1]))
                    location_cable[0] -= 1
                else:
                    house["cables"].append(Cable(location_cable[0], location_cable[1]))
                    location_cable[0] += 1
            # search for an equal y
            while location_cable[1] != location_battery[1]:
                if location_cable[1] > location_battery[1]:
                    house["cables"].append(Cable(location_cable[0], location_cable[1]))
                    location_cable[1] -= 1
                else:
                    house["cables"].append(Cable(location_cable[0], location_cable[1]))
                    location_cable[1] += 1
            
            cable_list.append(Cable(location_battery[0], location_battery[1]))
    return batteries
    

        

def toJSONpickle(object):
    return jsonpickle.encode(object)


def is_solution():
    pass


def calc_value():
    pass


def get_violations():
    pass
