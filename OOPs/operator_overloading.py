
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sum(self,p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        return f"X value is {self.x} and Y value is {self.y}"
    
    def __add__(self,p):
        return Point((self.x + p.x), (self.y + p.y))
    
p1 = Point(3,2)
p2 = Point(9,8)

# p = p1.sum(p2)
# print(p.print_point())
# p.print_point()

#operator overloading
p = p1 + p2
print(p.print_point())