# ****************************************************************************
#  * visualisation.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * This code makes visual representation of the SmartGrid model.
#  ***************************************************************************

# from bokeh.plotting import figure, output_file, show
# from bokeh.palettes import magma
# import pandas as pd

import classes 
import matplotlib.pyplot as plt
import numpy as np
import json

def visualize(grid):
    # graph = figure(title= "AmstelHaege")
    # data = pd.read_csv(grid)
    # color = magma(256)
    # graph.scatter(data, color=color)
    # show(graph)

    # make the data
    # radio russia inspired: https://github.com/minprog/radio_russia_demo
    
    print("Loading vis")
    # with open("output.json", 'r') as json_file:
    #     data = json.load(json_file)
    print("Done")  

    # data = json.dumps(grid.grid_list, indent=4)
    

    # batteries = []
    # houses = []
    x_batteries = []
    y_batteries = []
    x_houses = []
    y_houses = []
    x_cables = []
    y_cables = []

    for battery in grid.batteries:
        x_batteries.append(battery.battery_dict["location"][0])
        y_batteries.append(battery.battery_dict["location"][1])
    for house in grid.houses:
        x_houses.append(house.house_dict["location"][0])
        y_houses.append(house.house_dict["location"][1])
        for cable in house.house_dict["cables"]:
            x_cables.append(cable.location[0])
            y_cables.append(cable.location[1])
        
    # for battery in grid.batteries:
    #     x_batteries.append(battery.battery_dict["location"][0])
    #     y_batteries.append(battery.battery_dict["location"][1])
    #     for house in battery.battery_dict["houses"]:
    #         x_houses.append(house["location"][0])
    #         y_houses.append(house["location"][1])
    
    # plt.style.use('_mpl-gallery')
    plt.scatter(x_houses, y_houses)
    plt.scatter(x_batteries, y_batteries)
    plt.scatter(x_cables, y_cables)
    
    # place lines
    plt.grid(visible = True)

    # plotting
    plt.show()
