# What is a List Comprehension?
# It is a compact way to create a list from an iterable (like list, dict, range, API response, etc.)

# Basic form
# [expression for item in iterable]

#  Example 1: Creating a list of squares of numbers from 0 to 9
squares = [x*x for x in range(10)]
cubes = [x**3 for x in range(10)]
print("Squares:", squares)
print("cubes:",cubes)

# but with loops 
squares_loop = []
for i in range(10):
    squares_loop.append(i**2)
    print(f"Square of {i} is {i**2}")

# Example 2 with condition
# Include only items that match the condition
even_numbers = [ n for n in range(10) if n % 2 == 0]
print("Even numbers", even_numbers)

# With Transformation + Condition
even_squares = [ n*n for n in range(10) if n % 2 == 0]
print("Even Squares:", even_squares)

# Example 3 : using with Dict
dict_example = {
    "employee1": {
        "name": "Shamanth",
        "age": 30,
        20: "Twenty"
    },
    "employee2": {
        "name": "Alex",
        "age": 20,
        30: "ahah"
    }
}

names = [abc["name"] for abc in dict_example.values()]
print("Names from dict_example:", names)

# with condition
age_above30 = [abc["name"] for abc in dict_example.values() if abc["age"] >25]
print("Names with age above 25:", age_above30)

# Example 4: using with string 

letters = [c.upper() for c in "playwright"]
print("Uppercase Letters:", letters)

# Example 5: using with nested loops
pairs = [(x,y) for x in [1,2] for y in [3,4]]
print("Pairs from nested loops:", pairs)

# Example 6: combined output

labels = ["even" if n%2==0 else "odd" for n in range(5)]
print("Labels for numbers 0-4:", labels)

# List vs Set vs Dict Comprehension

# List
nums = [x*x for x in range(5)]
print("List Comprehension:", nums)

# Set
unique_squares = {x*x for x in [1, -1, 2, -2, 3]}
print("Set Comprehension:", unique_squares)  # Output: {1, 4, 9}

# Dict
squared_dict = {x: x*x for x in range(5)}
print("Dict Comprehension:", squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# Example 7: Flattening a nested list  
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [num for sublist in nested_list for num in sublist]
print("Flattened List:", flattened)

# Summary
"""| Concept   | Example                         | Meaning     |
| --------- | ------------------------------- | ----------- |
| Basic     | `[x for x in list]`             | copy        |
| Transform | `[x*x for x in list]`           | modify      |
| Filter    | `[x for x in list if x>5]`      | conditional |
| Dict      | `{k:v for k,v in dict.items()}` | build dict  |"""

