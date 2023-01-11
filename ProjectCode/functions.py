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
    print(json.dumps(grid.grid_dict))

    for i in range(len(grid.batteries)):
        print(grid.batteries[i].toJSON())
        print(json.dumps(grid.batteries[i]))
    
    for i in range(len(grid.houses)):
        print(grid.houses[i].toJSON())
        print(json.dumps(grid.houses[i]))


def visualize():
    pass
