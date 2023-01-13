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

    data = json.dumps(grid.grid_list, indent=4)
    
    batteries = []
    houses = []

    for battery in grid.batteries:
        batteries.append(battery.battery_dict["location"])
        for house in battery.battery_dict["houses"]:
            houses.append(house["location"])

    
    # plt.style.use('_mpl-gallery')
    plt.scatter(batteries, houses)
    
    plt.show()
    # plotting