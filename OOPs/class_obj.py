
class Employee:
    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.sal = sal
    
    def print_fun(self):
        print(f"Employee name is {self.name}, Age is {self.age}yrs old, and Salary is around {self.sal}LPA")

p = Employee("sid", 20, 1000000000)
p.print_fun()
print(dir(p))