# Functions & Arguments

# A function is a reusable block of code.
# "name" is a required parameter.
# "excited=False" gives "excited" a default value.
def greet(name, excited=False):
    # Check whether the excited argument is True.
    if excited:
        return f"HELLO {name}!"

    # return sends a value back to the code that called the function.
    return f"Hello, {name}."


# "Aisyah" is passed as a positional argument.
print(greet("Aisyah"))
print(greet("Aisyah", True))
# -> Hello, Aisyah.
# -> HELLO, Aisyah.


# We can also pass arguments by name using keyword arguments.
print(greet(name="Aisyah", excited=True))
# -> HELLO Aisyah!
