# Decorators: Its a function that wraps another fn
# Without modifiying the original fn behaviour

# Think like function + extra logic

# We can assign fn to a varables

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

