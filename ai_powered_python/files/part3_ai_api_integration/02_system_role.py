# Technique 2 of 4 - System Role

# A system message gives the AI instructions about its role
# or how it should behave.

from groq_client import client


# Send a request with a system instruction and a user request.
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Python Instructor. Explain concepts simply for beginners."
        },
        {
            "role": "user",
            "content": "What is a Python dictionary?"
        }
    ],
)


# Get the AI's response.
print(response.choices[0].message.content)