def repeat(n):
    def Decorator(fun):
        def wrapper(a):
            for _ in range(n):
                fun(a)
        return wrapper
    return Decorator

@repeat(100000)
def hello(name):
    print(f"Hello {name}")

hello("sid")