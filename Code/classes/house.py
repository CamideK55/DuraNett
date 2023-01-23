from classes.cable import Cable

class House:
    def __init__(self, x: int, y: int, max_output: float, unique_id: int) -> None:
        # self.id = unique_id - not sure if needed
        self.location = tuple((x, y))
        self.output = max_output
        self.cables = []

    def empty_cables(self):
        self.cables = []

    def placing_cable(self, battery):
        location_battery = list(battery.location)
        location_cable = list(self.location)
        cable_costs = 0

        # search for an equal x
        while location_cable[0] != location_battery[0]:
            if location_cable[0] > location_battery[0]:
                self.cables.append(Cable(location_cable[0], location_cable[1]))
                location_cable[0] -= 1
                cable_costs += 9
            else:
                self.cables.append(Cable(location_cable[0], location_cable[1]))
                location_cable[0] += 1
                cable_costs += 9
        self.cables.append(Cable(location_cable[0], location_cable[1]))
        cable_costs += 9

        # search for an equal y
        while location_cable[1] != location_battery[1]:
            if location_cable[1] > location_battery[1]:
                self.cables.append(Cable(location_cable[0], location_cable[1]))
                location_cable[1] -= 1
                cable_costs += 9
            else:
                self.cables.append(Cable(location_cable[0], location_cable[1]))
                location_cable[1] += 1
                cable_costs += 9
        self.cables.append(Cable(location_cable[0], location_cable[1]))
        cable_costs += 9
    
        return cable_costs

    def __repr__(self):
        return f"{self.location}"
