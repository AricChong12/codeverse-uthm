# Dictionaries

# A dictionary stores data as key-value pairs.
student = {
    "name": "Aisyah",
    "age": 21
}

print(student)

# Use the key to access its corresponding value.
# Unlike a list, we don't use a numeric index here.
print(student["name"])
# -> Aisyah

# Update the value associated with an existing key.
student["age"] = 22

# Add a new key-value pair to the dictionary.
student["city"] = "JB"

print(student)
# -> {'name': 'Aisyah', 'age': 22, 'city': 'JB'}