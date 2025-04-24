
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self): #this method are suppose to return string instead print it
        return f"Name is {self.name}"

    def __repr__(self):
        return f"Name : {self.name}"

    def __len__(self):
        return len(self.name)


p = Person("sid",20)
print(str(p))
print(repr(p))
print(len(p))