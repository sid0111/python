a = int(input("Enter any number to win a lottery : "))

match a:
    # case 1:
    #     print("Better luck next time!")
    
    case 2: 
        print("you won a camera")
    
    case 1:
        b = int(input("Enter a number again : "))
        if(b == 1):
            print("You are unlucky!")
        else:
            print("You won $1000")
    
    case 3 if(a ==3):
        print("You won a IPhone6")
    
    case _:
        print("Try Again!")