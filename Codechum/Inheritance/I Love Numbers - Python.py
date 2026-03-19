class Number:
    def __init__(self, value: int):
        self._value = value

    def get_value(self) -> int:
        return self._value

    def set_value(self, value: int):
        self._value = value

class DecimalNumber(Number):
    def __init__(self, value: int, decimal_places: int):
        super().__init__(value)
        self._decimal_places = decimal_places

    # Getters and Setters
    def get_decimal_places(self) -> int:
        return self._decimal_places

    def set_decimal_places(self, decimal_places: int):
        self._decimal_places = decimal_places

    def multiply(self, decimal_number: 'DecimalNumber') -> None:
        # Multiply the integer values
        new_value = self.get_value() * decimal_number.get_value()
        self.set_value(new_value)
        # Add the decimal places together
        self._decimal_places += decimal_number.get_decimal_places()

    def __str__(self) -> str:
        val_str = str(self.get_value())
        # Ensure the string is long enough by padding with leading zeros
        # if the value is 10 and places is 3, we need "010"
        padded_val = val_str.zfill(self._decimal_places)
        
        # Split into the part before and after the dot
        # If padded_val is "010" and places is 3, it becomes "0.010"
        if self._decimal_places == 0:
            return val_str
        
        # Logic to place the decimal point correctly
        if len(padded_val) <= self._decimal_places:
            return "0." + padded_val.zfill(self._decimal_places)
        else:
            split_pos = len(padded_val) - self._decimal_places
            return padded_val[:split_pos] + "." + padded_val[split_pos:]
    

class WholeNumber(Number):
    def __init__(self, value: int):
        super().__init__(value)

    def multiply(self, whole_number: 'WholeNumber') -> None:
        # Multiply current value by the value of the passed WholeNumber object
        new_value = self.get_value() * whole_number.get_value()
        self.set_value(new_value)

    def __str__(self) -> str:
        return str(self.get_value())