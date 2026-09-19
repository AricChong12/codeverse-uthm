# Bonus - Compare Providers
#
# The same task can be sent to a different AI provider.
# Anthropic uses its own native Python SDK.

# Install the Anthropic SDK once:
# pip install anthropic

import os

from dotenv import load_dotenv
from anthropic import Anthropic


# Load environment variables from the .env file.
load_dotenv()


# Create an Anthropic client using the API key
# stored in the environment.
client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)


# Send a message to the Claude model.
response = client.messages.create(

    model="claude-sonnet-5",

    # Claude requires us to specify the maximum output tokens.
    max_tokens=1024,

    messages=[
        {
            "role": "user",
            "content": "Explain recursion."
        }
    ],

)

# Anthropic's response structure is different from Groq's.
# Here, we access the first content item and then its text.
reply = response.content[0].text

print(reply)