class Bird:
    # Defining default values directly in the parameter list
    def __init__(self, breed: str = "Unknown", is_nocturnal: bool = False):
        self.breed = breed
        self.is_nocturnal = is_nocturnal