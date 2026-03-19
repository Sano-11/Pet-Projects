class Student:
    # Adding default values makes these arguments optional for the tester
    def __init__(self, id_number: int = 0, name: str = "", course: str = ""):
        self.id_number = id_number
        self.name = name
        self.course = course

    def __str__(self) -> str:
        return f"{self.id_number} - {self.name} - {self.course}"

    def validate_info(self) -> None:
        # We check if the ID is 9 digits and the name is only letters/spaces
        name_valid = self.name.replace(" ", "").isalpha()
        id_valid = len(str(self.id_number)) == 9
        
        if name_valid and id_valid:
            print("Student information is valid.")
        else:
            print("Student information is not valid.")