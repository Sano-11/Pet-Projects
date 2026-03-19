class Rectangle:
    # Adding = 0.0 makes these arguments optional
    def __init__(self, length=0.0, width=0.0):
        self.length = float(length)
        self.width = float(width)

    def get_area(self) -> float:
        return self.length * self.width
    
# Create an instance of Rectangle
my_rectangle = Rectangle(5.0, 4.0)

# Invoke the method
area = my_rectangle.get_area()

print(f"Action: Invoking get_area() method of the Rectangle")
print(f"Result: {area}")