# In java we use private access specifier to achieve encapsulation
# In python we use name mangling to achieve encapsulation
# We need encapsulation to hide secure data and to limit its access from outside the class
# Levels of encapsulation in python: public, protected and private (name-mangled harder to access)

class person:

    def __init__(self):
        self.name = "shamanth"
        self._age = 30          # protected variable
        self.__ssn = "123-45-6789"  # private variable

p = person()
print(p.name)        # accessible
print(p._age)        # accessible but should not be accessed directly
# print(p.__ssn)      # will raise attribute error

# Accessing private variable using setters and getters

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
emp = Employee("John", 50000)
print(emp.salary)  # Accessing salary using getter
emp.salary = 60000  # Modifying salary using setter
print(emp.salary)

# We can have some restrictions in setter method
class Employeee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
emp = Employeee("John", 50000)
print(emp.salary)  # Accessing salary using getter
emp.salary = 1  # Modifying salary using setter

# if someone tries to delete handler we can have a @x.deleter method to handle this

# Example for deleter : clear cache 

class APIclinet:
    def __init__(self):
        self.__token = "abcd123"
    @property
    def setToken(self):
        return self.__token
    
    @setToken.deleter
    def setToken(self):
        print("Deleting token ..")
        self.__token = None

api = APIclinet()
del api.setToken
print(api.setToken)