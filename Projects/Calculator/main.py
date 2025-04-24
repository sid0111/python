
try:
    a = int(input("Enter a First number : "))
    b = int(input("Enter a Second number : "))

    print("Enter your choice \nSelect + for addition. \nSelect - for subtraction. \n Select * for multiplication. \n Select / for division.")

    choice = input("Enter your choice : ")

    match choice:
        case "+":
            print(f"Addition of {a} and {b} is : {a + b}")
        case "-":
            print(f"Subtraction of {a} and {b} is : {a - b}")
        case "*":
            print(f"Multiplication of {a} and {b} is : {a * b}")
        case "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            print(f"Division of {a} and {b} is : {a / b}")
        case _:
            print("Invalid choice. Please select a valid operation.")        
except Exception as e:
    print("Unknown Error Occured : ", e)
