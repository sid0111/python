
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if b == 0:
    raise ZeroDivisionError("Can't divide by zero")

print(f"The division is {a/b}")