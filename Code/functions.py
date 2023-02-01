# ****************************************************************************
#  * functions.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of all functions
#  ***************************************************************************

from __future__ import annotations
from classes.battery import Battery
from classes.house import House
from classes.grid_format import Grid
from classes.cable import Cable
from algorithms import random as rand
import json
import matplotlib as mpl


def load(filename: str):
    """
    Loads the data from the csv files. Creates either House objects or Battery
    Objects, based on the filename.
    """
    with open(filename) as f:
        list = []
        line_counter = 0
        unique_id = 1

        # read lines in file
        while True:
            line = f.readline().replace('\"', '').strip()

            if line == "":
                break
            elif line_counter == 0:
                line_counter += 1
                continue

            # take coordinates and capacity/output
            line_list = line.split(',')
            x = int(line_list[0])
            y = int(line_list[1])
            capacity_output = float(line_list[2])

            # make house and battery objects and place them into appropriate list
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


def output(grid):
    """Convert to JSON file"""
    # grid.toJSON()
    with open("../Data/JSON_output/output.json", "w") as output_file:
            return json.dump(grid, output_file, indent= 4, default=vars)


def place_cables(batteries, grid):
    """
    Places the cables between the batteries and houses, after they have been
    assigned by a algorithm.
    """
    costs_shared = 0
    for battery in batteries:        
        costs_shared += 5000

        for house in battery.houses:
            cable_costs = house.placing_cable(battery)
            costs_shared += cable_costs
    return batteries, costs_shared


def correct_json(grid):
    """
    Creates the list with dicts in which the output is given. This list is 
    eventually converted to a JSON-file.
    """
    grid_dict = {
        "district": grid.district_num,
        "costs-shared": grid.total_costs() 
    }

    grid_list = [
        grid_dict,
        *battery_dict(grid.batteries)
    ]

    return grid_list


def battery_dict(batteries):
    """
    Part/continuation of the correct_json function.
    """
    battery_list = []
    for battery in batteries:
        battery_dict = {
            "location": f"{battery.location[0]},{battery.location[1]}",
            "capacity": battery.capacity,
            "houses": [*house_dict(battery.houses)]
        }
        battery_list.append(battery_dict)
    return battery_list


def house_dict(houses):
    """
    Part/continuation of the correct_json function.
    """
    house_list = []
    for house in houses:
        house_dict = {
            "location": f"{house.location[0]},{house.location[1]}",
            "output": house.output,
            "cables": [f"{cable.x},{cable.y}" for cable in house.cables]
        }
        house_list.append(house_dict)
    return house_list

def batteries_capacity_check(batteries: list):
    """
    Checks if any of the batteries is overloaded, and returns True if this is
    not the case
    """
    for battery in batteries:
        if battery.battery_capacity_overloaded():
            return False
    return True

def get_costs(grid) -> int:
    return grid.costs_shared


def error_message(commands1, commands2):
    """
    Error message in case of incorrect user input.
    """       
    print("Usage: SmartGrid.py <district number> <constructive algorithm> optional: <iterable algorithm> \n")
    print("COMMAND LINE OPTIONS")
    print("district number: 0, 1, 2, 3")
    print(f"base algorithm: {commands1}")
    print(f"top algorithm: {commands2}")
    exit(1)