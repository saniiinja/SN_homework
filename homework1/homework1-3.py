
number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))

operation = input("Choose an arithmetic operation: +, -, *, /: ")

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("Invalid operation.")
