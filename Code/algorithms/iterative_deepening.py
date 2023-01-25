from depth_first import Depth_first

class IDS(Depth_first):
    def __init__(self) -> None:
        self.infinite = int('inf')
    
    def iteration(self):
        for depth in range(0, self.infinite):
            found, remaining = Depth_first.run(self)
            if found != None:
                return found
            elif not remaining:
                return None
