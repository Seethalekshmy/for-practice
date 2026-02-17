#calculator using match case
a = input("enter first number:")
b = input("enter second number:")
a =int(a)
b =int(b)
operation = input("enter the operation:")
match operation:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)