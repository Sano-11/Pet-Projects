class Money:
    # We set default values for both amount and denomination
    def __init__(self, amount: int = 0, denomination: str = "Unknown"):
        self.amount = amount
        self.denomination = denomination