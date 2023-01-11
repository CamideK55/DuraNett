# ****************************************************************************
#  * SmartGrid.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  *   ----
#  ***************************************************************************

from classes import Battery, House, Grid
from functions import load, output, visualize
import sys


if __name__ == "__main__":
   
    # check if input is valid
    if len(sys.argv) != 2:
        print("Usage: SmartGrid.py <district number>\n")
        exit(1)

    # retrieve user input from command-line
    district_num = sys.argv[1]

    # loading csv file to the program
    batteries: list = load(f"../Huizen&Batterijen/district-{district_num}_houses.csv")
    houses: list = load(f"../Huizen&Batterijen/district-{district_num}_batteries.csv")

    # initialize grid 
    grid = Grid(houses, batteries, district)

    # render output of grid
    output(grid)
