# ****************************************************************************
#  * SmartGrid.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  *   ----
#  ***************************************************************************

from classes.grid_format import Grid
from functions import load, output, house_into_batteries, run_random, place_cables, get_costs, correct_json
from visualisation.visualisation import visualize
from algorithms import randomize
from algorithms import depth_first as df
from algorithms import hill_climber as hc
from algorithms import simulatedannealing as sa
from algorithms import random as rand
import sys

commands1 = ['-r', '-d']
commands2 = ['-hc', '-sa']


def error_message():       
    print("Usage: SmartGrid.py <district number> <constructive algorithm> optional: <iterable algorithm> \n")
    print("COMMAND LINE OPTIONS")
    print("district number: 0, 1, 2, 3")
    print(f"base algorithm: {commands1}")
    print(f"top algorithm: {commands2}")
    exit(1)


if __name__ == "__main__":
   
    # check if input is valid
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        error_message()
        
    # retrieve user input from command-line
    district_num = sys.argv[1]

    # retrieve constructive algorithm
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        constructive = sys.argv[2].lower()
        if constructive not in commands1:
            error_message()
    else:
        error_message()

    # retrieve top algorithm
    if len(sys.argv) == 4:
        iterable = sys.argv[3]
        if iterable not in commands2:
            error_message()
    else:
        iterable = None

    # loading csv file to the program
    # batteries: list = load(f"../Data/district_{district_num}/district-{district_num}_batteries.csv")
    # houses: list = load(f"../Data/district_{district_num}/district-{district_num}_houses.csv")
    
    # loading csv file to the scripts
    batteries: list = load(f"../../Data/district_{district_num}/district-{district_num}_batteries.csv")
    houses: list = load(f"../../Data/district_{district_num}/district-{district_num}_houses.csv")


    # initialize the grid
    grid = Grid(batteries, houses, int(district_num))

    # --------------- Run either of the two constructive base algorithms --------------
    
    #                                   1.
    # --------------------------- Random reassignment ---------------------------

    # start random algorithm
    if constructive == '-r':
      random = rand.Random(grid)
      grid = random.run()
      print(random.state_counter)
      
    #                                   2.
    #------------------------- Depth first search -------------------------------

    # start depth first search algorithm
    else:

        # initialize the depth first object
        depth = df.Depth_first(grid)

        # run the the depth algortithm
        grid = depth.run()
        
        # place the cables from the houses to their batteries
        costs_shared = place_cables(grid.batteries, grid)[1]
        print(costs_shared)


    # ---------------- Run either of the two iterable algorithms ----------------

    # ------------------------------- Hill Climber ------------------------------

    # start hill climber algorithm
    if iterable == '-hc':
        print("Starting Hill Climber")

        # sets the total amount of iterations for running th algorithm
        HillClimber_iterations = 500

        # initialize hill climber algorithm 
        hillclimber = hc.HillClimber(grid)

        # run the algorithm
        grid = hillclimber.run(HillClimber_iterations)

    # --------------------------- Simmulated Annealing --------------------------

    # start simulated annealing algorithm
    elif iterable == '-sa':
        print("Starting Simmulated Annealing")

        # initialize Simulated Annealing algorithm
        siman = sa.SimulatedAnnealing(grid, 40)

        # run the algorithm
        grid = siman.run(500)
   
    #--------------------- correct to right output format -----------------
   
    grid_output = correct_json(grid)

    #----------------------- Render output of grid ------------------------
    
    output(grid_output)

    # # output score
    # print(grid.total_costs_II)
    print(grid.total_costs())

    # visualize output
    visualize(grid)


