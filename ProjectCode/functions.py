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


def load(filename: str): 
    with open(filename) as f:
        
        list = []

        line_counter = 0
        unique_id = 1

        while True:
            if line == "":
                break
            elif line_counter == 0:
                continue

            line = f.readline().strip()
            
            line_list = line.split(',')
            x = line_list[0]
            y = line_list[1]
            capacity_output = line_list[2]

            if "batteries" in filename:
                battery = Battery(x, y, capacity_output, unique_id)
                list.append(battery)
            elif "houses" in filename:
                house = House(x, y, capacity_output)
                list.append(house)
            else:
                raise ValueError('file is invalid')

            
            unique_id += 1
            line_counter += 1
    
    return list


def output(grid: Grid):
    for i in range(len(grid.batteries)):
        print(grid.batteries[i])
    
    for i in range(len(grid.houses)):
        print(grid.houses[i])


def visualize():
    pass
