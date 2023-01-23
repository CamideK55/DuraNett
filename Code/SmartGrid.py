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
from algorithms import hill_climber as hc
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

    # ------------ Place houses in batteries according to algorithms ------------

    # --------------------------- Random reassignment --------------------------
    # for i in range(15):
    batteries = randomize.valid_random_assignment(batteries, houses)

    # --------------------------- Place cables ---------------------------------
    batteries, costs_shared = place_cables(batteries)                          

    # -------- Update grid with batteries and houses that have cables ----------
    grid = Grid(batteries, costs_shared, int(district_num))
    print(grid.total_costs())

    # ------------------------------- Hill Climber ------------------------------
    climber = hc.HillClimber(grid)

    climber.run(10)
    


    # costs_shared2 = grid.total_costs()

    # grid2 = Grid(batteries, costs_shared2, int(district_num))



    # # --------------------- correct to right output format ---------------------
    grid_output = correct_json(grid)

    # # ----------------------- Render output of grid ------------------------
    # # 
    # output(grid_output)

    # # output score
    # print(get_costs(grid))

    # # visualize output
    # visualize(grid)


