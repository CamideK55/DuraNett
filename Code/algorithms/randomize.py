import sys

sys.path.append('.../')

import random
import copy
from functions import batteries_capacity_check
from classes.battery import Battery
from classes.grid_format import Grid
# from .. import functions

# https://github.com/minprog/radio_russia_demo/blob/college_1/code/algorithms/randomise.py
possibilities = range(50)

# def random_assignment(batteries: list, houses: list):
#     """
#     Randomly assign each cable with one of the possibilities.
#     """
#     for battery in batteries:
#         for house in battery.houses:
#             house.empty_cables()
#         battery.empty_batteries()
#     while len(houses) > 0:
#         print("houses list is not empty")
#         for battery in batteries:
#             random.shuffle(houses)
#             index = random.choice(range(len(houses)))
#             print(f"total output houses is {battery.total_output_houses}")
#             print(f"total capacity is {battery.capacity}")
#             print(f"house output is {houses[index].output}")
#             if battery.battery_check(houses[index]):
#                 continue
#             battery.houses.append(houses[index])
#             battery.total_output_houses += houses[index].output
#             houses.pop(index)
    
        
        # for i, house in enumerate(houses):
        #     index = random.choice(range(len(batteries)))
        #     battery = batteries[index]
        #     print(index)
        #     print(f"total output houses is {battery.total_output_houses}")
        #     print(f"total capacity is {battery.capacity}")
        #     print(f"house output is {house.output}")
        #     # print("looping through houses")
        #     if battery.battery_check(house):
        #         print("Capacity overloaded")
        #         continue
            
        #     battery.houses.append(house)
        #     battery.total_output_houses += house.output
        #     print("House added to battery", {i})
        #     houses.pop(i)


        # for house in houses:
        #     index = random.randint(0, 4)
        #     battery = batteries[index]
        #     if battery.battery_check(house):
        #         continue
        #     else:
        #         battery.houses.append(house)
        #         battery.total_output_houses += house.output
        #         houses.pop()
    # return batteries


    
def valid_random_assignment(batteries: list, houses: list):
    i = 1
    while True:
        batteries, houses = random_assignment(batteries, copy.deepcopy(houses))
        print(f" This is try {i} for a valid solution")
        i += 1 
        for battery in batteries:
            overgebleven_capacity = battery.capacity - battery.total_output_houses
            # print(f"overgebleven capatiteit = {overgebleven_capacity}")
        if batteries_capacity_check(batteries) and len(houses) == 0:
            print("valid solution")
            break
    print(houses)
    return batteries




# def random_assignment(graph, possibilities):
#     """
#     Randomly assign each node with one of the possibilities.
#     """
#     for node in graph.nodes.values():
#         node.value = random.choice(possibilities)


# def random_reconfigure_node(graph, node, possibilities):
#     """
#     Takes a node and assigns each node with one of the possibilities.
#     """
#     node.value = random.choice(possibilities)


# def random_reconfigure_nodes(graph, nodes, possibilities):
#     """
#     Takes a list of nodes and assigns each node with one of the possibilities.
#     """
#     for node in nodes:
#         random_reconfigure_node(graph, node, possibilities)


# def random_reassignment(graph, possibilities):
#     """
#     Algorithm that reassigns nodes that are invalid until each node is valid.
#     CAUTION: may run indefinitely.
#     """
#     new_graph = copy.deepcopy(graph)

#     # Randomly assign a value to each of the nodes
#     random_assignment(new_graph, possibilities)

#     # Find nodes that are "violations" and have neighbours with same value
#     violating_nodes = new_graph.get_violations()

#     # While we have violations
#     while len(violating_nodes):
#         # Reconfigure violations randomly
#         random_reconfigure_nodes(new_graph, violating_nodes, possibilities)

#         # Find nodes that are violations
#         violating_nodes = new_graph.get_violations()

#     return









def random_assignment(batteries, houses):
    for battery in batteries:
        for house in battery.houses:
            house.empty_cables()
        battery.empty_batteries()
    tries = 0

    print("still trying")
    while len(houses) > 0 and tries < 30:
        for i, house in enumerate(houses):
            battery = batteries[random.choice(range(len(batteries)))]
            print(battery.id)
            print(f"total output houses is {battery.total_output_houses}")
            print(f"total capacity is {battery.capacity}")
            print(f"house output is {houses[i].output}")
            if battery.battery_check(house):
                tries += 1
                print(f"These are the tries {tries}")
                continue
            battery.houses.append(house)
            battery.total_output_houses += houses[i].output
            houses.pop(i)

    return batteries, houses
        
        