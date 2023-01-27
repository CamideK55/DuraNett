from classes.cable import Cable
from classes.grid_format import Grid

class House:
    def __init__(self, x: int, y: int, max_output: float, unique_id: int) -> None:
        # self.id = unique_id - not sure if needed
        self.location = tuple((x, y))
        self.output = max_output
        self.cables = []
        self.placed = False

    def empty_cables(self):
        self.cables = []
        self.placed = False

    def placing_cable(self, battery, grid):
        location_battery = list(battery.location)

        bat_locations = [(x,y) for x,y,b in grid.all_cables if b == battery] + [battery.location]

        # location_battery = functie(self.location, bat_locations)

        location_cable = list(self.location)
        cable_costs = 0

        # search for an equal x ---- merge de twee while-loops naar een functie, 0-1 locatie
        # while location_cable[0] != bat_locations[0]:
        while location_cable[0] != location_battery[0]:
            if location_cable[0] > location_battery[0]:
                if not grid.same_cables((location_cable[0], location_cable[1], battery)):
                    grid.all_cables.add((location_cable[0], location_cable[1], battery))     

                    self.cables.append(Cable(location_cable[0], location_cable[1]))
                    location_cable[0] -= 1
                    cable_costs += 9
                else:
                    location_cable[0] -= 1
                    continue
            else:
                if not grid.same_cables((location_cable[0], location_cable[1], battery)):
                    grid.all_cables.add((location_cable[0], location_cable[1], battery))                    
                    self.cables.append(Cable(location_cable[0], location_cable[1]))
                    location_cable[0] += 1
                    cable_costs += 9
                else:
                    location_cable[0] += 1
                    continue
        
        # grid.all_cables.add((location_cable[0], location_cable[1]))                    
        self.cables.append(Cable(location_cable[0], location_cable[1]))
        cable_costs += 9

        # search for an equal y
        # while location_cable[1] != bat_locations[1]:
        while location_cable[1] != location_battery[1]:
            if location_cable[1] > location_battery[1]:
                if not grid.same_cables((location_cable[0], location_cable[1], battery)):
                    grid.all_cables.add((location_cable[0], location_cable[1], battery))
                    self.cables.append(Cable(location_cable[0], location_cable[1]))
                    location_cable[1] -= 1
                    cable_costs += 9
                else:
                    # print("continue1")
                    location_cable[1] -= 1
                    continue
            else:
                if not grid.same_cables((location_cable[0], location_cable[1], battery)):
                    grid.all_cables.add((location_cable[0], location_cable[1], battery))                    
                    self.cables.append(Cable(location_cable[0], location_cable[1]))
                    location_cable[1] += 1
                    cable_costs += 9
                else:
                    # print("continue2")
                    location_cable[1] += 1
                    continue
        
        grid.all_cables.add((location_cable[0], location_cable[1], battery))                    
        self.cables.append(Cable(location_cable[0], location_cable[1]))
        cable_costs += 9
    
        return cable_costs

    def __repr__(self):
        return f"{self.location}"
