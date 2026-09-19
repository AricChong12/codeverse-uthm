# A List of Dictionaries

# A list can contain multiple dictionaries.
# Here, each dictionary represents one message.
messages = [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there!"},
]

print(messages)
print(messages[0])
# First, use the list index [0] to select the first message.
# Then, use the dictionary key ["content"] to get its content.
print(messages[0]["content"])
print(messages[1]['role'])

