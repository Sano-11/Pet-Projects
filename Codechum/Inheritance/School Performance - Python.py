class Performer:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age


class Dancer(Performer):
    def __init__(self, name: str, age: int, dance_style: str):
        super().__init__(name, age)
        self._dance_style = dance_style

    def get_dance_style(self) -> str:
        return self._dance_style

    def dance(self) -> None:
        print(f"{self.get_name()} is performing {self._dance_style} dance.")

class Singer(Performer):
    def __init__(self, name: str, age: int, vocal_range: str):
        super().__init__(name, age)
        self._vocal_range = vocal_range

    def get_vocal_range(self) -> str:
        return self._vocal_range

    def sing(self) -> None:
        print(f"{self.get_name()} is singing with a {self._vocal_range} range.")