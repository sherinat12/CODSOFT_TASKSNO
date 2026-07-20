def calculator():
    print("Simple Calculator")
    print("Operations: + - * /")

    try:
        num1 = float(input("Enter first number: "))
        operation = input("Choose operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Error: Invalid operation. Choose from +, -, *, /")
        return

    print(f"Result: {num1} {operation} {num2} = {result}")


if __name__ == "__main__":
    calculator()
