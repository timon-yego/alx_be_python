#Simple Calculator with Match Case
#prompt user to enter two numbers
num1 = float(input(Enter first number:))
num2 = float(input(Enter second number:))

#ask for type of opereation
operation = input(Choose the operation (+, -, *, /):)

#perform calculations
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Error: Invalid operation selected.")

