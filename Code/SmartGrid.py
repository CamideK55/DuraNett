# ****************************************************************************
#  * SmartGrid.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  *   ----
#  ***************************************************************************

from classes import Battery, House, Grid
from functions import load, output, house_into_batteries, place_cables
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

    # initialize grid
    # grid = Grid(batteries, houses, int(district_num))
    
    # # place cables in houses according to algorithms
    # grid_random = randomize.random_assignment(grid)

    # place houses in batteries according to algorithms
    batteries = randomize.random_assignment(batteries, houses)

    # place cables
    batteries = place_cables(batteries)
    
    # # place houses into batteries
    # update_batteries = house_into_batteries(batteries, houses)

    # update grid with batteries and houses that have cables
    grid = Grid(batteries, int(district_num))

    # render output of grid
    output(grid)

    # visualize output
    visualize(grid)
