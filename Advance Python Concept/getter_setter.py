class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def first_name(self):
        l = self.name.split()
        return l[1];

    @first_name.setter
    def first_name(self, new_name):
        l = self.name.split();
        nname = f"{l[0]} {new_name}"
        self.name = nname
    
    @first_name.deleter
    def first_name(self):
        print("checkPoint")
        del self.name

e1 = Employee("naik sid", 20)
fname = e1.first_name
print(fname)
e1.first_name = "sam"
print(e1.name)
del e1.first_name
print(e1.name)