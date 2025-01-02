def calculator():
    choice = input("Enter operation (1:Add, 2:Subtract, 3:Multiply, 4:Divide): ")
    num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))

    if choice == '1': print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2': print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3': print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4': print(f"{num1} / {num2} = {num1 / num2}" if num2 != 0 else "Error! Division by zero.")
    else: print("Invalid choice.")

calculator()