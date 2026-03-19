class Person:
    def __init__(self, name: str, age: int, gender: str):
        self._name = name
        self._age = age
        self._gender = gender

    # Getters
    def get_name(self) -> str: return self._name
    def get_age(self) -> int: return self._age
    def get_gender(self) -> str: return self._gender

    # Setters
    def set_name(self, name: str): self._name = name
    def set_age(self, age: int): self._age = age
    def set_gender(self, gender: str): self._gender = gender

    def is_minor(self) -> bool:
        return self._age < 18

    def __str__(self) -> str:
        return f"{self._name} - {self._age} - {self._gender}"
    

class Father(Person):
    def __init__(self, name: str, age: int):
        # Always passes 'M' as the gender
        super().__init__(name, age, 'M')

    def introduce_with_style(self, n: int) -> None:
        for i in range(n):
            # i starts at 0, so 0 spaces, 1 space, 2 spaces...
            print(" " * i + "I am your father")
        
class Son(Father):
    # Set name default to "Unknown"
    def __init__(self, name: str = "Unknown", age: int = 0):
        super().__init__(name, age)

    def introduce_with_style(self, n: int) -> None:
        # We need decreasing spaces. 
        # If n is 4, spaces should be 3, 2, 1, 0.
        for i in range(n - 1, -1, -1):
            print(" " * i + "I am your son")