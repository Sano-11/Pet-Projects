class Car:
    def __init__(self, color: str = "", price: float = 0.0, size: str = "M"):
        self.color = color
        self.price = price
        # Standardize size to uppercase immediately
        self.size = size.upper()

    # Getter Methods
    def get_color(self) -> str:
        return self.color

    def get_price(self) -> float:
        return self.price

    def get_size(self) -> str:
        return self.size

    # Setter Methods
    def set_color(self, color: str) -> None:
        self.color = color

    def set_price(self, price: float) -> None:
        self.price = price

    def set_size(self, size: str) -> None:
        # Update and ensure uppercase
        self.size = size.upper()

    def __str__(self) -> str:
        # 1. Determine size descriptor based on character
        descriptors = {
            'S': 'small',
            'M': 'medium',
            'L': 'large'
        }
        size_desc = descriptors.get(self.size, "unknown")

        # 2. Return formatted string with 2 decimal places for price
        return f"Car ({self.color}) - P{self.price:.2f} - {size_desc}"