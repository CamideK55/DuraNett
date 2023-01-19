class House:
    def __init__(self, x: int, y: int, max_output: float, unique_id: int) -> None:
        # self.id = unique_id - not sure if needed
        self.location = tuple((x, y))
        self.output = max_output
        self.cables = []

    def empty_cables(self):
        self.cables = []

    def __repr__(self):
        return f"{self.location}"
