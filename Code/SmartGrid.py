# ****************************************************************************
#  * SmartGrid.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  *   ----
#  ***************************************************************************

from classes import Battery, House, Grid
from functions import load, output, house_into_batteries
from visualisation.visualisation import visualize
from algorithms import randomize
import sys


if __name__ == "__main__":
   
    # check if input is valid
    if len(sys.argv) != 2:
        print("Usage: SmartGrid.py <district number>\n")
        exit(1)

    # retrieve user input from command-line
    district_num = sys.argv[1]

    # loading csv file to the program
    batteries: list = load(f"../Data/district_{district_num}/district-{district_num}_batteries.csv")
    houses: list = load(f"../Data/district_{district_num}/district-{district_num}_houses.csv")

    # place cables in houses according to algorithms
    # cables_into_batteries(houses)

    # place houses into batteries
    house_into_batteries(batteries, houses)
    
    # initialize grid
    grid = Grid(batteries, houses, int(district_num))

    # place cables according to algorithm 
    # grid_random = randomize.random_assignment(grid)

    # render output of grid
    output(grid)

    # visualize output
    visualize(grid)

    # nieuwe stappenplan:
    # initialize grid
    # grid_random = randomize.random_assignment(grid)
    # place houses into batteries
    # render output of grid
    # visualize outputs
    