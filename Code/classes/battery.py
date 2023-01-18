class Battery:
    def __init__(self, x: int, y: int, capacity: float, unique_id: int) -> None:
        """ post:  """ 
        # self.id = unique_id
        self.location = tuple((x,y))
        self.capacity = capacity
        self.houses = []
        self.total_output_houses = 0

    def battery_capacity_not_overloaded(self):
        if self.total_output_houses <= self.capacity:
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return f"{self}"
        