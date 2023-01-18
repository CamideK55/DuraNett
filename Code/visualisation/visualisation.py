# ****************************************************************************
#  * visualisation.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * This code makes visual representation of the SmartGrid model.
#  ***************************************************************************


import matplotlib.pyplot as plt
import numpy as np
import json

def visualize(grid):
  
    # radio russia inspired: https://github.com/minprog/radio_russia_demo
    x_batteries = []
    y_batteries = []
    x_houses = []
    y_houses = []
    x_cables = []
    y_cables = []

    for battery in grid.batteries:
        x_batteries.append(battery.location[0])
        y_batteries.append(battery.location[1])
        
        for house in battery.houses:
            x_houses.append(house.location[0])
            y_houses.append(house.location[1])
            
            for cable in house.cables:
                x_cables.append(cable.location[0])
                y_cables.append(cable.location[1])
    
    print("Start visualization")
    
    # create scatter plot
    plt.scatter(x_houses, y_houses, marker= 's')
    plt.scatter(x_batteries, y_batteries, marker= '+')
    plt.scatter(x_cables, y_cables, marker= '_')
    
    # place lines
    plt.grid(visible = True)

    # plotting
    plt.savefig("results.png")
    plt.show()
    
    print("Visualization done")