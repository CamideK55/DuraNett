from classes.cable import Cable
from classes.grid_format import Grid

class House:
    def __init__(self, x: int, y: int, max_output: float, unique_id: int) -> None:
        # self.id = unique_id - not sure if needed
        self.location = tuple((x, y))
        self.output = max_output
        self.cables = []
        self.placed = False

    def empty_cables(self, grid, battery):

        bat_locations = [(x,y) for x,y,b in grid.all_cables if b == battery] + [battery.location]
        bat_locations.sort()
        counter=0
        neighbours = []
        remove_location = self.location
        loop = True

        # print("Start looping through house cables")
    
        while loop == True:
            if remove_location in bat_locations:
                if (remove_location[0] + 1, remove_location[1]) in bat_locations:
                    counter += 1
                    print(f"counter: {counter}")
                    neighbours.append((remove_location[0] + 1, remove_location[1], battery))

                if (remove_location[0], remove_location[1] + 1) in bat_locations:
                    counter += 1
                    print(f"counter: {counter}")
                    neighbours.append((remove_location[0], remove_location[1] + 1, battery))

                if (remove_location[0] - 1, remove_location[1]) in bat_locations:
                    counter += 1
                    print(f"counter: {counter}")
                    neighbours.append((remove_location[0] - 1, remove_location[1], battery))

                if (remove_location[0], remove_location[1] - 1) in bat_locations:
                    counter += 1
                    print(f"counter: {counter}")
                    neighbours.append((remove_location[0], remove_location[1] - 1, battery))
            else:
                loop = False

            if counter >= 2:
                loop = False
            elif counter == 1:
                remove_location = neighbours[-1]
                counter = 0
            print(counter)

        for neighbour in neighbours:
            # print(grid.all_cables)
            if neighbour in grid.all_cables:
                grid.all_cables.discard(neighbour)
                
        
        self.cables = []

        # for cable in self.cables:
        #     grid.all_cables.discard(tuple((cable.x, cable.y, battery)))
        # self.cables = []

        # if grid.all_cables[2] == battery:
        #     for x,y in grid.all_cables:
        #         print(x)
        #         for xc,yc in self.cables:
        #             if xc == x and yc == y:
        #                 grid.all_cables.remove(x,y)
        #                 print("Removing cable from all cables")

        self.placed = False

    def placing_cable(self, battery, grid):
        location_battery = list(battery.location)

        bat_locations = [(x,y) for x,y,b in grid.all_cables if b == battery] + [battery.location]

        bat_locations.sort()

        # print(bat_locations)


        location_battery = self.closest_battery(self.location, bat_locations)

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

    def closest_battery(self, location_house, locations_battery):
        closest_location = tuple((51, 51))

        # closest_location = location_battery

        for location_battery in locations_battery:
            if abs(location_battery[0] - location_house[0]) <= closest_location[0] and abs(location_battery[1] - location_house[1]) <= closest_location[1]:
                closest_location = location_battery
        return closest_location


    def __repr__(self):
        return f"{self.location}"
