class Beverage:
    def __init__(self, name: str, volume: int, is_chilled: bool):
        self._name = name
        self._volume = volume
        self._is_chilled = is_chilled

    def is_empty(self) -> bool:
        return self._volume == 0

    def __str__(self) -> str:
        status = "is still chilled" if self._is_chilled else "is not chilled anymore"
        return f"{self._name} ({self._volume}mL) {status}"

    def get_name(self) -> str:
        return self._name

    def get_volume(self) -> int:
        return self._volume

    def get_is_chilled(self) -> bool:
        return self._is_chilled
    
class Beer(Beverage):
    def __init__(self, volume: int, is_chilled: bool, alcoholic_content: float):
        # Call the parent constructor
        super().__init__("Beer", volume, is_chilled)
        # Change double underscore to single underscore here
        self._alcoholic_content = alcoholic_content

    def get_type(self) -> str:
        if self._alcoholic_content < 0.03:
            return "Flavored"
        elif self._alcoholic_content < 0.06:
            return "Regular"
        else:
            return "Strong"

    def __str__(self) -> str:
        # super().__str__() gives us "Beer (330mL) is still chilled."
        # We strip the period to add the extra info.
        base_str = super().__str__().rstrip('.')
        # Use :.1f to ensure exactly one decimal place
        return f"{base_str} ({self._alcoholic_content * 100:.1f}% alcoholic content)."

    def get_alcoholic_content(self) -> float:
        return self._alcoholic_content

class Water(Beverage):
    # Set type to have a default value of "" (empty string)
    def __init__(self, volume: int, is_chilled: bool, type: str = ""):
        super().__init__("Water", volume, is_chilled)
        
        # Now handle the "if type is empty" logic
        if type == "" or type is None:
            self._type = "Regular"
        else:
            self._type = type

    def get_type(self) -> str:
        return self._type