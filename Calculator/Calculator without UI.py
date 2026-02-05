import math






def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("""

Calculator type shi

Select Operation

[1] Add
[2] Subtract
[3] Multiply
[4] Divide

""")

while True:

    userchoice = input("Enter Choice")
    if userchoice in ("1","2","3","4"):
        try:
            num1 = input("Enter first number")
        except ValueError:
            print
            








