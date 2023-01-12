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
    # https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
    
    print(grid.toJSON())

    # grid_dict = {}
    # battery_dict = {}
    # houses_dict = {}

    # print(json.dumps(grid.grid_dict_char))

    # for i in range(len(grid.batteries)):
        # print(grid.batteries[i].toJSON())
        # print(json.dumps(grid.batteries[i]))
    
    # for i in range(len(grid.houses)):
        # print(grid.houses[i].toJSON())
        # print(json.dumps(grid.houses[i]))

    # total_dict = {**grid_dict, **battery_dict, **houses_dict}

    # convert to json file: link= https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
#     with open("sample.json", "w") as outfile:
#         outfile.write(json_object)
    
    # return json

def visualize():
    pass

def house_into_batteries(batteries: list, houses: list):
    for battery in range(len(batteries)):
        for index, house in enumerate(houses):
            if index == 5:
                break
            batteries[battery].battery_dict["houses"].append(house.house_dict)
        # 30 houses per battery, implement for representation