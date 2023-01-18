# ****************************************************************************
#  * SmartGrid.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  *   ----
#  ***************************************************************************

from classes.grid_format import Grid
from functions import load, output, house_into_batteries, place_cables, get_costs, correct_json
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

    # place houses in batteries according to algorithms
    batteries = randomize.random_assignment(batteries, houses)

    # place cables
    batteries, costs_shared = place_cables(batteries)

    # update grid with batteries and houses that have cables
    grid = Grid(batteries, costs_shared, int(district_num))

    # correct to right output format
    grid_output = correct_json(grid)

    # render output of grid
    output(grid_output)

    # output score
    print(get_costs(grid))

    # visualize output
    visualize(grid)


