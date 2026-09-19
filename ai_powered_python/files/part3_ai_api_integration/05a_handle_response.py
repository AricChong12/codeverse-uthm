# Code - Handling the Response

from groq_client import client

try:
    # Send a request to the AI model.
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


except Exception as e:

    # Handle problems such as network or API errors.
    print(f"AI request failed: {e}")

print('------------------------')
print('Script continues....')

