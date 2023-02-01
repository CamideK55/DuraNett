class Battery:
    def __init__(self, x: int, y: int, capacity: float, unique_id: int) -> None:
        """
        Initializes the instance attributes.
        """ 
        self.id = unique_id
        self.location = (x,y)
        self.x = x
        self.y = y
        self.capacity = capacity
        self.houses = []
        self.total_output_houses = 0
        self.cost = 5000

    def battery_capacity_overloaded(self) -> bool:
        """
        Returns False if Battery is not overloaded, True if it is.
        """
        if self.total_output_houses <= self.capacity:
            return False
        else:
            return True

    def battery_check(self, house) -> bool:
        """
        Returns True if a house would 'fit' in the Battery network.
        """
        if self.total_output_houses + house.output > self.capacity:
            return True
        return False

    def empty_batteries(self):
        """
        Empties the houses list and set the total output to zero accordingly.
        """
        self.houses = []
        self.total_output_houses = 0
    
    def __repr__(self) -> str:
        return f"{self.houses}"
        