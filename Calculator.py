# Professional Python Calculator
# This script performs basic and advanced arithmetic operations
# such as addition, subtraction, multiplication, division,
# power, square root, and modulus.

import math


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        """Add two numbers."""
        self.result = num1 + num2
        return self.result

    def subtract(self, num1, num2):
        """Subtract second number from the first."""
        self.result = num1 - num2
        return self.result

    def multiply(self, num1, num2):
        """Multiply two numbers."""
        self.result = num1 * num2
        return self.result

    def divide(self, num1, num2):
        """Divide first number by the second. Handles division by zero."""
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        self.result = num1 / num2
        return self.result

    def power(self, base, exponent):
        """Return the result of base raised to the exponent."""
        self.result = math.pow(base, exponent)
        return self.result

    def sqrt(self, num):
        """Return the square root of a number."""
        if num < 0:
            raise ValueError("Cannot take the square root of a negative number!")
        self.result = math.sqrt(num)
        return self.result

    def modulus(self, num1, num2):
        """Return the remainder when num1 is divided by num2."""
        self.result = num1 % num2
        return self.result

    def clear(self):
        """Clear the result."""
        self.result = 0
        return self.result

    def get_result(self):
        """Get the current result."""
        return self.result


def main():
    """Main function to interact with the calculator."""
    calculator = Calculator()

    print("Welcome to the Professional Python Calculator!")
    print(
        "Operations Available: + (add), - (subtract), * (multiply), / (divide), ^ (power), sqrt (square root), % (modulus), clear (reset), exit (quit)")

    while True:
        try:
            operation = input("\nEnter operation: ").strip().lower()

            if operation == "exit":
                print("Exiting the calculator. Goodbye!")
                break
            elif operation == "clear":
                calculator.clear()
                print("Result cleared.")
                continue

            if operation in ['+', '-', '*', '/', '^', '%']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == "+":
                    print(f"Result: {calculator.add(num1, num2)}")
                elif operation == "-":
                    print(f"Result: {calculator.subtract(num1, num2)}")
                elif operation == "*":
                    print(f"Result: {calculator.multiply(num1, num2)}")
                elif operation == "/":
                    print(f"Result: {calculator.divide(num1, num2)}")
                elif operation == "^":
                    print(f"Result: {calculator.power(num1, num2)}")
                elif operation == "%":
                    print(f"Result: {calculator.modulus(num1, num2)}")
            elif operation == "sqrt":
                num = float(input("Enter number: "))
                print(f"Result: {calculator.sqrt(num)}")
            else:
                print("Invalid operation. Please try again.")
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
