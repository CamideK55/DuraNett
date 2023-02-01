# DuraNett
# Project of Programming Minor - SmartGrid

The transition to sustainable energy sources is one of the great challenges of modern times. Fossil fuels will have to be exchanged for sustainable alternatives. Solar energy is one of these alternatives. Our power grid, however, is not yet capable of storing all this energy. This project is an attempt to create a theoretical model of the most efficient grid possible, to maybe help towards a solution in this bigger problem. 

## Case
Within the case there are three neighborhoods with five batteries each and one hundred fifty houses. The goal is to minimize costs, given some validity requirements. 

The costs in our case are: 
- Battery-cost (5000 p/battery)
- Cable-costs (9 p/cable segment)

The validity requirements are:
- All houses are connected to a house
- None of the capacities of batteries is exceeded

The state-space of our case is enormous, yet there aren't a lot of valid states within this state-space. 

An old evaluation of one of our state-spaces (in Dutch):

<img src="Images/StateSpace.jpeg" width=500>

## Getting started

### Requirements

This codebase is written in Python 3.9+. For our visualisation we used the matplotlib package. This package is available for installation through the following commandline input:

> pip3 install matplotlib

### Usage

The main.py file in our repo is called SmartGrid.py.
To run our code the following usage key is used:

> python3 SmartGrid.py \<district number\> \<constructive algorithm\> optional: \<iterable algoritm\>

The commandline will show: \<distrct number\>, \<number of states visited\>, \<total costs of the grid\>

After running, a JSON file and PNG will be created in the /data directory. The JSON file displays a text-based version of our output, and the PNG visualises this output into a matplotlib scatterplot.

If you want to run the scripts, you need to to change the sys.path in which the JSON and PNG file are saved. You also need to use the other csv-loading script. 

### Structure

The following list describes the way our codebase is structured:

- /code
    - /code/algorithms: contains the code of the four algorithms
    - /code/classen: contains the code of the four classes
    - /code/future_work: contains code that was not finished in time, but can be important for future work
    - /code/scripts: contains the code for the scripts that were used in the experiments
    - /code/visualisation: contains the code for our visualisation
    - functions.py: collection of commonly used functions
    - SmartGrid.py: the main python file
- /data: contains the data that is used in our case and the results that are created
- /images: contains the images used in this README and the ones we used in our presentation 
- README.md

## Algorithms

### Random

The ranadom algorithm takes list of housen and batteries. Afterwards, it takes a random battery and a random houses and fills all batteries in this manner. Before placing the house, a check is done which looks at the batteries that are available for the placement of a house. If all batteries are full it takes a random battery, pops a house, and places the new house in the battery. The popped house is added to the list of houses to be placed. If the house does not fit in the battery, the mover is reversed, and the popped house is place back into the battery. In this case, the house that was to be placed, stays in the houses list, and another attempt is made to switch houses. This process is repeated until all houses are placed and no battery is overloaded. 


### Depth-first 

The depth-first search algorihm takes the batteries and houses. Afterwards, it places the houses in the batteries in such a way that the batteries are not overload, and returns the first solution that it finds. In practise the search will always go through the tree all the way to the bottom left, where it will find the first solution, as all houses are placed. 
 
### Hill Climber 

The Hill climber algorithm uses the output of either the Random or Depht-first algorithm. The algorithm changes the the state incrementaly, by switching two houses of two batteries. As the houses are being switched, new cables are set which results in different costs. If this results in a lower cost than before, the state is remembered and put through a new itteration.  The algorithm repeats this for a given number of iterations, in our case we use 500. This can be changed if needed. An issue with Hill Climber algorithms is that they can end up in local minima.

### Simulated Annealing

The Simulated Annealing algorithm uses the results of the Hill Climber, and tries to break out of the local minimum that it got stuck in. It does so by accepting states with higher costs. It uses a probabilty that increases when iterations increase. If a random float is lower than the calculated probability, the state is accepted.  It then checks if a new minimal costs has been found and repeats.

## Authors

- Joey Bink
- Jasper Claessen
- Camiel de Kom
