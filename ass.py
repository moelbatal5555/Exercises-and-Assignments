def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
def main():
    while True:
        command = input("Enter command (add, sub, mult, div) or 'stop' to exit: ").strip().lower()
        if command == "stop":
            print("Exiting the calculator. Goodbye!")
            break
        if command not in ["add", "sub", "mult", "div"]:
            print("Invalid command. Please try again.")
            continue
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        if command == "add":
            result = add(num1, num2)
        elif command == "sub":
            result = sub(num1, num2)
        elif command == "mult":
            result = mult(num1, num2)
        elif command == "div":
            result = div(num1, num2)
        print(f"The result is: {result}")
if __name__ == "__main__":
    main()
