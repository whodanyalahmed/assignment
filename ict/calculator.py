op = input("Enter an operator + - * /: ")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num1 = int(num1)
num2 = int(num2)

if (op == "+" ):
    result = num1 + num2
    print(result)
elif(op == "-"):
    result = num1 - num2
    print(result)
elif (op == "*"):
    result = num1 * num2
    print(result)
elif (op == "/"):
    result = num1 / num2
    print(result)
elif (op == "%"):
    result = num1 % num2
    print(result)
else:
    print("You entered an invalid operator")
