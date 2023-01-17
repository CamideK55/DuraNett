import random
import copy
from classes import Cable

# https://github.com/minprog/radio_russia_demo/blob/college_1/code/algorithms/randomise.py
possibilities = range(50)

def random_assignment(batteries: list, houses: list):
    """
    Randomly assign each cable with one of the possibilities.
    """

    while len(houses) > 0:
        for battery in range(len(batteries)):
            random.shuffle(houses)
            index = random.choice(range(len(houses)))
            batteries[battery].battery_dict["houses"].append(houses[index].house_dict)
            houses.pop(index)
    
    return batteries

    # places cables randomly from houses to batteries
    # for battery in batteries:
    #     for house in houses:
    #         for i in range(random.choice(possibilities)):
    #             x = random.choice(possibilities)
    #             y = random.choice(possibilities)
    #             cable = Cable(x, y)
    #             house.house_dict["cables"].append(cable)
            
    # return batteries, houses


# def random_reconfigure_node(graph, node):
#     """
#     Takes a node and assigns each node with one of the possibilities.
#     """
#     node.value = random.choice(possibilities)


# def random_reconfigure_nodes(graph, nodes):
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

#     return new_graph