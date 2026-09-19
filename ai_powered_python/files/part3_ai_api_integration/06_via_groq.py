# Bonus - Compare Providers

# The same chat-completion style can be used with Groq.

import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables from the .env file.
load_dotenv()


# Create a Groq client using the API key from the environment.
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


# Send a request to the AI model.
response = client.chat.completions.create(

    model="openai/gpt-oss-120b",

    messages=[
        {
            "role": "user",
            "content": "Explain recursion."
        }
    ],

)

# Extract the AI's text reply from the response.
reply = response.choices[0].message.content

print(reply)
