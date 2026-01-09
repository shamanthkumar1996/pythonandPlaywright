# Example 1: Object as a class attribute
class Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # default_person = Name("Default", 0)  # Class attribute

# Example 2: Object created in __init__ as instance attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friend = Name("Friend", 25)
      # Creates another object

# Example 3: Standard instantiation (outside class)
obj1 = Name("Shamanth", 30)
print("Name:", obj1.name)

# In python we cannt have multiple constructors like Java or C++
# But we can use default arguments to achieve similar functionality
class Animal:
    def __init__(self, species="Dog", age=1):
        self.species = species
        self.age = age
# Creating objects with different parameters
animal1 = Animal()
animal2 = Animal("Cat", 3)
animal3 = Animal(age=3)
print("Animal1:", animal1.species, animal1.age)
print("Animal2:", animal2.species, animal2.age)
print("Animal3:", animal3.species, animal3.age)