
class Animal:
    species = "Mammal"

    @classmethod
    def get_species(cls):
        return cls.species
    
    @classmethod 
    def set_species(cls, new_species):
        cls.species = new_species

# print(Animal.get_species())
# Animal.set_species("Reptiles")
# print(Animal.get_species())

#also can be acces using instance but preferablly class methods are access by class name
s = Animal()
print(s.get_species())
s.set_species("Reptiles")
print(s.get_species())

n = Animal()
print(n.get_species())