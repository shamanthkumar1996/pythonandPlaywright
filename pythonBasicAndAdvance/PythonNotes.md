# Python Interview Preparation Notes
## Complete Guide: Basic to Advanced

---

## Table of Contents
1. [Python Overview & Compilation](#python-overview--compilation)
2. [Python Advantages & Disadvantages](#python-advantages--disadvantages)
3. [Basic Concepts](#basic-concepts)
4. [Data Types & Structures](#data-types--structures)
5. [Control Flow](#control-flow)
6. [Functions](#functions)
7. [Object-Oriented Programming](#object-oriented-programming)
8. [Exception Handling](#exception-handling)
9. [File Handling](#file-handling)
10. [Modules & Packages](#modules--packages)
11. [Iterators & Generators](#iterators--generators)
12. [Decorators](#decorators)
13. [Context Managers](#context-managers)
14. [Comprehensions](#comprehensions)
15. [Lambda Functions](#lambda-functions)
16. [Memory Management](#memory-management)
17. [Multithreading & Multiprocessing](#multithreading--multiprocessing)
18. [Advanced Topics](#advanced-topics)
19. [Common Interview Questions](#common-interview-questions)
20. [🎭 PLAYWRIGHT - Browser Automation](#-playwright---browser-automation--testing)
21. [🚀 ADVANCED PYTHON TOPICS FOR EXPERTISE](#-advanced-python-topics-for-expertise)
    - [Collections Module](#1-collections-module)
    - [Itertools Module](#2-itertools-module)
    - [Functools Module](#3-functools-module)
    - [Deep vs Shallow Copy](#4-deep-vs-shallow-copy)
    - [Performance Optimization & Profiling](#5-performance-optimization--profiling)
    - [Abstract Base Classes](#6-abstract-base-classes-abc)
    - [Dataclasses](#7-dataclasses-modern-alternative-to-namedtuple)
    - [Slots - Memory Optimization](#8-slots---memory-optimization)
    - [Enum](#9-enum---defined-set-of-values)
    - [Advanced Pytest](#10-advanced-testing-with-pytest)
    - [Debugging Techniques](#11-debugging-techniques)
    - [Virtual Environments & Packaging](#12-virtual-environments--packaging)
    - [Code Quality Tools](#13-code-quality-tools)
    - [Configuration Management](#14-configuration-management)
    - [Advanced Async/Await](#15-advanced-asyncawait)
    - [Pathlib](#16-pathlib---modern-file-handling)

---

## 💡 Quick Learning Tips

**Before diving in, remember these essential points:**

1. **Code as you read** - Passive reading won't stick. Type every example and run it.
2. **Read error messages** - They're not scary, they're helpful! Read them completely.
3. **Test your assumptions** - Don't just believe what you read, test it in REPL.
4. **Focus on "WHY" not "WHAT"** - Understand why concepts work, not just memorize syntax.
5. **Build something** - After each section, build something using those concepts.
6. **Make mistakes on purpose** - Break code to understand what breaks and why.
7. **Read other people's code** - Study good code on GitHub to learn idioms and patterns.

---

## Python Overview & Compilation

### What is Python?
- **High-level, interpreted, general-purpose programming language**
- Created by Guido van Rossum in 1991
- Emphasizes code readability with significant use of whitespace
- Supports multiple programming paradigms: procedural, object-oriented, functional

### How Python Code Executes

#### 1. Source Code (.py file)
```python
# example.py
print("Hello World")
```

#### 2. Compilation to Bytecode
- Python first compiles source code to **bytecode**
- Bytecode is platform-independent intermediate representation
- Stored in `.pyc` files in `__pycache__` directory
- Not machine code - it's instructions for Python Virtual Machine (PVM)

#### 3. Python Virtual Machine (PVM)
- Interprets and executes bytecode
- Final step in Python execution
- Platform-specific but handles platform-independent bytecode

**Complete Flow:**
```
Source Code (.py) → Compiler → Bytecode (.pyc) → PVM → Execution
```

### Is Python Compiled or Interpreted?
**Both!** Python is:
- **Compiled** to bytecode (compilation phase)
- **Interpreted** by PVM (execution phase)
- Often called an "interpreted language" because compilation is automatic and hidden

### CPython vs Other Implementations
- **CPython**: Standard implementation (written in C)
- **Jython**: Python on JVM (compiles to Java bytecode)
- **IronPython**: Python for .NET framework
- **PyPy**: Python with JIT compiler (faster execution)

---

## Python Advantages & Disadvantages

### Advantages

#### 1. **Easy to Learn and Read**
- Simple, clean syntax
- Resembles pseudo-code
- Extensive documentation

#### 2. **Extensive Libraries**
- NumPy, Pandas (Data Science)
- Django, Flask (Web Development)
- TensorFlow, PyTorch (Machine Learning)
- Requests, BeautifulSoup (Web Scraping)

#### 3. **Cross-Platform**
- Runs on Windows, Mac, Linux, Unix
- Write once, run anywhere

#### 4. **Versatile**
- Web development
- Data analysis & visualization
- Machine learning & AI
- Automation & scripting
- Game development
- Desktop applications

#### 5. **Large Community**
- Active community support
- Abundant resources and tutorials
- Quick problem resolution

#### 6. **Dynamically Typed**
- No need to declare variable types
- Faster development

#### 7. **Integration**
- Easy integration with C, C++, Java
- Can call C/C++ libraries for performance

#### 8. **Free and Open Source**
- No licensing costs
- Community-driven development

### Disadvantages

#### 1. **Slower Execution Speed**
- Interpreted nature makes it slower than compiled languages (C, C++, Java)
- Not ideal for performance-critical applications

#### 2. **High Memory Consumption**
- Dynamic typing requires more memory
- Not suitable for memory-intensive tasks

#### 3. **Mobile Development**
- Not popular for mobile app development
- Limited mobile frameworks compared to Java/Kotlin (Android) or Swift (iOS)

#### 4. **Runtime Errors**
- Dynamic typing can lead to runtime errors
- Type errors only caught during execution

#### 5. **GIL (Global Interpreter Lock)**
- Prevents true multi-threading in CPython
- Only one thread executes Python bytecode at a time
- Limits parallel processing capabilities

#### 6. **Database Access**
- Database access layers less mature than JDBC or ODBC
- Not the first choice for database-heavy applications

---

## Basic Concepts

### Variables and Data Types

**What are Variables?**
Variables are containers for storing data values. Unlike languages like Java or C++, Python doesn't require you to declare the variable type beforehand. Python automatically determines the type based on the value you assign. This is called **dynamic typing** and makes Python flexible and beginner-friendly.

**Key Points about Python Variables:**
- No type declaration needed
- Type can change (though not recommended for clean code)
- Variable names are case-sensitive (`name` ≠ `Name`)
- Cannot start with a number
- Can contain letters, numbers, and underscores

**Example:**
```python
# Variable Assignment (no declaration needed)
name = "John"           # str (text)
age = 25               # int (integer number)
height = 5.9           # float (decimal number)
is_student = True      # bool (True/False)

# Python figures out the type automatically!
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

# Multiple Assignment (Tuple Unpacking)
x, y, z = 1, 2, 3  # Assign multiple values at once
a = b = c = 10      # Assign same value to multiple variables

print(x, y, z)      # 1 2 3
print(a, b, c)      # 10 10 10

# Type Conversion (Casting)
# Converting one type to another
num_str = "123"      # This is text, not a number
num_int = int(num_str)  # Convert string to integer
print(num_int + 77)     # Now we can do math: 200

# Other conversions
num_float = float("3.14")  # "3.14" → 3.14
num_str = str(123)         # 123 → "123"
bool_val = bool(1)         # 1 → True (0 is False, everything else is True)
```

### Naming Conventions (PEP 8 Style)
These conventions help make code readable and professional:
- **Variables/Functions**: lowercase_with_underscores (snake_case)
  - Example: `user_name`, `calculate_total`, `process_data`
- **Classes**: CapitalizedWords (PascalCase)
  - Example: `UserProfile`, `BankAccount`, `DataProcessor`
- **Constants**: UPPER_CASE_WITH_UNDERSCORES
  - Example: `MAX_SIZE`, `PI_VALUE`, `DEFAULT_TIMEOUT`
- **Private/Internal**: _leading_underscore
  - Example: `_internal_method`, `_cache`
  - Signals: "Use with caution, this is for internal use"
- **Name Mangling**: __double_leading_underscore (rare)
  - Example: `__private_var`
  - Creates: `_ClassName__private_var` (strongly discourages external access)

**Why conventions matter:**
- Code readability for you and others
- Makes intent clear (is this a class or function?)
- Helps avoid naming conflicts
- Professional coding practice

### Comments
Comments are notes in your code that Python ignores. Use them to explain "why" you did something, not "what" (code is self-explanatory).

```python
# Single line comment - use # for one line
# Good comments explain the reasoning, not just what the code does

# BAD: increments i by 1
i = i + 1

# GOOD: move to next iteration
i = i + 1

# Multi-line comments for detailed explanations
"""
This is a docstring (documentation string).
Used to document: functions, classes, and modules.
Will be shown when someone uses help() or?
"""

# Alternative multi-line style (less common, but works)
'''
Another way for multi-line,
but docstrings with """ are preferred.
'''
```

**When to comment:**
- Explain complex logic
- Explain why you made a decision
- Highlight potential issues
- Document functions and classes (use docstrings)

**When NOT to comment:**
- Don't repeat what code obviously does
- Don't comment every line (code should be self-explanatory)
- When variable/function names are clear

### Indentation - Critical in Python!
Unlike other languages that use `{` `}`, Python uses indentation (spaces) to define code blocks. This is unique and important.

**Why indentation matters:**
- Defines which lines belong together
- Makes code structure visual and clear
- Forces consistent, readable code
- Syntax error if indentation is wrong

**Indentation Rules:**
- Use 4 spaces per indentation level (PEP 8 standard)
- Don't mix tabs and spaces (use spaces only)
- Each nested block gets 4 more spaces

```python
# Python uses indentation to define code blocks
if True:
    print("Indented")  # 4 spaces (required!)
    if True:
        print("Nested")  # 8 spaces (4 more)

# Indentation matters - this is a SYNTAX ERROR:
if True:
print("Error!")  # No indent - Python won't understand
```

**Real-world example:**
```python
user = {"age": 25}

if user["age"] >= 18:           # Start of if block
    print("Adult")              # Part of if block (4 spaces)
    if user["age"] >= 21:       # Nested if (still 4 from previous)
        print("Can drink")      # Part of nested if (8 spaces total)
print("Script continues")      # Back to 0 spaces - outside all blocks
```

---

## Data Types & Structures

### 1. Numbers

#### Integer
```python
x = 10
y = -5
z = 0
big_num = 123456789012345678901234567890  # No limit on integer size
```

#### Float
```python
pi = 3.14
e = 2.718
scientific = 1.5e2  # 150.0
```

#### Complex
```python
c = 3 + 4j
print(c.real)  # 3.0
print(c.imag)  # 4.0
```

### 2. Strings

```python
# Creation
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''multi
line
string'''

# String Operations
text = "Hello World"
print(text[0])        # 'H' (indexing)
print(text[-1])       # 'd' (negative indexing)
print(text[0:5])      # 'Hello' (slicing)
print(text[::-1])     # 'dlroW olleH' (reverse)

# String Methods
print(text.upper())           # 'HELLO WORLD'
print(text.lower())           # 'hello world'
print(text.replace("World", "Python"))  # 'Hello Python'
print(text.split())           # ['Hello', 'World']
print("  text  ".strip())     # 'text'
print("Hello".startswith("He"))  # True
print("World".endswith("ld"))    # True

# String Formatting
name = "Alice"
age = 30

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# format() method
print("Name: {}, Age: {}".format(name, age))

# % operator (old style)
print("Name: %s, Age: %d" % (name, age))

# String Immutability
s = "hello"
# s[0] = 'H'  # TypeError: strings are immutable
s = "H" + s[1:]  # Create new string
```

### 3. Lists

```python
# Creation
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
nested = [[1, 2], [3, 4]]

# List Operations
numbers.append(6)           # Add to end
numbers.insert(0, 0)        # Insert at index
numbers.extend([7, 8])      # Add multiple elements
numbers.remove(3)           # Remove first occurrence
popped = numbers.pop()      # Remove and return last element
numbers.pop(0)              # Remove at index

# List Methods
print(numbers.index(4))     # Find index of element
print(numbers.count(2))     # Count occurrences
numbers.sort()              # Sort in place
numbers.reverse()           # Reverse in place
new_list = sorted(numbers)  # Return sorted list
numbers.clear()             # Remove all elements

# List Comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Slicing
lst = [0, 1, 2, 3, 4, 5]
print(lst[1:4])    # [1, 2, 3]
print(lst[::2])    # [0, 2, 4] (step)
print(lst[::-1])   # [5, 4, 3, 2, 1, 0] (reverse)

# List are Mutable
lst[0] = 10  # Allowed
```

### 4. Tuples

```python
# Creation
t1 = (1, 2, 3)
t2 = 1, 2, 3          # Parentheses optional
single = (1,)          # Comma needed for single element
empty = ()

# Tuple Operations
print(t1[0])           # Access by index
print(t1.count(2))     # Count occurrences
print(t1.index(3))     # Find index

# Tuple Immutability
# t1[0] = 10  # TypeError: tuples are immutable

# Tuple Unpacking
x, y, z = t1
a, *rest, b = (1, 2, 3, 4, 5)  # a=1, rest=[2,3,4], b=5

# Use Cases
# - Immutable data
# - Dictionary keys
# - Return multiple values from functions
```

### 5. Sets

```python
# Creation
s1 = {1, 2, 3, 4, 5}
s2 = set([1, 2, 2, 3, 3])  # {1, 2, 3} - duplicates removed
empty_set = set()           # {} creates empty dict, not set

# Set Operations
s1.add(6)              # Add element
s1.remove(1)           # Remove (raises KeyError if not found)
s1.discard(1)          # Remove (no error if not found)
s1.clear()             # Remove all

# Set Mathematics
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)           # {1, 2, 3, 4, 5, 6} Union
print(a & b)           # {3, 4} Intersection
print(a - b)           # {1, 2} Difference
print(a ^ b)           # {1, 2, 5, 6} Symmetric difference

# Set Methods
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))

# Frozen Set (Immutable)
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError
```

### 6. Dictionaries

```python
# Creation
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Alternative creation
d = dict(name="Alice", age=25)
d = dict([("a", 1), ("b", 2)])

# Accessing
print(person["name"])          # 'John'
print(person.get("age"))       # 30
print(person.get("country", "USA"))  # Default value

# Modifying
person["age"] = 31             # Update
person["country"] = "USA"      # Add new key

# Dictionary Methods
print(person.keys())           # dict_keys(['name', 'age', 'city'])
print(person.values())         # dict_values(['John', 30, 'New York'])
print(person.items())          # dict_items([...])

person.update({"age": 32, "job": "Engineer"})
popped = person.pop("city")    # Remove and return value
person.popitem()               # Remove and return last item (3.7+)
person.setdefault("salary", 50000)  # Add if not exists

# Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Nested Dictionaries
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}

# Iteration
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```

### Type Comparison Table

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|---------|
| **Mutable** | ✓ Yes | ✗ No | ✓ Yes | ✓ Yes |
| **Ordered** | ✓ Yes | ✓ Yes | ~ No* | ✓ Yes (3.7+) |
| **Indexed** | ✓ Yes | ✓ Yes | ✗ No | By key |
| **Duplicates** | ✓ Allowed | ✓ Allowed | ✗ No | Keys: No, Values: Yes |
| **Syntax** | `[]` | `()` | `{}` | `{k:v}` |
| **Performance** | Medium | Fast | Very Fast | Very Fast |
| **Use Case** | Sequences | Immutable data, keys | Unique items | Key-value mapping |

*Sets are conceptually unordered but maintain insertion order in Python 3.7+

**When to use what:**
- **List**: Default choice for collections; use when order matters or you need to modify
- **Tuple**: When data should't change; as dictionary keys; returning multiple values
- **Set**: Removing duplicates; checking membership; set operations
- **Dictionary**: Storing related data with meaningful labels; configuration/settings

---

## Control Flow

Control flow determines which code executes based on conditions. It's the "logic" in your program.

### 1. if-elif-else

Decision making in code. Execute different code based on conditions.

```python
# Basic if - execute block only if condition is True
age = 18
if age >= 18:
    print("Adult")

# if-else - do one thing OR the other
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if-elif-else - multiple conditions
score = 85
if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good")
elif score >= 70:
    print("C - Satisfactory")
elif score >= 60:
    print("D - Passing")
else:
    print("F - Failing")

# Nested if - conditions within conditions
if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Adult but no license")
else:
    print("Too young to drive")

# Ternary Operator - one-line if-else
# Syntax: value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions: and, or, not
# and - ALL must be True
if age >= 18 and has_license:
    print("Can drive")

# or - ANY must be True
if is_weekend or is_holiday:
    print("No work!")

# not - negates condition
if not is_raining:
    print("Go outside!")

### 2. Loops

### 2. Loops

Loops repeat code: **for** loops repeat a set number of times, **while** loops repeat while a condition is true.

#### for Loop - Repeat for each item
```python
# Basic for loop with range
for i in range(5):
    print(i)        # 0, 1, 2, 3, 4

# range(start, stop, step)
for i in range(1, 10, 2):   # Start at 1, go to 9, step by 2
    print(i)        # 1, 3, 5, 7, 9

# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)    # Prints each fruit

# With index - enumerate gives position AND value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # 0: apple
    # 1: banana
    # 2: cherry

# Iterate over dictionary
person = {"name": "Alice", "age": 25, "city": "NYC"}
for key, value in person.items():
    print(f"{key}: {value}")

# String iteration
for char in "hello":
    print(char)     # h, e, l, l, o

# enumerate() - get index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterate over dictionary
person = {"name": "John", "age": 30}
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)

# zip() - iterate over multiple sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

#### while Loop - Repeat while condition is True
```python
# Basic while - keeps running until condition becomes False
count = 0
while count < 5:
    print(count)
    count += 1  # Must change condition, or infinite loop!

# Infinite loop with break - useful for repeating until user quits
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break      # Exit loop
    print(f"You entered: {user_input}")

# while with continue - skip current iteration
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue   # Skip even numbers, go to next iteration
    print(count)   # Prints: 1, 3, 5, 7, 9

# while-else - else executes if loop ends normally (not via break)
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed normally")  # Executes at end
```

### 3. break, continue, pass

**Three important loop control keywords:**
- **break**: Exit loop immediately
- **continue**: Skip to next iteration
- **pass**: Do nothing (placeholder)

```python
# break - exit loop when condition met
for i in range(10):
    if i == 5:
        break        # Exit entire loop
    print(i)         # Prints: 0, 1, 2, 3, 4

# continue - skip current iteration, go to next
for i in range(10):
    if i % 2 == 0:
        continue     # Skip even numbers
    print(i)         # Prints: 1, 3, 5, 7, 9

# pass - placeholder, do nothing yet
for i in range(5):
    if i == 3:
        pass         # TODO: Implement this logic later
    print(i)

# pass in functions/classes (common in development)
def future_function():
    pass             # Will implement later

class FutureClass:
    pass             # Will implement later

# Real example: pass during development
def process_order(order):
    if order["status"] == "pending":
        pass         # TODO: Send to warehouse
    elif order["status"] == "shipped":
        print(f"Order {order['id']} is on the way")
```

### 4. Match Statement (Python 3.10+)

```python
# Pattern matching
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # Default case
            return "Unknown"

# Pattern matching with conditions
def grade(score):
    match score:
        case s if s >= 90:
            return "A"
        case s if s >= 80:
            return "B"
        case s if s >= 70:
            return "C"
        case _:
            return "F"

# Structural pattern matching
def process_command(command):
    match command.split():
        case ["quit"]:
            return "Quitting"
        case ["load", filename]:
            return f"Loading {filename}"
        case ["save", filename]:
            return f"Saving {filename}"
        case _:
            return "Unknown command"
```

---

## Functions

### 1. Basic Functions

```python
# Simple function
def greet():
    print("Hello!")

greet()  # Call function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)  # 8

# Multiple return values
def get_stats():
    return 100, 50, 25

max_val, min_val, avg_val = get_stats()

# Return without value (returns None)
def do_something():
    print("Doing something")
    return  # Optional

result = do_something()  # None
```

### 2. Function Arguments

**Different ways to pass data to functions:**

```python
# Default arguments - use values if not provided
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest! (uses default)
greet("Alice")   # Hello, Alice! (uses provided value)

# Keyword arguments - specify which parameter is which
def person_info(name, age, city):
    print(f"{name} is {age} years old, lives in {city}")

# These all do the same thing:
person_info("Alice", 25, "NYC")              # Positional
person_info("Alice", age=25, city="NYC")     # Mixed
person_info(name="Alice", age=25, city="NYC") # All keyword
person_info(age=25, city="NYC", name="Alice") # Order doesn't matter!

# *args - Accept any number of positional arguments
# Returns them as a tuple
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))          # 15
print(sum_all(10, 20))                 # 30
print(sum_all(1, 2, 3, 4, 5, 6, 7))   # 28

# **kwargs - Accept any number of keyword arguments
# Returns them as a dictionary
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC

# Combining all types: Regular, *args, **kwargs
def complex_func(a, b, *args, default=10, **kwargs):
    print(f"Regular params: a={a}, b={b}")
    print(f"args (tuple): {args}")
    print(f"Keyword-only default: {default}")
    print(f"Extra keywords: {kwargs}")

complex_func(1, 2, 3, 4, 5, default=20, x=100, y=200)
# Output:
# Regular params: a=1, b=2
# args (tuple): (3, 4, 5)
# Keyword-only default: 20
# Extra keywords: {'x': 100, 'y': 200}

# Positional-only parameters (Python 3.8+)
def func(a, b, /, c, d):
    # / means a, b are positional-only (can't use keywords)
    # c, d can be positional or keyword
    pass

func(1, 2, 3, 4)        # OK
func(1, 2, c=3, d=4)    # OK
# func(a=1, b=2, c=3, d=4)  # Error - a and b must be positional

# Keyword-only parameters
def func(a, b, *, c, d):
    # * means c, d must be passed as keywords
    # a, b can be positional or keyword
    pass

func(1, 2, c=3, d=4)    # OK
# func(1, 2, 3, 4)      # Error - c and d must be keywords
func(a=1, b=2, c=3, d=4)  # OK
```

### 3. Lambda Functions

```python
# Anonymous function
square = lambda x: x ** 2
print(square(5))  # 25

add = lambda x, y: x + y
print(add(3, 5))  # 8

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# Lambda with sorted()
points = [(1, 2), (3, 1), (5, 4)]
sorted_points = sorted(points, key=lambda x: x[1])
# [(3, 1), (1, 2), (5, 4)]
```

### 4. Scope and Lifetime

```python
# Global scope
global_var = "I'm global"

def outer():
    # Enclosing scope
    outer_var = "I'm in outer"
    
    def inner():
        # Local scope
        inner_var = "I'm in inner"
        print(global_var)  # Can access
        print(outer_var)   # Can access
        print(inner_var)   # Can access
    
    inner()

# global keyword
count = 0

def increment():
    global count  # Modify global variable
    count += 1

increment()
print(count)  # 1

# nonlocal keyword
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Modify enclosing variable
        x += 1
        print(x)
    
    inner()  # 11
    print(x)  # 11

# LEGB Rule: Local → Enclosing → Global → Built-in
```

### 5. Higher-Order Functions

```python
# Functions as arguments
def apply_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

result = apply_operation(add, 5, 3)  # 8

# Returning functions
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times_two = multiplier(2)
times_three = multiplier(3)

print(times_two(5))    # 10
print(times_three(5))  # 15

# Closures
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

c1 = make_counter()
print(c1())  # 1
print(c1())  # 2
```

### 6. Docstrings

```python
def function_with_docstring(param1, param2):
    """
    This function does something.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: If param1 is negative
    """
    if param1 < 0:
        raise ValueError("param1 must be non-negative")
    return param1 + param2

# Access docstring
print(function_with_docstring.__doc__)
help(function_with_docstring)
```

---

## Object-Oriented Programming

OOP organizes code around **objects** that have data (attributes) and behavior (methods). Think of classes as blueprints and objects as actual instances of those blueprints.

### 1. Classes and Objects

```python
# Class definition - blueprint for objects
class Person:
    # Class variable - SHARED by all instances
    species = "Homo sapiens"
    
    # Constructor - runs when object is created
    def __init__(self, name, age):
        # Instance variables - unique to each object
        self.name = name
        self.age = age
    
    # Instance method - can access and modify instance data
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    # String representation - what print() shows
    def __str__(self):
        return f"Person({self.name}, {self.age})"
    
    # Detailed representation - what repr() shows
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Create objects (instances of the class)
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

# Access attributes
print(p1.name)              # 'Alice'
print(p1.age)               # 25

# Call methods
print(p1.introduce())       # Hi, I'm Alice and I'm 25 years old

# Access class variable
print(p1.species)           # Homo sapiens
print(p2.species)           # Homo sapiens (same for all instances)

# String representation
print(p1)                   # Person(Alice, 25)
print(repr(p2))             # Person(name='Bob', age=30)

### 2. Encapsulation

```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # Protected (convention)
        self.__account_number = "12345"  # Private (name mangling)
    
    # Getter
    def get_balance(self):
        return self._balance
    
    # Setter
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500

# Private attribute access (name mangling)
# account.__account_number  # AttributeError
print(account._BankAccount__account_number)  # 12345 (not recommended)
```

### 3. Properties

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter for radius"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        """Computed property"""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

c = Circle(5)
print(c.radius)        # 5
print(c.area)          # 78.53975
c.radius = 10          # Uses setter
print(c.area)          # 314.159
# c.radius = -5        # ValueError
```

### 4. Inheritance

```python
# Single inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # Abstract method

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
    
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!

# isinstance and issubclass
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True
```

### 5. Multiple Inheritance

```python
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())    # Flying
print(duck.swim())   # Swimming
print(duck.quack())  # Quack!

# Method Resolution Order (MRO)
print(Duck.__mro__)
# (<class '__main__.Duck'>, <class '__main__.Flyer'>, 
#  <class '__main__.Swimmer'>, <class 'object'>)
```

### 6. Polymorphism

```python
# Method overriding
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(5, 10), Circle(7), Rectangle(3, 4)]

for shape in shapes:
    print(f"Area: {shape.area()}")
```

### 7. Abstract Classes

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    def sleep(self):
        return "Sleeping..."  # Concrete method

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def move(self):
        return "Running"

# animal = Animal()  # TypeError: Can't instantiate abstract class
dog = Dog()
print(dog.speak())  # Woof!
print(dog.sleep())  # Sleeping...
```

### 8. Special Methods (Magic Methods)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Index out of range")
    
    def __call__(self):
        return f"Vector at ({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)   # Vector(6, 8)
print(v1 * 3)    # Vector(6, 9)
print(v1 == v2)  # False
print(len(v1))   # 3
print(v1[0])     # 2
print(v1())      # Vector at (2, 3)
```

### 9. Class Methods and Static Methods

```python
class MyClass:
    class_variable = 0
    
    def __init__(self, value):
        self.instance_variable = value
    
    # Instance method (has access to instance via self)
    def instance_method(self):
        return f"Instance: {self.instance_variable}"
    
    # Class method (has access to class via cls)
    @classmethod
    def class_method(cls):
        return f"Class: {cls.class_variable}"
    
    # Static method (no access to instance or class)
    @staticmethod
    def static_method(x, y):
        return x + y
    
    # Alternative constructor using class method
    @classmethod
    def from_string(cls, string):
        value = int(string)
        return cls(value)

obj = MyClass(10)
print(obj.instance_method())      # Instance: 10
print(MyClass.class_method())     # Class: 0
print(MyClass.static_method(5, 3)) # 8

# Alternative constructor
obj2 = MyClass.from_string("20")
print(obj2.instance_variable)     # 20
```

### 10. Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown"  # Default value
    hobbies: list = field(default_factory=list)  # Mutable default
    
    def __post_init__(self):
        # Called after __init__
        if self.age < 0:
            raise ValueError("Age cannot be negative")

p1 = Person("Alice", 25)
p2 = Person("Bob", 30, "bob@email.com", ["reading", "gaming"])

print(p1)  # Person(name='Alice', age=25, email='unknown', hobbies=[])
print(p2)  # Person(name='Bob', age=30, email='bob@email.com', hobbies=['reading', 'gaming'])

# Automatic __eq__, __repr__, etc.
print(p1 == p2)  # False
```

---

## Exception Handling

### 1. Try-Except

```python
# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    x = int("abc")
except ValueError:
    print("Invalid integer")
except TypeError:
    print("Type error")

# Catch multiple exceptions in one block
try:
    # some code
    pass
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Catch all exceptions (not recommended)
try:
    # some code
    pass
except Exception as e:
    print(f"Error occurred: {e}")
```

### 2. Try-Except-Else-Finally

```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
else:
    # Executed if no exception occurred
    print("File read successfully")
    print(data)
finally:
    # Always executed
    try:
        file.close()
    except:
        pass
    print("Cleanup done")
```

### 3. Raising Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# Re-raising exceptions
try:
    # some code
    raise ValueError("Something went wrong")
except ValueError:
    print("Handling error")
    raise  # Re-raise the same exception
```

### 4. Custom Exceptions

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds: balance={balance}, required={amount}"
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

try:
    account = BankAccount(100)
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e.message)
```

### 5. Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── AssertionError
    ├── AttributeError
    ├── EOFError
    ├── ImportError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── TimeoutError
    ├── RuntimeError
    ├── TypeError
    ├── ValueError
    └── ...
```

### 6. Context Managers with Exceptions

```python
# Using with statement
with open("file.txt", "w") as f:
    f.write("Hello")
# File automatically closed even if exception occurs

# Multiple context managers
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data)
```

---

## File Handling

### 1. Reading Files

```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines into list
with open("file.txt", "r") as f:
    lines = f.readlines()

# Read first N characters
with open("file.txt", "r") as f:
    chunk = f.read(100)
```

### 2. Writing Files

```python
# Write (overwrites existing content)
with open("file.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("New line")

# Append
with open("file.txt", "a") as f:
    f.write("\nAppended line")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("file.txt", "w") as f:
    f.writelines(lines)
```

### 3. File Modes

```python
# 'r'  - Read (default)
# 'w'  - Write (overwrites)
# 'a'  - Append
# 'x'  - Exclusive creation (fails if file exists)
# 'b'  - Binary mode
# 't'  - Text mode (default)
# '+'  - Read and write

# Binary file
with open("image.jpg", "rb") as f:
    binary_data = f.read()

with open("copy.jpg", "wb") as f:
    f.write(binary_data)

# Read and write
with open("file.txt", "r+") as f:
    content = f.read()
    f.write("\nNew content")
```

### 4. File Operations

```python
import os
import shutil

# Check if file exists
if os.path.exists("file.txt"):
    print("File exists")

# Get file size
size = os.path.getsize("file.txt")

# Rename file
os.rename("old.txt", "new.txt")

# Delete file
os.remove("file.txt")

# Copy file
shutil.copy("source.txt", "destination.txt")

# Move file
shutil.move("source.txt", "new_location/source.txt")

# Get file info
import os.path
print(os.path.getsize("file.txt"))      # Size in bytes
print(os.path.getctime("file.txt"))     # Creation time
print(os.path.getmtime("file.txt"))     # Modification time
print(os.path.isfile("file.txt"))       # Is it a file?
print(os.path.isdir("folder"))          # Is it a directory?
```

### 5. Working with Paths

```python
import os
from pathlib import Path

# os.path methods
path = os.path.join("folder", "subfolder", "file.txt")
dirname = os.path.dirname(path)
basename = os.path.basename(path)
abs_path = os.path.abspath("file.txt")

# pathlib (modern approach)
p = Path("folder") / "subfolder" / "file.txt"
print(p.exists())
print(p.is_file())
print(p.is_dir())
print(p.parent)
print(p.name)
print(p.suffix)  # File extension
print(p.stem)    # Filename without extension

# Read/write with pathlib
p = Path("file.txt")
content = p.read_text()
p.write_text("New content")
```

### 6. CSV Files

```python
import csv

# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"]
]

with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# DictReader and DictWriter
with open("data.csv", "w", newline='') as f:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Alice", "Age": 25, "City": "NYC"})

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```

### 7. JSON Files

```python
import json

# Writing JSON
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding"]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Reading JSON
with open("data.json", "r") as f:
    loaded_data = json.load(f)

# JSON strings
json_string = json.dumps(data, indent=4)
data_from_string = json.loads(json_string)
```

---

## Modules & Packages

### 1. Importing Modules

```python
# Import entire module
import math
print(math.pi)
print(math.sqrt(16))

# Import specific items
from math import pi, sqrt
print(pi)
print(sqrt(16))

# Import with alias
import numpy as np
import pandas as pd

# Import all (not recommended)
from math import *

# Import from package
from package.module import function
```

### 2. Creating Modules

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

# Using the module
# main.py
import mymodule

print(mymodule.greet("Alice"))
print(mymodule.PI)
calc = mymodule.Calculator()
print(calc.add(3, 5))
```

### 3. Creating Packages

```
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

```python
# __init__.py
from .module1 import function1
from .module2 import function2

# Usage
from mypackage import function1
# or
import mypackage.module1
```

### 4. The `__name__` Variable

```python
# module.py
def main():
    print("Running as main")

if __name__ == "__main__":
    # Only runs when script is executed directly
    # Not when imported as module
    main()
```

### 5. Standard Library Modules

```python
# os - Operating system interface
import os
print(os.getcwd())
os.mkdir("new_folder")

# sys - System-specific parameters
import sys
print(sys.version)
print(sys.argv)  # Command line arguments

# datetime - Date and time
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)

# random - Random number generation
import random
print(random.randint(1, 100))
print(random.choice([1, 2, 3, 4, 5]))

# re - Regular expressions
import re
pattern = r'\d+'
text = "I have 2 apples and 5 oranges"
numbers = re.findall(pattern, text)

# collections - Specialized container datatypes
from collections import Counter, defaultdict, OrderedDict
cnt = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})

# itertools - Iterator functions
from itertools import combinations, permutations, product
list(combinations([1, 2, 3], 2))  # [(1, 2), (1, 3), (2, 3)]

# functools - Higher-order functions
from functools import reduce, lru_cache
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 15
```

---

## Iterators & Generators

### 1. Iterators

```python
# Iterator protocol
my_list = [1, 2, 3]
my_iter = iter(my_list)

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
# print(next(my_iter))  # StopIteration

# Custom iterator
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for num in Counter(1, 6):
    print(num)  # 1, 2, 3, 4, 5
```

### 2. Generators

```python
# Generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5

# Generator expression
squares = (x**2 for x in range(10))
print(next(squares))  # 0
print(next(squares))  # 1

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))

# Generator with send()
def echo():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")
```

### 3. Generator Benefits

```python
# Memory efficient
# List comprehension - creates entire list in memory
squares_list = [x**2 for x in range(1000000)]

# Generator - creates values on demand
squares_gen = (x**2 for x in range(1000000))

# Pipeline processing
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

def filter_lines(lines):
    for line in lines:
        if "error" in line.lower():
            yield line

def process_lines(lines):
    for line in lines:
        yield line.upper()

# Chaining generators
lines = read_large_file("large.log")
filtered = filter_lines(lines)
processed = process_lines(filtered)

for line in processed:
    print(line)
```

---

## Decorators

### 1. Function Decorators

```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function
# Hello!
# After function

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### 2. Preserving Metadata

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def add(a, b):
    """Add two numbers"""
    return a + b

print(add.__name__)  # 'add' (without @wraps would be 'wrapper')
print(add.__doc__)   # 'Add two numbers'
```

### 3. Practical Decorators

```python
# Timing decorator
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Logging decorator
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Caching decorator
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Authentication decorator
def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not user_is_authenticated():
            raise PermissionError("User not authenticated")
        return func(*args, **kwargs)
    return wrapper
```

### 4. Class Decorators

```python
# Decorator as a class
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Call 1 of say_hello
say_hello()  # Call 2 of say_hello

# Class decorator (decorates a class)
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Creating database connection")

db1 = Database()  # Creating database connection
db2 = Database()  # No output (returns same instance)
print(db1 is db2)  # True
```

### 5. Method Decorators

```python
# @property
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

# @staticmethod and @classmethod
class MyClass:
    class_var = 10
    
    @staticmethod
    def static_method(x):
        return x * 2
    
    @classmethod
    def class_method(cls):
        return cls.class_var
```

---

## Context Managers

### 1. Using Context Managers

```python
# with statement
with open("file.txt", "r") as f:
    content = f.read()
# File automatically closed

# Multiple context managers
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    outfile.write(infile.read())
```

### 2. Creating Context Managers

#### Class-based
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to suppress exceptions
        return False

with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
```

#### Function-based with contextlib
```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

with file_manager("test.txt", "w") as f:
    f.write("Hello, World!")

# Timer context manager
@contextmanager
def timer(name):
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"{name} took {end - start:.4f} seconds")

with timer("My operation"):
    time.sleep(1)
    # some operations

# Database transaction
@contextmanager
def transaction(db):
    db.begin()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
```

### 3. Practical Examples

```python
# Change directory temporarily
@contextmanager
def change_dir(path):
    import os
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)

with change_dir("/tmp"):
    # work in /tmp
    pass
# back to original directory

# Suppress exceptions
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("non_existent_file.txt")
# No error raised

# Redirect stdout
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    print("This goes to StringIO")
output = f.getvalue()
```

---

## Comprehensions

### 1. List Comprehension

```python
# Basic
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Matrix transpose
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]
```

### 2. Dictionary Comprehension

```python
# Basic
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# From two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = {k: v for k, v in zip(keys, values)}
# {'name': 'Alice', 'age': 25, 'city': 'NYC'}
```

### 3. Set Comprehension

```python
# Basic
squares = {x**2 for x in range(10)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# With condition
evens = {x for x in range(20) if x % 2 == 0}
# {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers}
# {1, 2, 3, 4}
```

### 4. Generator Expression

```python
# Similar to list comprehension but returns generator
squares = (x**2 for x in range(10))
print(next(squares))  # 0
print(next(squares))  # 1

# Memory efficient for large datasets
sum_of_squares = sum(x**2 for x in range(1000000))

# Can be passed directly to functions
max_value = max(x for x in range(100) if x % 7 == 0)
```

---

## Lambda Functions

### 1. Basic Lambda

```python
# Syntax: lambda arguments: expression
add = lambda x, y: x + y
print(add(3, 5))  # 8

square = lambda x: x ** 2
print(square(4))  # 16

# Multiple arguments
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24
```

### 2. Lambda with Built-in Functions

```python
# map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
# 120 (1*2*3*4*5)

# sorted()
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_points = sorted(points, key=lambda x: x[1])
# [(3, 1), (1, 2), (2, 3), (5, 4)]

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
# Bob, Alice, Charlie
```

### 3. Lambda Limitations

```python
# Cannot contain statements (only expressions)
# Cannot use: return, assert, pass, etc.
# Limited to single expression

# NOT allowed:
# bad_lambda = lambda x: if x > 0: return x else: return -x

# Use regular function instead:
def abs_value(x):
    if x > 0:
        return x
    else:
        return -x
```

---

## Memory Management

### 1. Reference Counting

```python
import sys

# Get reference count
a = [1, 2, 3]
print(sys.getrefcount(a))  # 2 (variable + getrefcount argument)

b = a  # Increase reference count
print(sys.getrefcount(a))  # 3

del b  # Decrease reference count
print(sys.getrefcount(a))  # 2
```

### 2. Garbage Collection

```python
import gc

# Manual garbage collection
gc.collect()

# Get garbage collection stats
print(gc.get_count())

# Disable/enable garbage collection
gc.disable()
gc.enable()

# Check if object is tracked by GC
obj = [1, 2, 3]
print(gc.is_tracked(obj))  # True
```

### 3. Memory Profiling

```python
import sys

# Get size of object
a = [1, 2, 3]
print(sys.getsizeof(a))  # Size in bytes

# Different data structures
print(sys.getsizeof([]))      # Empty list
print(sys.getsizeof(()))      # Empty tuple
print(sys.getsizeof({}))      # Empty dict
print(sys.getsizeof(set()))   # Empty set
```

### 4. Shallow vs Deep Copy

```python
import copy

# Shallow copy
original = [[1, 2], [3, 4]]
shallow = original.copy()  # or list(original) or original[:]

shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] - original affected!

# Deep copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99
print(original)  # [[1, 2], [3, 4]] - original unchanged
print(deep)      # [[99, 2], [3, 4]]
```

### 5. Interning

```python
# String interning (optimization for small strings)
a = "hello"
b = "hello"
print(a is b)  # True (same object)

# Integer interning (-5 to 256 are cached)
x = 256
y = 256
print(x is y)  # True

x = 257
y = 257
print(x is y)  # False (different objects)

# Force interning
import sys
a = sys.intern("hello world")
b = sys.intern("hello world")
print(a is b)  # True
```

### 6. Memory Leaks

```python
# Common causes:
# 1. Circular references
class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

a = Node(1)
b = Node(2)
a.ref = b
b.ref = a  # Circular reference

# 2. Global variables
global_list = []
def add_to_global():
    global_list.append([0] * 1000000)  # Memory leak

# 3. Unclosed files
# f = open("file.txt")  # Should use 'with' statement

# Use weakref to avoid circular references
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._ref = None
    
    @property
    def ref(self):
        return self._ref() if self._ref else None
    
    @ref.setter
    def ref(self, node):
        self._ref = weakref.ref(node) if node else None
```

---

## Multithreading & Multiprocessing

### 1. Threading

```python
import threading
import time

# Create thread
def worker(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finishing")

# Start threads
t1 = threading.Thread(target=worker, args=("A",))
t2 = threading.Thread(target=worker, args=("B",))

t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

print("All threads completed")
```

### 2. Thread Synchronization

```python
# Lock
lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(100000):
        with lock:  # or lock.acquire() ... lock.release()
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # 1000000

# RLock (Reentrant Lock)
rlock = threading.RLock()

def recursive_function(n):
    with rlock:
        if n > 0:
            recursive_function(n - 1)

# Semaphore
semaphore = threading.Semaphore(3)  # Allow max 3 threads

def worker():
    with semaphore:
        print(f"Thread {threading.current_thread().name} working")
        time.sleep(2)

# Event
event = threading.Event()

def waiter():
    print("Waiting for event")
    event.wait()
    print("Event received!")

def setter():
    time.sleep(2)
    event.set()

threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()
```

### 3. GIL (Global Interpreter Lock)

```python
# GIL prevents true parallelism in CPU-bound tasks
# Only one thread executes Python bytecode at a time

# CPU-bound task (GIL limits performance)
import threading
import time

def cpu_bound():
    count = 0
    for i in range(100000000):
        count += 1

start = time.time()
t1 = threading.Thread(target=cpu_bound)
t2 = threading.Thread(target=cpu_bound)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Threading: {time.time() - start:.2f}s")

# I/O-bound tasks benefit from threading
def io_bound():
    time.sleep(2)  # Simulating I/O

start = time.time()
t1 = threading.Thread(target=io_bound)
t2 = threading.Thread(target=io_bound)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Threading: {time.time() - start:.2f}s")  # ~2s (parallel)
```

### 4. Multiprocessing

```python
import multiprocessing
import time

# Create process
def worker(name):
    print(f"Process {name} starting")
    time.sleep(2)
    print(f"Process {name} finishing")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args=("A",))
    p2 = multiprocessing.Process(target=worker, args=("B",))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("All processes completed")
```

### 5. Process Pool

```python
from multiprocessing import Pool

def square(x):
    return x ** 2

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        # map
        result = pool.map(square, range(10))
        print(result)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        
        # apply_async
        result = pool.apply_async(square, (5,))
        print(result.get())  # 25
        
        # starmap (multiple arguments)
        def add(x, y):
            return x + y
        
        result = pool.starmap(add, [(1, 2), (3, 4), (5, 6)])
        print(result)  # [3, 7, 11]
```

### 6. Inter-Process Communication

```python
# Queue
from multiprocessing import Queue, Process

def producer(q):
    for i in range(5):
        q.put(i)
        print(f"Produced {i}")

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    
    p1.start()
    p2.start()
    
    p1.join()
    q.put(None)  # Signal consumer to stop
    p2.join()

# Pipe
from multiprocessing import Pipe

def sender(conn):
    conn.send("Hello from sender")
    conn.close()

def receiver(conn):
    msg = conn.recv()
    print(f"Received: {msg}")

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p1 = Process(target=sender, args=(child_conn,))
    p2 = Process(target=receiver, args=(parent_conn,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

# Shared memory
from multiprocessing import Value, Array

def increment(shared_value, shared_array):
    shared_value.value += 1
    for i in range(len(shared_array)):
        shared_array[i] += 1

if __name__ == "__main__":
    shared_val = Value('i', 0)  # 'i' for integer
    shared_arr = Array('i', [0, 0, 0])  # array of integers
    
    processes = [Process(target=increment, args=(shared_val, shared_arr)) 
                 for _ in range(10)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    print(shared_val.value)  # 10
    print(list(shared_arr))  # [10, 10, 10]
```

### 7. asyncio (Async/Await)

```python
import asyncio

# Basic async function
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Run async function
asyncio.run(say_hello())

# Multiple async tasks
async def task(name, delay):
    print(f"Task {name} starting")
    await asyncio.sleep(delay)
    print(f"Task {name} completed")
    return f"Result from {name}"

async def main():
    # Run concurrently
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )
    print(results)

asyncio.run(main())

# async with
async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.example.com/data') as response:
            return await response.json()
```

---

## Advanced Topics

### 1. Metaclasses

```python
# Type is the metaclass for all classes
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
print(type(int))      # <class 'type'>

# Custom metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Add a class variable
        dct['added_attribute'] = 100
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.added_attribute)  # 100

# Singleton using metaclass
class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    pass

db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

### 2. Descriptors

```python
class Descriptor:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)
    
    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]

class MyClass:
    value = Descriptor('value')
    
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(obj.value)  # 10
obj.value = 20    # OK
# obj.value = "string"  # TypeError
```

### 3. `*args` and `**kwargs` Unpacking

```python
# Function arguments
def func(a, b, c):
    print(a, b, c)

args = [1, 2, 3]
func(*args)  # Unpacking list: func(1, 2, 3)

kwargs = {"a": 1, "b": 2, "c": 3}
func(**kwargs)  # Unpacking dict: func(a=1, b=2, c=3)

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Merging lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [*list1, *list2]
# [1, 2, 3, 4, 5, 6]
```

### 4. Type Hints (Python 3.5+)

```python
from typing import List, Dict, Tuple, Optional, Union, Callable

# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Collection types
def process_items(items: List[int]) -> int:
    return sum(items)

def get_user(user_id: int) -> Dict[str, Union[str, int]]:
    return {"name": "Alice", "age": 25}

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    if user_id > 0:
        return "Alice"
    return None

# Union (multiple types)
def process(value: Union[int, str]) -> str:
    return str(value)

# Callable
def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

# Type aliases
Vector = List[float]
def scale(vector: Vector, scalar: float) -> Vector:
    return [x * scalar for x in vector]

# Generic types
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()

# Runtime type checking (requires external library)
# pip install typeguard
from typeguard import typechecked

@typechecked
def add(a: int, b: int) -> int:
    return a + b

# add(1, "2")  # TypeError
```

### 5. Coroutines and async/await

```python
import asyncio

# Coroutine
async def fetch_data(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)  # Simulate network delay
    return f"Data from {url}"

# Run coroutine
async def main():
    data = await fetch_data("https://api.example.com")
    print(data)

asyncio.run(main())

# Multiple concurrent tasks
async def main():
    tasks = [
        fetch_data("https://api1.com"),
        fetch_data("https://api2.com"),
        fetch_data("https://api3.com")
    ]
    results = await asyncio.gather(*tasks)
    print(results)

# Create task
async def main():
    task = asyncio.create_task(fetch_data("https://api.com"))
    # Do other work
    result = await task
```

### 6. Regular Expressions

```python
import re

# Match
pattern = r'\d+'
text = "I have 2 apples and 5 oranges"
match = re.search(pattern, text)
if match:
    print(match.group())  # '2'

# Find all
numbers = re.findall(pattern, text)
print(numbers)  # ['2', '5']

# Replace
new_text = re.sub(r'\d+', 'X', text)
print(new_text)  # 'I have X apples and X oranges'

# Split
text = "apple,banana,cherry"
fruits = re.split(r',', text)
print(fruits)  # ['apple', 'banana', 'cherry']

# Groups
pattern = r'(\w+)@(\w+)\.(\w+)'
email = "user@example.com"
match = re.search(pattern, email)
if match:
    print(match.group(0))  # 'user@example.com'
    print(match.group(1))  # 'user'
    print(match.group(2))  # 'example'
    print(match.group(3))  # 'com'

# Compile pattern for reuse
pattern = re.compile(r'\d+')
numbers = pattern.findall(text)

# Common patterns
# \d - digit
# \w - word character
# \s - whitespace
# . - any character
# * - 0 or more
# + - 1 or more
# ? - 0 or 1
# {n} - exactly n
# {n,} - n or more
# {n,m} - between n and m
# ^ - start of string
# $ - end of string
# [...] - character set
# [^...] - negated character set
```

### 7. Working with Dates and Times

```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
today = date.today()

print(now)    # 2025-02-13 10:30:45.123456
print(today)  # 2025-02-13

# Create specific datetime
dt = datetime(2025, 12, 25, 10, 30, 0)

# Format datetime
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # '2025-02-13 10:30:45'

# Parse string to datetime
dt = datetime.strptime("2025-02-13", "%Y-%m-%d")

# Timedelta (duration)
future = now + timedelta(days=7, hours=2)
past = now - timedelta(weeks=1)

# Difference between dates
diff = future - now
print(diff.days)        # Days
print(diff.seconds)     # Seconds
print(diff.total_seconds())  # Total seconds

# Common format codes
# %Y - Year (4 digits)
# %m - Month (01-12)
# %d - Day (01-31)
# %H - Hour (00-23)
# %M - Minute (00-59)
# %S - Second (00-59)
# %A - Weekday name
# %B - Month name
```

---

## Common Interview Questions

### 1. What is the difference between list and tuple?
- **List**: Mutable, uses [], slower, more memory
- **Tuple**: Immutable, uses (), faster, less memory, can be dictionary keys

### 2. What is `__init__` and `__new__`?
- `__new__`: Creates instance (constructor)
- `__init__`: Initializes instance (initializer)
- `__new__` is called before `__init__`

### 3. What is GIL?
Global Interpreter Lock prevents multiple threads from executing Python bytecode simultaneously. Only one thread can execute at a time. Limits CPU-bound multithreading but doesn't affect I/O-bound tasks.

### 4. What are decorators?
Functions that modify the behavior of other functions. Implemented using @ syntax.

### 5. Explain `*args` and `**kwargs`
- `*args`: Variable number of positional arguments (tuple)
- `**kwargs`: Variable number of keyword arguments (dict)

### 6. What is list comprehension?
Concise way to create lists: `[expression for item in iterable if condition]`

### 7. What is the difference between `==` and `is`?
- `==`: Checks value equality
- `is`: Checks identity (same object in memory)

### 8. What is monkey patching?
Dynamically modifying a class or module at runtime.

```python
class MyClass:
    def method(self):
        return "original"

# Monkey patching
MyClass.method = lambda self: "patched"

obj = MyClass()
print(obj.method())  # "patched"
```

### 9. What is the difference between shallow and deep copy?
- **Shallow copy**: Copies object but not nested objects
- **Deep copy**: Copies object and all nested objects

### 10. What is `self` in Python?
Reference to the instance of the class. First parameter in instance methods.

### 11. What are generators?
Functions that use `yield` to return values one at a time. Memory efficient for large datasets.

### 12. What is the difference between `append()` and `extend()`?
- `append()`: Adds single element
- `extend()`: Adds multiple elements from iterable

### 13. What is duck typing?
"If it walks like a duck and quacks like a duck, it's a duck." Type checking based on behavior rather than inheritance.

### 14. What is MRO (Method Resolution Order)?
Order in which Python looks for methods in inheritance hierarchy. Determined by C3 linearization algorithm.

### 15. What are Python's built-in data types?
- Numeric: int, float, complex
- Sequence: list, tuple, range
- Text: str
- Mapping: dict
- Set: set, frozenset
- Boolean: bool
- Binary: bytes, bytearray

### 16. Explain pass, break, and continue
- `pass`: Do nothing (placeholder)
- `break`: Exit loop
- `continue`: Skip to next iteration

### 17. What is lambda function?
Anonymous function defined with `lambda` keyword. Limited to single expression.

### 18. What is `__name__ == '__main__'`?
Checks if script is run directly (not imported). Used to write code that runs only when script is executed.

### 19. What is the difference between remove(), del, and pop()?
- `remove()`: Removes first occurrence of value
- `del`: Removes element by index
- `pop()`: Removes and returns element

### 20. What are Python packages?
Collections of modules organized in directories with `__init__.py` file.

---

## Best Practices

### 1. PEP 8 Style Guide
- Use 4 spaces for indentation
- Max line length: 79 characters
- Use snake_case for variables and functions
- Use PascalCase for classes
- Add blank lines to separate logical sections

### 2. Code Organization
```python
# Imports (standard library, third-party, local)
import os
import sys

import numpy as np
import pandas as pd

from mymodule import myfunction

# Constants
MAX_SIZE = 100

# Functions

# Classes

# Main code
if __name__ == '__main__':
    main()
```

### 3. Error Handling
- Use specific exceptions
- Don't catch all exceptions unless necessary
- Use finally for cleanup
- Create custom exceptions for domain-specific errors

### 4. Documentation
- Write docstrings for modules, classes, and functions
- Use meaningful variable names
- Comment complex logic
- Keep comments up-to-date

### 5. Testing
```python
import unittest

class TestMyFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_negative(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

---

---

## How to Use These Notes Effectively

### Learning Path (Recommended Order)
1. **Start Here:** Python Overview, Variables, Data Types, Control Flow
   - Master: What is Python, how code runs, basic data structs
   
2. **Then:** Functions, Loops, and Conditions
   - Master: How to write reusable code, control program flow
   
3. **Next:** Object-Oriented Programming, Classes
   - Master: How to structure complex projects
   
4. **Then:** Exception Handling, File I/O, Modules
   - Master: Real-world application skills
   
5. **Finally:** Advanced Topics (Decorators, Generators, etc.)
   - Master: Professional-level Python skills

### Pro Tips for Learning
- **Type all code examples** - Don't just read, actually write and run the code
- **Modify examples** - Change print statements, add features, break things on purpose
- **Use REPL** - Open Python REPL and test concepts interactively
- **Practice daily** - 30 minutes coding daily > 5 hours once a week
- **Build projects** - Theory + practice = mastery
- **Read error messages carefully** - Errors are helpful, not bad!
- **Use print() to debug** - Add strategic print statements to understand flow

---

## Summary

This comprehensive guide covers Python from basic to advanced concepts:

### Part 1: Fundamentals
- **Python Overview:** Compilation process, advantages, disadvantages
- **Variables & Data Types:** int, float, str, bool, list, tuple, set, dict
- **Control Flow:** if/elif/else, for loops, while loops
- **Functions:** Parameters, return values, scope, closures

### Part 2: Collections & Data Structures
- **Lists:** Ordered, mutable, indexing, slicing, comprehension
- **Tuples:** Immutable, unpacking, use as dict keys
- **Sets:** Unique elements, mathematical operations
- **Dictionaries:** Key-value pairs, nested structures, iterations

### Part 3: Object-Oriented Programming
- **Classes & Objects:** Constructors, methods, attributes
- **Encapsulation:** Public, protected, private members
- **Properties:** Decorators for controlled access
- **Inheritance:** Single, multiple, MRO
- **Polymorphism:** Method overriding, duck typing

### Part 4: Advanced Topics
- **Exception Handling:** try/except/finally, custom exceptions
- **Decorators:** Function/class modification, common patterns
- **Generators:** Memory-efficient iteration with yield
- **Context Managers:** with statement, resource cleanup
- **Comprehensions:** List, dict, set comprehensions, generator expressions
- **Type Hints:** Static typing information for IDE support
- **Regular Expressions:** Pattern matching and text manipulation
- **Async/Await:** Asynchronous programming for concurrent tasks

### Part 5: Professional Skills
- **File Handling:** Read, write, context managers
- **Modules & Packages:** Organizing code, imports
- **Memory Management:** Reference counting, garbage collection
- **Concurrency:** Threading, multiprocessing, async
- **Testing:** unittest, pytest basics
- **Best Practices:** PEP 8, documentation, error handling

---

## Essential Concepts to Master

### 1. **Mutable vs Immutable**
- **Mutable:** list, dict, set - can be changed after creation
- **Immutable:** int, float, str, tuple - cannot be changed
- **Implication:** Use immutable for dict keys and to prevent accidental changes

### 2. **References vs Values**
```python
a = [1, 2, 3]
b = a              # b references same list as a
b.append(4)
print(a)           # [1, 2, 3, 4] - a changed too!

c = a.copy()       # c is new list with same values
c.append(5)
print(a)           # [1, 2, 3, 4] - a unchanged
```

### 3. **When to Use Each Data Structure**
- **List:** "I have a sequence of items"
- **Tuple:** "I have immutable data or need hashable items"
- **Set:** "I need unique items or set operations"
- **Dict:** "I need to look up values by meaningful names"

### 4. **DRY Principle (Don't Repeat Yourself)**
- If copying code, consider making a function
- If copying functions, consider using loops or higher-order functions
- If finding yourself repeating logic, consider abstraction

### 5. **Scope is Your Friend**
- Use local variables by default
- Use global rarely (often indicates design issue)
- Understand LEGB rule for variable lookup
- Use encapsulation to control data access

---

## Common Mistakes to Avoid

1. **Mutable Default Arguments**
   ```python
   # WRONG
   def add_item(item, list=[]):  # [] created once!
       list.append(item)
       return list
   
   # RIGHT
   def add_item(item, list=None):
       if list is None:
           list = []
       list.append(item)
       return list
   ```

2. **Modifying List While Iterating**
   ```python
   # WRONG - unpredictable behavior
   for i in list:
       if condition:
           list.remove(i)
   
   # RIGHT
   list = [i for i in list if not condition]
   ```

3. **Confusing == and is**
   ```python
   a = [1, 2, 3]
   b = [1, 2, 3]
   a == b   # True - same contents
   a is b   # False - different objects
   ```

4. **Global Variables**
   - Avoid them when possible
   - If must use, document clearly
   - Use classes or functions instead

5. **Bare except**
   ```python
   # BAD - catches everything including KeyboardInterrupt
   except:
       pass
   
   # GOOD - catch specific exceptions
   except IndexError:
       pass
   ```

---

## Key Takeaways

1. **Python is Both Compiled and Interpreted**
   - Compilation to bytecode happens automatically
   - PVM interprets bytecode at runtime
   - This is why Python is flexible and cross-platform

2. **Everything is an Object**
   - Even functions and classes are objects
   - This enables powerful patterns like decorators

3. **GIL Limits CPU-Bound Multithreading**
   - Only one thread executes Python bytecode at a time
   - Doesn't affect I/O-bound tasks (network, file)
   - Use multiprocessing for CPU-intensive work

4. **Data Types Matter**
   - Choose right data structure for task
   - Mutable vs immutable has important implications
   - List comprehension is idiomatic and fast

5. **Readability Counts**
   - PEP 8 isn't just style guide, it's Python philosophy
   - Clean code > clever code
   - Comments explain WHY, not WHAT

6. **Functions and Classes Organize Code**
   - Small, focused functions easier to test
   - Classes group related data and behavior
   - Encapsulation prevents bugs

---

## Next Steps for Learning

### For Beginners
- [ ] Create 5 small programs using basic concepts
- [ ] Build a calculator application
- [ ] Make a to-do list CLI application
- [ ] Run existing Python code and understand it
- [ ] Solve coding challenges on HackerRank or LeetCode

### For Intermediate Learners
- [ ] Build a web app with Flask or Django
- [ ] Work with databases (SQL, ORM)
- [ ] Write tests for your code (unittest or pytest)
- [ ] Practice object-oriented design
- [ ] Contribute to open-source projects

### For Advanced Learners
- [ ] Study metaclasses and descriptors
- [ ] Explore async/await patterns
- [ ] Optimize performance bottlenecks
- [ ] Design large-scale applications
- [ ] Study Python internals

---

## Useful Resources

### Official Documentation
- Python Docs: https://docs.python.org/3/
- PEP 8 Style Guide: https://www.python.org/dev/peps/pep-0008/

### Interactive Learning
- Python REPL - learn hands-on
- Jupyter Notebooks - mix code and documentation
- Online judges - practice coding skills

### Practice Projects
- Build web scraper
- Create CLI tool
- Build API with Flask/Django
- Game development with Pygame
- Data analysis with Pandas

---

**Remember:** Mastering Python takes time and practice. Focus on understanding concepts deeply rather than memorizing syntax. The code examples here are starting points - modify them, break them, and learn from your mistakes!

**Your learning path:** Start with basics → Practice constantly → Build projects → Study advanced topics → Master the language

Good luck with your Python journey! 🐍

---

# 📚 COMPLETE LEARNING ROADMAP: Python + Playwright Mastery

## Phase 1: Python Fundamentals (Weeks 1-4)

### Week 1-2: Core Syntax
- ✅ Variables and data types (int, float, str, bool)
- ✅ String operations and formatting
- ✅ Basic input/output
- ✅ Comments and code style (PEP 8)
- ✅ Indentation and code blocks
- **Practice:** Write 5 small programs (calculator, temperature converter, etc.)

### Week 2-3: Collections & Control Flow
- ✅ Lists, tuples, sets, dictionaries
- ✅ Indexing and slicing
- ✅ if/elif/else statements
- ✅ for and while loops
- ✅ List comprehensions
- **Practice:** Build programs that manipulate data collections

### Week 3-4: Functions & Scope
- ✅ Function definition and calls
- ✅ Parameters (positional, keyword, default, *args, **kwargs)
- ✅ Return values
- ✅ Variable scope (Local, Enclosing, Global, Built-in)
- ✅ Lambda functions
- **Practice:** Refactor previous programs using functions

---

## Phase 2: Object-Oriented Programming (Weeks 5-7)

### Week 5: OOP Basics
- ✅ Classes and objects
- ✅ Constructor (__init__)
- ✅ Instance methods and variables
- ✅ Class variables
- **Practice:** Create Person, Animal, Car classes with methods

### Week 6: Advanced OOP
- ✅ Inheritance (single and multiple)
- ✅ Polymorphism and method overriding
- ✅ Encapsulation (public, protected, private)
- ✅ Properties and decorators
- **Practice:** Create inheritance hierarchies, use super()

### Week 7: OOP Best Practices
- ✅ Abstract Base Classes
- ✅ Composition vs Inheritance
- ✅ SOLID principles
- ✅ Design patterns
- **Practice:** Refactor all previous code using OOP

---

## Phase 3: Advanced Python (Weeks 8-10)

### Week 8: Functional Programming & Decorators
- ✅ Map, filter, reduce
- ✅ Decorator basics
- ✅ Decorator patterns
- ✅ Closures and nested functions
- **Practice:** Create custom decorators

### Week 9: Standard Library Deep Dive
- ✅ Collections (Counter, defaultdict, deque, namedtuple)
- ✅ Itertools (chain, combinations, permutations)
- ✅ Functools (wraps, lru_cache, partial)
- ✅ Pathlib for file operations
- **Practice:** Use each module in a project

### Week 10: Error Handling & File I/O
- ✅ try/except/finally/else
- ✅ Custom exceptions
- ✅ Context managers (with statement)
- ✅ File reading/writing
- ✅ JSON and CSV handling
- **Practice:** Robust error handling in all code

---

## Phase 4: Python Testing & Quality (Weeks 11-12)

### Week 11: Testing Frameworks
- ✅ Unittest basics
- ✅ Pytest fixtures and parametrization
- ✅ Mocking and patching
- ✅ Test organization
- **Practice:** Write tests for Phase 1-2 code

### Week 12: Code Quality
- ✅ Type hints and mypy
- ✅ Code style (flake8, black, pylint)
- ✅ Profiling and optimization
- ✅ Debugging with pdb
- **Practice:** Apply quality tools to all your code

---

## Phase 5: Async, Performance & Advanced Topics (Weeks 13-15)

### Week 13: Asynchronous Programming
- ✅ Async/await basics
- ✅ Coroutines and tasks
- ✅ Aiohttp for async HTTP
- ✅ Threading and multiprocessing
- **Practice:** Build concurrent applications

### Week 14: Performance & Internals
- ✅ Profiling with cProfile
- ✅ Slots, __new__, __del__
- ✅ Descriptors and properties
- ✅ Memory management and GIL
- **Practice:** Optimize a slow program

### Week 15: Capstone Python Project
- ✅ Build a medium-sized application
- ✅ Use everything learned (OOP, testing, async, standard library)
- **Project ideas:** CLI tool, data processor, web scraper

---

## Phase 6: Web Automation with Playwright (Weeks 16-18)

### Week 16: Playwright Basics
- ✅ Installation and browser launching
- ✅ Page navigation and interactions
- ✅ Locators and selectors
- ✅ Screenshots and basic assertions
- **Practice:** Automate simple web tasks

### Week 17: Playwright Testing
- ✅ Pytest integration
- ✅ Page Objects pattern
- ✅ Fixtures and parametrization
- ✅ Assertions and waiting
- **Practice:** Write tests for 5 websites

### Week 18: Advanced Playwright
- ✅ Request/response interception
- ✅ Mobile emulation and geolocation
- ✅ Authentication and cookies
- ✅ Debugging and tracing
- **Practice:** Complex test scenarios

---

## Phase 7: Integration & Real-World Projects (Weeks 19-20)

### Week 19: Playwright + Pytest Advanced
- ✅ Fixtures with database
- ✅ Parallel test execution
- ✅ CI/CD integration
- ✅ Test reporting and analytics
- **Practice:** Setup complete test framework

### Week 20: Capstone Playwright Project
- ✅ Build comprehensive test suite for real website
- ✅ Use Page Objects
- ✅ Parallel execution
- ✅ Generate reports
- **Goals:** 50+ tests, multiple browsers, CI/CD ready

---

## Phase 8: Specialization & Expertise (Weeks 21-24)

### Choose Your Path:

#### Path A: Web Testing Expert
- Advanced Playwright scenarios
- Cross-browser testing strategies
- API testing integration
- Performance testing with Playwright

#### Path B: Python Backend Expert
- REST API development (Flask/Django)
- Database integration (SQLAlchemy)
- Microservices architecture
- System design and scalability

#### Path C: Full-Stack Test Automation Expert
- API testing with Pytest
- UI testing with Playwright
- Performance testing
- Test infrastructure and CI/CD

---

## Daily Practice Schedule

### Beginner (Weeks 1-8)
**Daily:** 60-90 minutes
- 30 min: Read and understand concepts
- 30 min: Write code from memory (no copy-paste)
- 30 min: Challenge problems or mini-projects

### Intermediate (Weeks 9-16)
**Daily:** 90-120 minutes
- 30 min: Study advanced concepts
- 60 min: Build features or solve problems
- 30 min: Code review and refactoring

### Advanced (Weeks 17-24)
**Daily:** 120-150 minutes
- 30 min: Read documentation/blogs
- 90 min: Contribute to projects
- 30 min: Optimization and profiling

---

## Recommended Project Progression

### Beginner Projects
1. **Calculator:** Basic Python
2. **To-Do List:** Collections and persistence
3. **Student Grade System:** OOP basics
4. **Weather App:** API calling and data parsing

### Intermediate Projects
1. **E-commerce Scraper:** Web scraping with error handling
2. **Task Manager API:** Flask/Django REST API
3. **Data Analyzer:** Collections, pandas, visualization
4. **Automated Report Generator:** File I/O, templating

### Advanced Projects
1. **Web Testing Suite:** 100+ tests with Playwright
2. **Microservices System:** Multiple services, async communication
3. **Real-time Analytics:** Async/await, database, UI
4. **CI/CD Pipeline:** Testing, deployment automation

### Capstone Project Ideas
- **Comprehensive Test Automation Framework**
  - Page objects, fixtures, utilities
  - Multiple browsers, multiple environments
  - CI/CD integration, reporting
  - 100+ tests, parallel execution

- **Full-Stack Monitoring System**
  - Python backend (API)
  - Playwright integration tests
  - Performance monitoring
  - Real-time notifications

---

## Resources by Topic

### Python Learning Resources
- Official Python Docs: https://docs.python.org/3/
- Real Python: https://realpython.com/
- Python Enhancement Proposals (PEPs): https://www.python.org/dev/peps/
- Books: "Fluent Python", "Effective Python"

### Playwright Resources
- Official Documentation: https://playwright.dev/python/
- GitHub: https://github.com/microsoft/playwright-python
- Examples: https://github.com/microsoft/playwright/tree/main/examples

### Testing Framework Resources
- Pytest: https://docs.pytest.org/
- Unittest: https://docs.python.org/3/library/unittest.html

### Practice Platforms
- LeetCode: Algorithm problems in Python
- HackerRank: Python challenges
- Codewars: Daily coding problems
- Real websites: Practice Playwright on real sites (ethically)

---

## Milestone Checkpoints

### Milestone 1: Python Basics (End of Week 4)
- [ ] Write program with functions
- [ ] Use all data structures
- [ ] Handle errors gracefully
- [ ] Follow PEP 8 style

### Milestone 2: OOP Mastery (End of Week 7)
- [ ] Inheritance working correctly
- [ ] Proper encapsulation
- [ ] Polymorphic behavior
- [ ] Abstract classes understood

### Milestone 3: Testing Expert (End of Week 12)
- [ ] 80%+ test coverage
- [ ] Pytest advanced features
- [ ] Mocking and patching
- [ ] Type hints everywhere

### Milestone 4: Playwright Proficient (End of Week 18)
- [ ] 50+ passing tests
- [ ] Page Objects pattern implemented
- [ ] Parallel execution working
- [ ] Advanced features (mocking, record)

### Milestone 5: Expert Level (End of Week 24)
- [ ] Can architect test/application system
- [ ] Understand performance trade-offs
- [ ] Design efficient solutions
- [ ] Mentor others

---

## How to Maximize Learning

### ✅ DO:
- Type every single code example
- Break code on purpose to understand errors
- Explain concepts out loud
- Build projects incrementally
- Read other people's code
- Practice daily, even 15 minutes

### ❌ DON'T:
- Only watch videos without coding
- Copy-paste code
- Skip error messages
- Jump to advanced topics too early
- Leave projects unfinished
- Study in 6-hour marathon sessions

---

## Success Metrics

### By Week 4 (Python Basics)
- Can solve simple programming problems
- Understand data structures
- Clean code with functions

### By Week 12 (Intermediate)
- OOP code is natural
- Testing is automatic
- Code quality passes lint checks

### By Week 20 (Playwright)
- Test suite runs reliably
- Understand Playwright deeply
- Can debug test failures

### By Week 24 (Expert)
- Design systems, not just code
- Optimize for performance
- Can learn new tools quickly
- Help others learn

---



## What is Playwright?

Playwright is a modern browser automation framework by Microsoft. It's like a robot that controls your browser - perfect for:
- **Web Automation:** Automate repetitive browser tasks
- **Test Automation:** Test web applications across browsers
- **Web Scraping:** Extract data from dynamic websites
- **Performance Testing:** Measure real user scenarios
- **Screenshot/Video Recording:** Document test results

**Why Playwright over Selenium?**
- Faster (better architecture)
- Works across Chromium, Firefox, WebKit (not just Chrome)
- Better handling of async operations
- Built-in support for multiple contexts, cookies, etc.
- Better debugging tools
- Cleaner API

---

## Installation & Setup

```python
# Install Playwright
pip install playwright

# Download browser binaries (one-time)
playwright install

# Install pytest plugin for testing
pip install pytest-playwright

# Install with specific browser support
playwright install chromium
playwright install firefox
playwright install webkit
```

---

## Basic Playwright Usage

### 1. Synchronous API (Simple, Blocking)

```python
from playwright.sync_api import sync_playwright

# Context manager handles setup/cleanup
with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)  # headless=True for CI/CD
    
    # Create a page
    page = browser.new_page()
    
    # Navigate
    page.goto("https://example.com")
    
    # Interactions
    page.fill("input[name='search']", "Playwright")
    page.click("button:has-text('Search')")
    page.wait_for_load_state("networkidle")
    
    # Get content
    title = page.locator("h1").text_content()
    print(title)
    
    # Screenshot
    page.screenshot(path="screenshot.png")
    
    # Cleanup
    browser.close()
```

### 2. Asynchronous API (Concurrent, Non-Blocking)

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto("https://example.com")
        await page.fill("input", "text")
        
        await browser.close()

asyncio.run(main())
```

---

## Locators & Selectors - Finding Elements

**Modern Playwright uses Locators (recommended):**

```python
# CSS selectors
page.locator("button.submit")
page.locator("input[type='password']")

# XPath
page.locator("//button[@id='submit']")

# Text-based (great for buttons/links)
page.locator("button:has-text('Click Me')")
page.locator("text=Welcome")

# Role-based (accessibility-friendly, recommended)
page.locator("role=button[name='Submit']")
page.locator("role=textbox[name='Username']")

# Get multiple elements
items = page.locator(".item")
for i in range(items.count()):
    print(items.nth(i).text_content())

# Filter locators
rows = page.locator("tr")
filtered = rows.filter(has_text="John")
```

---

## Common Interactions

```python
page = browser.new_page()

# Input text
page.locator("input").fill("Hello")
page.locator("input").type("Slowly", delay=100)  # Type slowly

# Click
page.locator("button").click()

# Double click and right click
page.locator("button").dblclick()
page.locator("button").click(button="right")  # Right click

# Select from dropdown
page.locator("select").select_option("option2")

# Checkbox and radio
page.locator("input[type='checkbox']").check()
page.locator("input[type='radio']").check()

# Upload file
page.locator("input[type='file']").set_input_files("path/to/file.txt")

# Keyboard actions
page.keyboard.press("Enter")
page.keyboard.type("password123")
page.keyboard.down("Shift")
page.locator("input").click()
page.keyboard.up("Shift")

# Get values
value = page.locator("input").input_value()
text = page.locator("div").text_content()
html = page.locator("div").inner_html()

# Check visibility
is_visible = page.locator("button").is_visible()
is_checked = page.locator("input").is_checked()
is_disabled = page.locator("button").is_disabled()
```

---

## Waiting & Synchronization

**Critical for reliable tests - wait for elements to appear:**

```python
# Wait for element to appear
page.wait_for_selector("button.loaded")

# Wait for locator
page.locator("button").wait_for()

# Wait for specific load state
page.wait_for_load_state("networkidle")  # Network idle
page.wait_for_load_state("domcontentloaded")  # DOM ready

# Wait with timeout
try:
    page.locator("rare-button").wait_for(timeout=5000)
except:
    print("Element didn't appear in 5 seconds")

# Wait for function (custom logic)
page.wait_for_function("() => document.readyState === 'complete'")

# Wait for URL
page.wait_for_url("**/thank-you")

# Wait for navigation
with page.expect_navigation():
    page.click("a[href='/next']")

# Wait for popup
with page.expect_popup() as popup_info:
    page.click("a[target='_blank']")
popup = popup_info.value
```

---

## Request & Response Interception

```python
# Listen to requests and responses
def handle_request(request):
    print(f"Request: {request.url}")

def handle_response(response):
    print(f"Response: {response.url} - {response.status}")

page.on("request", handle_request)
page.on("response", handle_response)

# Block specific resources (speed up tests)
page.route("**/*.{png,jpg,jpeg,gif,svg}", lambda route: route.abort())

# Mock API responses
def handle_route(route):
    if "api.example.com" in route.request.url:
        route.abort()  # Block API call
    else:
        route.continue_()

page.route("**/*", handle_route)

# Respond with mocked data
def mock_api(route):
    route.fulfill(
        status=200,
        headers={"Content-Type": "application/json"},
        body=json.dumps({"status": "success"})
    )

page.route("**/api/data", mock_api)
```

---

## Test Automation with pytest-playwright

```python
# conftest.py - Shared fixtures
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

# test_example.py
def test_login(page):
    page.goto("https://example.com/login")
    page.fill("input[name='username']", "user@example.com")
    page.fill("input[name='password']", "password123")
    page.click("button:has-text('Login')")
    
    # Assert
    assert page.locator("h1:has-text('Dashboard')").is_visible()

def test_shopping_flow(page):
    page.goto("https://example.com")
    page.click("text=Products")
    page.click(".product:nth-of-type(1)")
    page.click("button:has-text('Add to Cart')")
    
    assert page.locator("text=Added to cart").is_visible()

# Run with pytest
# pytest test_example.py
# pytest test_example.py -k login  # Run specific test
# pytest --headed  # Show browser
# pytest -n 4  # Run 4 tests in parallel (needs pytest-xdist)
```

---

## Page Objects Pattern

**Best practice for maintainable test code:**

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button:has-text('Login')")
        self.error_message = page.locator(".error-message")
    
    def navigate(self):
        self.page.goto("https://example.com/login")
    
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def is_error_shown(self):
        return self.error_message.is_visible()

# pages/dashboard_page.py
class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.welcome_text = page.locator("h1")
    
    def is_logged_in(self):
        return self.welcome_text.is_visible()

# tests/test_login.py
def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("user@example.com", "password123")
    
    dashboard = DashboardPage(page)
    assert dashboard.is_logged_in()

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("wrong@example.com", "wrong")
    
    assert login_page.is_error_shown()
```

---

## Advanced Features

### 1. Screenshots & Videos

```python
# Single screenshot
page.screenshot(path="screenshot.png")

# Screenshots for comparison
page.screenshot(path="before.png")
# ... make changes ...
page.screenshot(path="after.png")

# Full page screenshot
page.screenshot(path="full_page.png", full_page=True)

# Record video
browser = p.chromium.launch()
context = browser.new_context(record_video_dir="videos/")
page = context.new_page()
# ... run test ...
context.close()  # Video saved automatically
```

### 2. Authentication & Cookies

```python
# Save cookies after login
context = browser.new_context()
page = context.new_page()
page.goto("https://example.com/login")
page.fill("input[name='username']", "user")
page.fill("input[name='password']", "pass")
page.click("button:has-text('Login')")
page.context.storage_state(path="auth.json")  # Save auth

# Use saved cookies in future tests
context = browser.new_context(storage_state="auth.json")
page = context.new_page()
page.goto("https://example.com/dashboard")  # Already logged in!
```

### 3. Mobile Emulation

```python
# Desktop browser
page = browser.new_page()

# Mobile device emulation
iphone = p.devices["iPhone 12"]
context = browser.new_context(**iphone)
page = context.new_page()
page.goto("https://example.com")

# Custom viewport
page = browser.new_page(viewport={"width": 1920, "height": 1080})

# Slow network
page = browser.new_page()
page.route("**/*", lambda route: route.continue_())
# Network throttling
page.context.set_extra_http_headers({})  # Reset
```

### 4. Geolocation & Timezone

```python
context = browser.new_context(
    geolocation={"latitude": 37.7749, "longitude": -122.4194},
    timezone_id="America/Los_Angeles",
    locale="en-US"
)
page = context.new_page()
```

---

## Common Playwright Patterns

### Testing with Assertions

```python
import pytest
from playwright.sync_api import expect

def test_button_text(page):
    page.goto("https://example.com")
    
    # Assertions with auto-waiting
    expect(page.locator("button")).to_have_text("Click me")
    expect(page.locator("button")).to_be_visible()
    expect(page.locator("button")).to_be_enabled()
    expect(page.locator("input")).to_have_value("")
    
    # Count elements
    expect(page.locator(".item")).to_have_count(5)
```

### Handling Alerts

```python
# Listen to alerts
page.on("dialog", lambda dialog: dialog.accept())

# Dismiss alert
def handle_alert(dialog):
    print(f"Alert: {dialog.message}")
    dialog.dismiss()

page.on("dialog", handle_alert)
```

### Multiple Tabs/Windows

```python
with page.expect_popup() as popup_info:
    page.click("a[target='_blank']")  # Opens in new tab

new_page = popup_info.value
new_page.goto("https://example.com")
```

---

## Debugging Playwright Tests

```python
# 1. Headed mode - see browser
playwright.launch(headless=False)

# 2. Slow motion
playwright.launch(slow_mo=1000)  # 1 second delay per action

# 3. Debug mode
# Set environment variable:
# PWDEBUG=1 pytest test_file.py
# This opens Inspector with step-through debugging

# 4. Screenshots on failure (in pytest)
@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png")

# 5. Logs
page.context.tracing.start(screenshots=True, snapshots=True)
# ... run test ...
page.context.tracing.stop(path="trace.zip")
# View: npx playwright show-trace trace.zip

# 6. Console messages
def print_msg(msg):
    print(f"Console: {msg.text}")

page.on("console", print_msg)
```

---

## Best Practices for Playwright Tests

```python
# ✅ DO: Use explicit waits
page.wait_for_load_state("networkidle")
page.locator("element").wait_for()

# ❌ DON'T: Use random sleeps
# time.sleep(2)  # BAD!

# ✅ DO: Use role-based locators (accessibility)
page.locator("role=button[name='Submit']")

# ❌ DON'T: Use fragile XPaths
# page.locator("//div[@class='container']/div[3]/button")

# ✅ DO: Use Page Objects
# Encapsulate page elements in a class

# ❌ DON'T: Scattered page interactions
# Duplicated selectors everywhere

# ✅ DO: Handle errors gracefully
try:
    page.goto(url, timeout=5000)
except Exception as e:
    print(f"Navigation failed: {e}")

# ✅ DO: Use context managers
with sync_playwright() as p:
    # Automatic cleanup

# ✅ DO: Parallel testing
# pytest -n 4  # pytest-xdist

# ✅ DO: Meaningful assertions
expect(page.locator("h1")).to_have_text("Welcome User")

# ❌ DON'T: Vague assertions
# assert page.is_visible()  # What's not visible?
```

---

---

# 🚀 ADVANCED PYTHON TOPICS FOR EXPERTISE

## 1. Collections Module

Standard library module with specialized container types:

```python
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

# Counter - Count hashable objects
words = ["apple", "banana", "apple", "apple", "cherry"]
count = Counter(words)
print(count)  # Counter({'apple': 3, 'banana': 1, 'cherry': 1})

# Most common
print(count.most_common(2))  # [('apple', 3), ('banana', 1)]

# defaultdict - Auto-create default values
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
# No KeyError! Missing keys auto-create empty list

# OrderedDict - Remember insertion order (Python 3.7+ dict works too)
d = OrderedDict()
d['first'] = 1
d['second'] = 2

# namedtuple - Lightweight class
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
print(p[0], p[1])  # Also indexable

# deque - Double-ended queue (efficient for both ends)
d = deque([1, 2, 3])
d.appendleft(0)  # Fast
d.pop()  # Fast from right
d.popleft()  # Fast from left
# Better than list for queue operations
```

---

## 2. Itertools Module

Tools for efficient iteration:

```python
from itertools import chain, cycle, repeat, combinations, permutations, islice

# chain - Combine multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list(chain(list1, list2))  # [1, 2, 3, 4, 5, 6]

# cycle - Infinite cycle through values
colors = cycle(['red', 'green', 'blue'])
next(colors)  # 'red'
next(colors)  # 'green'
next(colors)  # 'blue'
next(colors)  # 'red' - starts over

# repeat - Repeat a value n times
repeated = list(repeat('x', 3))  # ['x', 'x', 'x']

# combinations - All unique combinations (order doesn't matter)
from itertools import combinations
items = [1, 2, 3, 4]
combos = list(combinations(items, 2))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# permutations - All unique arrangements (order matters)
from itertools import permutations
perms = list(permutations([1, 2, 3]))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# islice - Slice an iterator (efficient)
nums = range(100)
subset = list(islice(nums, 10, 20, 2))  # items 10-19, step 2

# tee - Create independent iterators
from itertools import tee
it1, it2 = tee([1, 2, 3])
# Now can iterate both independently
```

---

## 3. Functools Module

Tools for function programming:

```python
from functools import wraps, lru_cache, reduce, partial
import functools

# @wraps - Preserve original function metadata in decorators
def timer(func):
    @wraps(func)  # This preserves func.__name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time() - start}s")
        return result
    return wrapper

@timer
def slow_function():
    """This is slow."""
    return "done"

print(slow_function.__name__)  # "slow_function" (not "wrapper")

# @lru_cache - Memoization (cache function results)
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Fast! Results cached
print(fibonacci.cache_info())  # See cache hits/misses

# reduce - Combine sequence into single value
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)  # 120
# Processes: 1*2=2, 2*3=6, 6*4=24, 24*5=120

# partial - Pre-fill function arguments
from functools import partial
multiply = lambda x, y: x * y
times_two = partial(multiply, 2)
print(times_two(5))  # 10 (2 * 5)
# Useful for callbacks

# Real example: Create specialized functions
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(5))  # 25
print(cube(5))    # 125
```

---

## 4. Deep vs Shallow Copy

Critical for mutable objects:

```python
import copy

# Shallow copy - copies outer object, but inner objects still referenced
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] - CHANGED!
# Inner lists still share reference

# Deep copy - completely independent copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 999
print(original)  # [[1, 2], [3, 4]] - Unchanged!

# Assignment vs copy
a = [1, 2, 3]
b = a          # Reference to same list
b[0] = 999
print(a)       # [999, 2, 3] - Changed!
```

---

## 5. Performance Optimization & Profiling

```python
import timeit
import cProfile
import pstats

# timeit - Measure execution time
# Command line:
# python -m timeit "'-'.join(map(str, range(100)))"

# In code:
setup = "nums = list(range(1000))"
statement = "sum(nums)"
time_taken = timeit.timeit(statement, setup, number=100000)
print(f"Average: {time_taken/100000}s")

# cProfile - Where is time spent?
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Option 1: Profiling in code
cProfile.run('fibonacci(30)')

# Option 2: Command line
# python -m cProfile -s cumulative script.py

# Real optimization example:
# BAD - Creates new list each iteration
result = ""
for word in words:
    result += word  # Linear search, creates new string each time!

# GOOD - Use join
result = "".join(words)  # O(n) time
```

---

## 6. Abstract Base Classes (ABC)

Force subclasses to implement methods:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base - cannot instantiate directly"""
    
    @abstractmethod
    def area(self):
        """Must implement in subclass"""
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    # Regular method (optional to override)
    def description(self):
        return f"I'm a {self.__class__.__name__}"

# Can't do this:
# shape = Shape()  # TypeError: Can't instantiate abstract class

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# This works:
c = Circle(5)
```

---

## 7. Dataclasses (Modern Alternative to namedtuple)

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown@example.com"  # Default value
    hobbies: List[str] = field(default_factory=list)  # Mutable default

p = Person("Alice", 25)
print(p)  # Person(name='Alice', age=25, email='unknown@example.com', hobbies=[])

# Automatically got __init__, __repr__, __eq__!
p2 = Person("Bob", 25)
print(p == p2)  # False (different names)

# With frozen=True (immutable)
@dataclass(frozen=True)
class Point:
    x: int
    y: int

point = Point(1, 2)
# point.x = 5  # TypeError - frozen
```

---

## 8. Slots - Memory Optimization

```python
# Normal class - uses __dict__ for attributes
class PersonNormal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# With slots - fixed attributes, less memory
class PersonSlots:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Slots advantages:
# - Less memory (~40% for thousands of objects)
# - Slightly faster attribute access
# Disadvantages:
# - Can't add new attributes dynamically
# - More complex to maintain

# Use slots for:
# - Performance-critical code
# - Millions of objects
# - Not for normal application code
```

---

## 9. Enum - Defined Set of Values

```python
from enum import Enum, IntEnum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Access
color = Color.RED
print(color.name)    # 'RED'
print(color.value)   # 1

# Iteration
for color in Color:
    print(color)

# IntEnum - can compare with integers
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

if Priority.HIGH > Priority.LOW:
    print("HIGH priority")

# auto() - auto-increment values
class Status(Enum):
    PENDING = auto()      # 1
    APPROVED = auto()     # 2
    REJECTED = auto()     # 3
```

---

## 10. Advanced Testing with Pytest

```python
# conftest.py - Shared fixtures
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

@pytest.fixture(scope="session")
def database():
    """Setup once per test session"""
    db = connect_database()
    yield db
    db.close()

# test_math.py
def test_sum(sample_data):
    assert sum(sample_data) == 15

# Parametrize - Run test multiple times
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input**2 == expected

# Markers - Organize tests
@pytest.mark.smoke
def test_critical_feature():
    pass

@pytest.mark.slow
def test_integration():
    pass

# Run only smoke tests:
# pytest -m smoke

# Fixtures with params
@pytest.fixture(params=[1, 2, 3])
def numbers(request):
    return request.param

def test_with_numbers(numbers):
    assert numbers > 0  # Runs 3 times
```

---

## 11. Debugging Techniques

```python
# 1. pdb - Python Debugger
import pdb

def buggy_function():
    x = 5
    pdb.set_trace()  # Execution stops here
    y = x + 10
    return y

# In debugger:
# l     - list code
# n     - next line
# s     - step into function
# c     - continue
# p var - print variable
# h     - help

# 2. Logging (instead of print)
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug info")
logger.info("General info")
logger.warning("Warning!")
logger.error("Something failed")

# 3. Assertions (catches logic errors)
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

# 4. Exception information
try:
    1 / 0
except Exception:
    import traceback
    traceback.print_exc()  # Full error details
```

---

## 12. Virtual Environments & Packaging

```bash
# Create virtual environment
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows

# Create requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Package your code (setup.py)
# Or modern: pyproject.toml + setup.py
```

```python
# setup.py
from setuptools import setup

setup(
    name="mypackage",
    version="1.0.0",
    py_modules=["mymodule"],
    install_requires=[
        "requests>=2.25.0",
        "pytest>=6.0.0",
    ],
)

# Install your package
# pip install -e .  (editable/development mode)
```

---

## 13. Code Quality Tools

```bash
# Linting - Check code style
pip install flake8 pylint black

# Black - Auto-format code
black myfile.py

# Flake8 - Lint checker
flake8 myfile.py

# Pylint - Detailed code analysis
pylint myfile.py

# Type checking
pip install mypy

# mypy - Static type checks
mypy myfile.py
```

---

## 14. Configuration Management

```python
# config.py - Centralized configuration
import os
from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).parent
    DEBUG = os.getenv("DEBUG", False)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")

# Use in app
from config import Config

print(Config.DEBUG)
print(Config.DATABASE_URL)

# With environment files (.env)
pip install python-dotenv

# .env file
DEBUG=True
DATABASE_URL=postgresql://user:pass@localhost/db

# Load in code
from dotenv import load_dotenv
load_dotenv()
```

---

## 15. Advanced Async/Await

```python
import asyncio

# Concurrent tasks
async def fetch(url):
    await asyncio.sleep(1)  # Simulate I/O
    return f"Data from {url}"

async def main():
    tasks = [
        fetch("http://1.com"),
        fetch("http://2.com"),
        fetch("http://3.com"),
    ]
    results = await asyncio.gather(*tasks)  # Run concurrently
    print(results)

# With timeout
async def main():
    try:
        result = await asyncio.wait_for(fetch("http://1.com"), timeout=2.0)
    except asyncio.TimeoutError:
        print("Request timed out")

# Real-world: Async HTTP requests
import aiohttp

async def fetch_multiple(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses
```

---

## 16. Pathlib - Modern File Handling

```python
from pathlib import Path

# Create path object
p = Path("data/files/document.txt")

# Path operations
print(p.name)           # 'document.txt'
print(p.stem)           # 'document'
print(p.suffix)         # '.txt'
print(p.parent)         # Path('data/files')

# Check existence
if p.exists():
    print("File exists")

# Create directories
p.parent.mkdir(parents=True, exist_ok=True)

# Write/read
p.write_text("Hello world")
content = p.read_text()

# Glob (find files)
for py_file in Path(".").glob("**/*.py"):
    print(py_file)
```

---

## Expert Python Summary

**To be a Python expert, master:**

1. ✅ Core data structures deeply (lists, dicts, sets, tuples)
2. ✅ OOP principles (classes, inheritance, polymorphism, encapsulation)
3. ✅ Functional programming (lambdas, map, filter, reduce, comprehensions)
4. ✅ Decorators and context managers
5. ✅ Async/await for concurrent programming
6. ✅ Testing frameworks (pytest, unittest)
7. ✅ Standard library (collections, itertools, functools, pathlib)
8. ✅ Profiling and optimization
9. ✅ Virtual environments and packaging
10. ✅ Type hints and static analysis
11. ✅ Debugging techniques
12. ✅ Code quality tools

---

Good luck on your journey to master both Python and Playwright! 🚀