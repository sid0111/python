
class MathUtils:
    # even if decorator is not added it is static method beacuse it doesn't contain self or cls
    @staticmethod
    def sum(a,b): 
        return a+b

# print(MathUtils.sum(2,3))

c = MathUtils()
print(c.sum(4,3))