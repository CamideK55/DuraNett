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
    # x_batteries = [[],[],[],[],[]]
    # y_batteries = [[],[],[],[],[]]
    x_batteries = []
    y_batteries = []
    x_houses = []
    y_houses = []
    x_cables = [[],[],[],[],[]]
    y_cables = [[],[],[],[],[]]


    # for i in batteries:
    #     for battery in grid.batteries:

    #         batteries[i].append(battery.location)

    for index, battery in enumerate(grid.batteries):
        x_batteries.append(battery.location[0])
        y_batteries.append(battery.location[1])
        
        for house in battery.houses:
            x_houses.append(house.location[0])
            y_houses.append(house.location[1])
            
            for cable in house.cables:
                x_cables[index].append(cable.location[0])
                y_cables[index].append(cable.location[1])
                

    print("Start visualization")
    
    color = ['crimson', 'chartreuse', 'turquoise', 'maroon', 'mediumblue']
    
    # create scatter plot
    for i in range(5):
        plt.scatter(x_batteries[i], y_batteries[i], marker= "P", c=color[i], label=f'Battery {i+1}')
        plt.scatter(x_houses, y_houses, marker= 's', c='grey')
        plt.scatter(x_cables[i], y_cables[i], marker= '.', c=color[i], s=2)
    

    # plt.scatter(x_houses, y_houses, marker= 's')
    # plt.scatter(x_batteries[0], y_batteries[0], marker= '+', c='red')
    # plt.scatter(x_batteries[1], y_batteries[1], marker= '+', c='blue')
    # plt.scatter(x_batteries[2], y_batteries[2], marker= '+', c='orange')
    # plt.scatter(x_batteries[3], y_batteries[3], marker= '+', c='green')
    # plt.scatter(x_batteries[4], y_batteries[4], marker= '+', c='yellow')
    
    # place lines
    plt.grid(visible = True)

    plt.legend(loc='best', bbox_to_anchor=(1,1))
    # plotting
    plt.savefig("results.png", bbox_inches='tight')
    plt.show()
    
    print("Visualization done")