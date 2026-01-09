# Demonstration of Inheritance and Composition in Python
# Example of Inheritance and Composition
class Animal:
    def speak(self) -> str:
        return "Animal speaks"
    
class Dog(Animal):  # Dog is an Animal (Inheritance)
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):  # Cat is an Animal (Inheritance)
    def speak(self) -> str:
        return "Meow!"

class Person:
    def __init__(self, name):
        self.name = name
        self.pet = None  # Person has a pet (Composition)
    
    def set_pet(self, pet):
        self.pet = pet
    
    def introduce(self):
        if self.pet:
            return f"Hi, I'm {self.name} and my pet says: {self.pet.speak()}"
        else:
            return f"Hi, I'm {self.name} and I have no pet."

# Test the code
dog = Dog()
person = Person("Alice")
person.set_pet(dog)
print(person.introduce())

# Cat
cat = Cat()
person2 = Person("Alice")
person2.set_pet(cat)
print(person2.introduce())

# Person without pet
person3 = Person("Bob")
print(person3.introduce())