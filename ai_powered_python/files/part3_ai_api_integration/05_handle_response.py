# Code - Handling the Response

# An AI API response contains several useful pieces of information:
#
# response.choices[0].message.content -> the AI's text reply
# response.usage.total_tokens         -> tokens used
# response.model                      -> model that replied

from groq_client import client

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Give me one fun fact about Python."
        }
    ],

)
# Extract the AI's text reply.
answer = response.choices[0].message.content

# Extract the number of tokens used.
tokens = response.usage.total_tokens

# Extract the model name.
model = response.model


print(f"Answer: {answer}")
print(f"Tokens used: {tokens}")
print(f"Model: {model}")


# API calls use the network, so things can sometimes go wrong.
# try/except lets us handle an error without crashing the program.

try:

    # Example: make your API request here.

    ...

except Exception as e:

    print(f"AI request failed: {e}")