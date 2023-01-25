class Battery:
    def __init__(self, x: int, y: int, capacity: float, unique_id: int) -> None:
        """ post:  """ 
        self.id = unique_id
        self.location = (x,y)
        self.x = x
        self.y = y
        self.capacity = capacity
        self.houses = []
        self.total_output_houses = 0
        self.cost = 5000

    def battery_capacity_overloaded(self):
        if self.total_output_houses <= self.capacity:
            return False
        else:
            return True

    def battery_check(self, house):
        print(f"{self.total_output_houses} + {house.output} > {self.capacity}")
        if self.total_output_houses + house.output > self.capacity:
            return True
        return False

    def empty_batteries(self):
        self.houses = []
        self.total_output_houses = 0
    
    def __repr__(self) -> str:
        return f"{self.houses}"
        