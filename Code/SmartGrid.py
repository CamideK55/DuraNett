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
from algorithms import depth_first as df
from algorithms import hill_climber as hc
from algorithms import simulatedannealing as sa
from algorithms import random as rand
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

    #------------------------- Depth first search -------------------------------
    # depth = df.Depth_first(batteries, houses)
    # batteries = depth.run()
    # print("states:", depth.states_visted)


    # -------- Update grid with batteries and houses that have cables ----------
    # costs_shared = int(depth.lowest_cost)
    grid = Grid(batteries, houses, int(district_num))
    

    # --------------------------- Random reassignment --------------------------
    # for i in range(15):
    # batteries = randomize.valid_random_assignment(batteries, houses)
    
    random = rand.Random(grid)
    grid_new = random.run()

    total_houses_sum = 0
    for battery in grid_new.batteries:
        print(battery.total_output_houses)
        total_houses = len(battery.houses)
        # print(total_houses)
        total_houses_sum += total_houses
    print(f"Total houses in batteries is {total_houses_sum}")

    grid_new.batteries, costs_shared = place_cables(grid_new.batteries, grid_new)      
    

    print(grid_new.total_costs())
    # print(grid.batteries)

    # ------------------------------- Hill Climber ------------------------------
    # climber = hc.HillClimber(grid)
    # climber.run(2000)
    
    # --------------------------- Simmulated Annealing --------------------------
    # print("Starting Simmulated Annealing")
    # siman = sa.SimulatedAnnealing(grid, 40)
    # siman.run(10000)

    # costs_shared2 = grid.total_costs()

    # grid2 = Grid(batteries, costs_shared2, int(district_num))



    # # --------------------- correct to right output format ---------------------
    grid_output = correct_json(grid_new)

    # # ----------------------- Render output of grid ------------------------
    # # 
    output(grid_output)

    # # output score
    # print(get_costs(grid))

    # visualize output
    visualize(grid_new)


