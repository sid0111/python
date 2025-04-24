
class Animal:
    def __init__(self,type):
        self.type = type
        print("hello sid!")
    
    def speak(self):
        print("Animal sounds")
    
class Dog(Animal):
    
    def speak(self):
        super().speak()
        print("Wofff!")

d = Dog("Dog")
d.speak()