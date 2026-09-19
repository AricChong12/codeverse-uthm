# Lists & Indexing

# A list stores multiple values in a single variable.
fruits = ["apple", "banana", "cherry"]

print(fruits)

# List indexing starts at 0, not 1.
print(fruits[0])
# -> apple

# Index 1 refers to the second item.
print(fruits[1])
# -> banana

# len() tells us how many items are in the list.
print(len(fruits))
# -> 3

# append() adds a new item to the end of the list.
fruits.append("mango")

print(fruits)
# -> ['apple', 'banana', 'cherry', 'mango']