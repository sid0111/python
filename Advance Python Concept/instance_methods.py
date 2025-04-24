
class Employee:
    def __init__(self, name):
        self.n = name

    def emp_info(self):
        return f"The age of {self.n} is 20"

e = Employee("sid")
print(e.emp_info())