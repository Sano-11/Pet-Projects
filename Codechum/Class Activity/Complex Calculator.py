import math

class ComplexCalculator:
    def get_square_root(self, number: int) -> float:
        if number < 0:
            return 0.0
        return float(math.sqrt(number))

    def get_factorial(self, number: int) -> int:
        if number < 0:
            return 0
        return math.factorial(number)

    def get_sum(self, number1: int, number2: int) -> float:
        return float(number1 + number2)

    def get_product(self, number1: int, number2: int) -> float:
        return float(number1 * number2)

    def get_difference(self, number1: int, number2: int) -> float:
        return float(number1 - number2)

    def get_quotient(self, number1: int, number2: int) -> float:
        if number2 == 0:
            return 0.0
        return float(number1 / number2)