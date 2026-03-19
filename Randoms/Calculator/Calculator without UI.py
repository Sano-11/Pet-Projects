def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print("""
Select Operation
[1] Add
[2] Subtract
[3] Multiply
[4] Divide
""")
    
    userchoice = input("Enter Choice: ")
    
    if userchoice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
            ## IF num1 or num2 is a str, it displays this
            print("Invalid Input, please enter a number")
            continue

        if userchoice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif userchoice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif userchoice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif userchoice == "4":
            if num2 == 0:
                print("Math Error, Cannot divide by zero.")
                ## Why num2 only? 0/5 = 0 but 5/0 = math error
                continue
            else:
                print(f"{num1} / {num2} = {divide(num1, num2)}")

        
        continue_calculating = input(f"\nContinue Calculating? (Y/N): ").upper()
        if continue_calculating == "N":
            print("Exiting Calculator. Goodbye!")
            break
        elif continue_calculating == "Y":
            print("\n")
            continue
    else:
        print("Invalid Choice. Please pick 1, 2, 3, or 4.")