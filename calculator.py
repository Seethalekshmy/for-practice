#calculator using functions
def addition(a,b):
    c = a + b
    return c
def subtraction(a,b):
    c = a - b
    return c
def multiplication(a,b):
    c = a * b
    return c
def division(a,b):
    c = a / b
    return c
a = input("enter first number:")
b = input("enter second number:")
a = int(a)
b = int(b)
operation = input("enter the operation :")
if operation == "+":
    print(addition(a,b))
elif operation == "-":
    print(subtraction(a,b))
elif operation == "*":
    print(multiplication(a,b))
elif operation == "/":
    print(division(a,b))