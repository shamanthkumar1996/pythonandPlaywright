# List

list_example = [1,2,3,"shamanth",5.6]
list_example.append("new_item")
list_example.remove(2)
list_example[0]= 10
list_example.insert(2,"inserted_item")

print("List Example:", list_example)

# Tuple

tuple_example = (1,2,3,"shamanth",5.6)
# Tuples are immutable, so we cannot modify them like lists
# tuple_example[0] = 10  # This would raise an error

# sets
set_example = {1,2,3,"shamanth",5.6}
set_example.add("new_item")
set_example.remove(1)
print("Set Example:", set_example)
set_example.add(3)  # Adding duplicate item, will have no effect
# Sets are unordered collections of unique items
# ✔ Unordered
# ✔ Collection of unique values
# ✔ Mutable (you can add/remove items)
# ✔ Fast for lookup & membership tests

# Why do we needs sets?
# 1. To eliminate duplicate values from a collection
# 2. To perform mathematical set operations like union, intersection, difference

# Remove duplicate test data 
emails = ["a@test.com","a@test.com","b@test.com"]
unique_emails = set(emails)
print("Unique Emails:", unique_emails)

# To find missing data 
expected = {"NY","LA","SF"}
actual = {"NY","LA","SF","Chicago"}

print(actual - expected)

# Fast lookup in validation
blocked_users = {"u1","u2","u3"}
user_id ="u4"
if user_id in blocked_users:
    print("User is blocked")

# Sets Union, Intersection, Difference
# Union A | B
A = {1,2,3}
B = {3,4,5}

print(A | B)
#  out put : {1, 2, 3, 4, 5}
# Intersection A & B
print(A & B)
# out put : {3}

# DIFFERENCE — Items in A but NOT in B

print(A - B)
# out put : {1, 2}

# Sets with Symmetric Difference — Items in A or B but NOT in both
print(A ^ B)
# out put : {1, 2, 4, 5}

# Dictionary

dict_example ={
    "name":"Shamanth",
    "age":30,
    "role":"Automation engineer lead",
    "Skills":["python","Selenium","APIS"],
    "male": True,
    20: "twenty"
}

for key,value in dict_example.items():
    print(f"{key}: {value}")

print("Dictionary Example:", dict_example["Skills"])

# Modifying dictionary
dict_example["age"] = 31
dict_example["location"] = "USA"
print("Modified Dictionary Example:", dict_example)
# Removing item
del dict_example[20]
print("After Deletion Dictionary Example:", dict_example)
# Nested Dictionary
nested_dict = {
    "employee1": {
        "name": "Shamanth",
        "age": 30
    },
    "employee2": {
        "name": "Alice",
        "age": 28
    }
}
print("Nested Dictionary Example:", nested_dict["employee1"]["name"])

for emp_id, details in nested_dict.items():
    print(emp_id, details)

#  Inner loops

for emp_id,details in nested_dict.items():
    for key,values in details.items():
        print(f"{key}:{values}")
# Print only values

for details in nested_dict.values():
    print("values", details)

for details in nested_dict.values():
    for values in details.values():
        print(values)

#  Convert all keys to index

keys = list(nested_dict.keys())
print("Keys as list:", keys)

print("using index",nested_dict[keys[1]]["name"])
# List Comprehension — Extract All Names
names = [abc["name"] for abc in nested_dict.values()]
print("Names List:", names)

# Different ways to print 
# We have Multiline f-strings
# You can write f-strings across multiple lines — super useful for logging, reports, API debugging, etc.

name = "Shamanth"
role = "SDET"
exp = 7

message = f"""
User Details:
Name: {name}
Role: {role}
Experience: {exp} years
"""

print(message)
# Number Formatting with f-strings
number = 123.2323233
print(f"number formate: {number:.2f}")

# Thusands separator
big_number = 1000000
print(f"Big number: {big_number:,}")

# Align text 
print(f"{'Item':<10} {'Price':>10}")
print(f"{'Shoes':<10} {1999:>10}")

# Json module
import json

response = {
    "user":"Shamanth",
    "role":"SDET",
    "skills":["Python","Playwright","API"]
}

print(json.dumps(response, indent=4))
