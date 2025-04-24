
# def marks(**kwargs):
#     for item in kwargs.keys():
#         print(f"{item} marks is {kwargs[item]}")

# marks(sid=99, sam=100, san=100, suh=101)

def data(*args, **kwargs):
    print(args)
    print(kwargs)

data(1, 2, 3, 4, sid=10, sam=100)