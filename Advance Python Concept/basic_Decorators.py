def Decorator(fun):

    def wrapper():
        print("Before Execution!")
        fun()
        print("After Execution!")
    
    return wrapper

def hello():
    print("Hello sid!")

p = Decorator(hello)
p()