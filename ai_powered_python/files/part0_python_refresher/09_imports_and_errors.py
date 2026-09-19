# Imports & Handling Errors

# Python has many built-in modules that we can import and use.
import math

# sqrt() calculates the square root of a number.
print(math.sqrt(16))
# -> 4.0

# External packages may need to be installed before we can use them.
# Install a package once from the terminal:
#
# pip install requests

# After installing it, we can import and use it in our Python code.
import requests

# try/except lets us handle an error without stopping the program.
try:
    # This causes a ZeroDivisionError because we cannot divide by zero.
    result = 10 / 0

except ZeroDivisionError as e:
    # Display a friendly message instead of letting the program crash.
    print(f"Error : {e}")
# -> Oops: division by zero

print('script continues...')