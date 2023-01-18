class Cable:
    def __init__(self, x, y) -> None:
        """ post: list of coordinates on which the cable runs """
        self.location = tuple((x, y))

    def __repr__(self) -> str:
        return f"{self.location}"