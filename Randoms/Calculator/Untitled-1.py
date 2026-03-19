def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication (x,y):
    return x * y
def division(x,y):
    return x / y

while True:
    print("""
 Calculator App
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division         
          """)
    
    choice = input("Choose arithmic operation (1,2,3,4): ")

    if choice in ("1","2","3","4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter Second Number"))
        
        except ValueError:
            print("Invalid")
            continue

        if choice == "1":
            print(f"{num1} + {num2} = {addition(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")
        elif choice =="4":
            if num2 == 0:
                print("Math Error, Cannot divide by zero.")
            ## Why num2 only? 0/5 = 0 but 5/0 = math error
                continue
            else:
                print(f"{num1} / {num2} = {division(num1, num2)}")

        
        continue_calculating = input(f"\nContinue Calculating? (Y/N): ").upper()
        if continue_calculating == "N":
            print("Exiting Calculator. Goodbye!")
            break
        elif continue_calculating == "Y":
            print("\n")
            continue
    else:
        print("Invalid Choice. Please pick 1, 2, 3, or 4.")