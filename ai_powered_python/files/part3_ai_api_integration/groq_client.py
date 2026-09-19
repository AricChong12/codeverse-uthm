# Code - Setup

# This file creates the Groq client once.
# Other Python files can then reuse it with:
#
# from groq_client import client

import os

from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file.
load_dotenv()


# Get the API key from the environment.
# This keeps the secret key out of our Python code.
api_key = os.environ.get("GROQ_API_KEY")


# Create the Groq client.
client = Groq(api_key=api_key)
