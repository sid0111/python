
while True:
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        
        print(f"The division is {a/b}")
    
    except ValueError:
        print("Please enter numeric typevalue")

    except ZeroDivisionError:
        print("Please enter valid number")

    except Exception as e:
        print("Unknown Exception : ",e)

    finally:
        print("EOP")