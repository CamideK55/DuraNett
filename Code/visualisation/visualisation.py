# ****************************************************************************
#  * visualisation.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * This code makes visual representation of the SmartGrid model.
#  ***************************************************************************

import matplotlib.pyplot as plt


def visualize(grid):
  
    # radio russia inspired: https://github.com/minprog/radio_russia_demo
    x_batteries = []
    y_batteries = []
    x_houses = []
    y_houses = []
    x_cables = [[],[],[],[],[]]
    y_cables = [[],[],[],[],[]]

    # place data from grid into seperate batteries, houses, and cables lists
    for index, battery in enumerate(grid.batteries):
        x_batteries.append(battery.location[0])
        y_batteries.append(battery.location[1])
        
        for house in battery.houses:
            x_houses.append(house.location[0])
            y_houses.append(house.location[1])
            
            for cable in house.cables:
                x_cables[index].append(cable.location[0])
                y_cables[index].append(cable.location[1])
                

    # set colors for visualization
    color = ['crimson', 'chartreuse', 'turquoise', 'maroon', 'mediumblue']
    
    # create scatter plot
    for i in range(5):
        plt.scatter(x_batteries[i], y_batteries[i], marker= "P", c=color[i], label=f'Battery {i+1}')
        plt.scatter(x_houses, y_houses, marker= 's', c='grey')
        plt.scatter(x_cables[i], y_cables[i], marker= '.', c=color[i], s=2)
        
    # place lines and legend
    plt.grid(visible = True)
    plt.legend(loc='best', bbox_to_anchor=(1,1))
    
    # save and display plott
    plt.savefig("../Data/results/results.png", bbox_inches='tight')
    plt.show()
    
    