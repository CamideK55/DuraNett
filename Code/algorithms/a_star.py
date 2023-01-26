from queue import PriorityQueue

class a_star:
    def __init__(self, batteries) -> None:
        self.batteries = batteries

        # self.houses =
        # self.pathfinding_location = self.start_location
        # self.target_location = target.location
        # self.cost = 9 * (abs(start.location[0] - target.location[0]) + abs(start.location[1] - target.location[1]))
        self.open = []
        self.closed = []
        # self.closed.append(start.location)
        self.cable_list = []

    def pathfinding(self, start, target):
        path = start.location
        while path != target.location:
            pass

    def run(self):
        for battery in self.batteries:
            for house in battery.houses:
                self.pathfinding(house, battery)

