# Decorators: Its a function that wraps another fn
# Without modifiying the original fn behaviour
# A decorator in Python is a function that wraps another
#  function to extend its behavior without modifying 
# the original function. It leverages 
# first-class functions and closures and is
#  commonly used for logging, retry logic, 
# access control, and framework-level enhancements.
# Think like function + extra logic

# We can assign fn to a varables

# Why decorators are important for you

# ✔ retry logic
# ✔ logging
# ✔ timing execution
# ✔ auth handling
# ✔ screenshots on failure
# ✔ reporting hooks

# Pytest Uses Decorators Everywhere
# @pytest.fixture
# def setup(): pass

# @pytest.mark.smoke
# def test_login(): pass


def greet():
    return "Hello,world"

say_hello = greet
print(say_hello())

# Function inside a funcation

def outer():
    def inner():
        return "Hello from inner"
    return inner()

print(outer())

# Fn that accepts another fn

def my_main_fn(greet):
    def wrapper():
        print("Before calling greet")
        greet()
        print("After calling greet")
    return wrapper

# Instead of manual wrapping , we have annotation with @

@my_main_fn
def greet2():
    print("hello from greet2")

print(greet2())
#  this is equal to greet2 = my_main_fn(greet2)

# Example of decorator with real world solutions

def log(func):
    def wrapper():
        print(f"Logging before calling {func.__name__}")
        fun = func()
        print(f"logging after calling {func.__name__}")
        return fun
    return wrapper

@log
def say_login():
    print("User Logged in")

say_login()

# Best example is retry logic

def retry(func):
    def wrapper():
        for __ in range(3):
            try:
                return func()
            except:
                print(f"Retrying {func.__name__}")
        return wrapper()
    return func()

@retry
def call_api_with_retry():
    print("Calling API and failing it")
    raise Exception("Fail")

call_api_with_retry()


def main_fn(func):
    def wrapper():
        print("START")
        func()
        print("END")
    return wrapper

@main_fn
def test_fn():
    print("Main test")

test_fn()