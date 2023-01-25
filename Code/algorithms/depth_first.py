# ****************************************************************************
#  * depth_first.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * implementation of a depth_first algoritm
#  ***************************************************************************
# inspired by Radio Russia: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/depth_first.py
import copy
from classes.house import House
from classes.battery import Battery
from classes.grid_format import Grid
from functions import place_cables

depth = 5
class Depth_first:
    """
    Depth first algorithm which constructs a stack of grids, each with its own version of houses-batteries assignment
    """

    def __init__(self, batteries, houses):
        self.houses: list = copy.deepcopy(houses)
        self.batteries: list = copy.deepcopy(batteries)         #deepcopy?
        self.optional_state = [copy.deepcopy(self.batteries)]
        self.best_solution = [None]
        self.lowest_cost = float('inf')
        self.states_visted = 0
        self.archive = set()

    def next_state(self):
        return self.optional_state.pop()

    def create_children_OLD(self, batteries, house): 
        # get all possibilities for a house
        options = self.get_possibilities(batteries, house)

        # add a version of the batteries-houses to the stack, with a unique batteries combination
        for battery in options:
            new_batteries = copy.deepcopy(batteries)
            battery.houses.append(house)
            
            for new_battery in new_batteries:
                if new_battery.id == battery.id:
                    new_battery = battery

            print("child:",new_batteries)
            self.optional_state.append(new_batteries)
    

    def create_children(self, batteries, house): 
        # get all possibilities for a house

        #print("create child:",batteries,"house:",house)
        for index, battery in enumerate(batteries):
            #print("battery:",batteries[index])
            if not batteries[index].battery_check(house):
                new_batteries = copy.deepcopy(batteries)
                new_batteries[index].houses.append(house)
                print("child:",new_batteries)
                self.optional_state.append(new_batteries)

    
    
    def check_solutions(self, new_batteries):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = place_cables(new_batteries)[1]
        old_value = self.lowest_cost

        # We are looking for grids that cost less
        if new_value <= old_value:
            self.best_solution = new_batteries
            self.lowest_cost = new_value
            print(f"New lowest cost: {self.lowest_cost}")

    def run_old(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        new_batteries = None
        # for i in range(depth):
        while self.optional_state:
            new_batteries = self.next_state()
            print("state:",new_batteries)
            self.states_visted += 1
        
            for house in self.houses: # 
                print("house:",house)
                if not house.placed:
                    print("not placed")
                    self.create_children(new_batteries, house)
                    house.placed = True
                else:
                    continue
        
        self.check_solutions(new_batteries)
        
        print(self.states_visted)
        self.batteries = self.best_solution
        # print(self.best_solution)

        return self.batteries
    
    def depth_first_recursive_old(self,batteries,houses):
        print("batteries:",batteries, "houses:",houses)
        for index,h in enumerate(houses):
            for b in batteries:
                if b.battery_check(h):
                    b.houses.append(houses[index])
                    houses.pop(index)
                    # self.depth_first_recursive(batteries,houses)
                    houses.insert(index,h)
                    b.houses.pop()

    def depth_first_recursive(self,batteries,houses,house_index):
        if house_index==len(houses):
            print("batteries:",batteries,"house_index:",house_index)
            self.done=True
        #for index,h in enumerate(houses):
        if not self.done:
            for index in range(house_index,len(houses)):
                for b in batteries:
                    if not self.done and not b.battery_check(houses[house_index]):
                        b.houses.append(houses[index])
                        self.depth_first_recursive(batteries,houses,house_index+1)
                        b.houses.pop()

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        self.done=False
        self.depth_first_recursive(self.batteries,self.houses,0)
                
        
    # move to class as method
    def get_possibilities(self, batteries, house):
        """
        returns a list of available batteries in which the house could be included, based on the current 
        capacity of the battery and total output of the houses 
        """
        available_opt = set(batteries)
        unavailable_opt = set()
        for battery in batteries:
            if battery.battery_check(house):
                unavailable_opt.add(battery)
                
        return list(available_opt - unavailable_opt)
        