"""
INTERVIEW-READY EXPLANATION: Java vs Python Exception Handling

In Java:
- Exceptions can be checked or unchecked
- Checked exceptions require methods to either handle them or declare them using the 'throws' keyword
- This enforces compile-time awareness of potential exceptions

In Python:
- Python does NOT have checked exceptions or a 'throws' keyword
- ALL exceptions are runtime (unchecked)
- If an exception is not handled in a function, it automatically propagates up the call stack
  until it is caught or the program terminates
- We can optionally re-raise exceptions when needed using the 'raise' statement, 
  which is similar to Java's 'throw'
"""

# Define a custom exception class that inherits from the base Exception class
# 
class myException(Exception):
    # Constructor method that initializes the custom exception with a message
    def __init__(self, message):
        # Store the error message as an instance variable
        self.message = message

    # Method that demonstrates exception handling with try-except-else-finally blocks
    def sampleException(self):
        # Try block: contains code that might raise an exception
        try:
            # Attempt to divide 10 by 0, which will raise a ZeroDivisionError
            x = 10/0
        # Except block: catches and handles the ZeroDivisionError exception
        except ZeroDivisionError as e:
            # Print the caught exception details
            print("ZeroDivisionError caught:", e)
            # Raise our custom exception with a specific error message instead
            raise myException("Custom Exception: Division by zero is not allowed.")
        # Else block: executes only if no exception occurs in the try block
        else:
            print("No exception raised.")
        # Finally block: always executes regardless of whether an exception occurred
        finally:
            print("I am cleaning up resources.")
    
# Entry point of the script - ensures code runs only when file is executed directly, not imported
if __name__ == "__main__":
    # Create an instance of the custom exception class with a message
    exception_instance = myException("This is a custom exception")
    # Try block: attempt to call the sampleException method
    try:
        exception_instance.sampleException()
    # Except block: catches the custom exception if it's raised
    except myException as me:
        # Print the custom exception message stored in the instance
        print(me.message)

# Retry handling in python exceptions

def call_api():
    raise TimeoutError("API failed")

for _ in range(3):
    try:
        call_api()
        break
    except:
        print("Retrying…")

