class Beverage:
    def __init__(self, flavor: str = "Unknown", color: str = "Unknown"):
        self.flavor = flavor
        self.color = color

class Bottle:
    def __init__(self, mL: int, flavor: str = "Unknown", color: str = "Unknown"):
        self.mL = mL
        # We create the Beverage object right here
        self.beverage = Beverage(flavor, color)