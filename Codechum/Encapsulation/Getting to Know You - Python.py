class Person:
    # Adding default values makes these arguments optional
    def __init__(self, name: str = "None", age: int = 0, gender: str = "None"):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_age(self) -> int:
        return self.age

    def set_age(self, age: int) -> None:
        # Validation: age should be positive
        if age > 0:
            self.age = age

    def get_gender(self) -> str:
        return self.gendera

    def set_gender(self, gender: str) -> None:
        # Validation: ensuring it's either 'M' or 'F'
        if gender == 'M' or gender == 'F':
            self.gender = gender