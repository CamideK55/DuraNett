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


def output(grid):
    """Convert to JSON file"""
    # grid.toJSON()
    with open("output.json", "w") as output_file:
            return json.dump(grid, output_file, indent= 4, default=vars)


def house_into_batteries(batteries: list, houses: list):
    for battery in range(len(batteries)):
        for index, house in enumerate(houses):
            if index == 5:
                break
            batteries[battery].houses.append(house.house_dict)
    return batteries


def place_cables(batteries, grid):
    costs_shared = 0
    for battery in batteries:
        # location_battery = list(battery.location)
        # cable_list = []
        costs_shared += 5000

        for house in battery.houses:
            cable_costs = house.placing_cable(battery, grid)
            costs_shared += cable_costs
            # cable_list.append(Cable(location_battery[0], location_battery[1]))
    return batteries, costs_shared


def correct_json(grid): 
    grid_dict = {
        "district": grid.district_num,
        "costs-shared": grid.total_costs() 
    }

    grid_list = [
        grid_dict,
        *battery_dict(grid.batteries)
    ]

    return grid_list

    # List[dict{"district",
    # "costs-shared"},
    #  dict{"location",
    # "capacity",
    # "houses":[{"location",
    #     "output",
    #     "cables"[]]}}]


def battery_dict(batteries):
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
    for battery in batteries:
        if battery.battery_capacity_overloaded():
            return False
    return True


# def same_cable(grid, cable):
#     if cable.location in grid.all_cables:
#         return True
#     else:
#         return False
        
        
def is_solution():
    pass


def get_violations():
    pass


def get_costs(grid):
    return grid.costs_shared


def run_random(iterations, grid):

    for iteration in range(iterations):

        random = rand.Random(grid)
        random.run

        random.check_solution(grid)
