
def Decorator(fun):
    def wrapper():
        print("Before Execution!")
        fun()
        print("After Execution!")

    return wrapper

@Decorator
def hello():
    print("hello sid!")

hello()