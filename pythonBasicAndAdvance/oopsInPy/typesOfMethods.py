# We have instance, class and static methods in python
class Example:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    # Instance method
    def instance_method(self):
        return f"Instance method called. Instance variable: {self.instance_variable}"

    # Class method
    @classmethod
    def class_method(cls):
        return f"Class method called. Class variable: {cls.class_variable}"

    # Static method
    @staticmethod
    def static_method():
        return "Static method called. No access to instance or class variables."

# Creating an object of Example class
example = Example("I am an instance variable")
print(example.instance_method())  # Calling instance method
print(Example.class_method())     # Calling class method    
print(Example.static_method())  

# Inheritance example to show method types in derived class
class Example2(Example):
    def __init__(self, instance_variable):
        super().__init__(instance_variable)
        example_var = Example("I am in Example2")
        print(example_var.instance_method())  # Accessing instance method from base class
    # Overriding instance method
    
    def instance_method(self):
        return f"Derived Instance method called. Instance variable: {self.instance_variable}"
    # calling example class methods
    print(Example.class_method())
    print(Example.static_method())

example2 = Example2("Derived instance variable")
examplemain = Example("Main instance variable")

print(example2.instance_method()) 

print(examplemain.instance_method())  # Calling overridden instance method