# Mini Project - AI Study Assistant

# This program:
# 1. Gets a topic from the user.
# 2. Builds a prompt for the AI.
# 3. Sends the prompt to the AI.
# 4. Displays the AI-generated study card.
#
# Type "quit" to exit the program.


import os

from dotenv import load_dotenv
from groq import Groq

# Load the API key from the .env file.
load_dotenv()

# Create the Groq client using the API key.
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

def build_prompt(topic: str) -> str:
    # Build a detailed prompt using the topic provided by the user.
    #
    # topic: str  -> topic should be a string.
    # -> str      -> this function returns a string.

    return f"""
You are a friendly Python tutor. Explain the topic below to a
beginner computer science student. Respond in this exact format:

1. Explanation: (2-3 simple sentences)
2. Common Uses: (2-3 bullet points)
3. Example: (a short, commented Python code block)
4. Key Points: (3-5 bullet points)
5. Quiz: (2-3 short questions, no answers)

Topic: {topic}
"""


def ask_study_assistant(topic: str) -> str:
    # Send the topic to the AI and return the study card as text.
    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "user",
                "content": build_prompt(topic)
            }
        ],

        # A lower temperature makes the response more consistent.
        temperature=0.5,
    )

    # Extract the AI's text response.
    return response.choices[0].message.content


def main():
    # Display the program title and instructions.
    print("=== AI Study Assistant ===")
    print("Type a topic to study, or 'quit' to exit.\n")

    # Keep asking for topics until the user chooses to quit.
    while True:

        # input() waits for the user to enter something.
        # strip() removes extra spaces from the beginning and end.
        topic = input("Topic: ").strip()

        # Stop the program when the user enters "quit".
        # lower() makes the check case-insensitive.
        if topic.lower() == "quit":
            break

        # Ignore empty input and ask for another topic.
        if not topic:
            continue

        try:
            # Ask the AI to create a study card.
            card = ask_study_assistant(topic)

            # Display the study card.
            print(f"\n{card}\n" + "-" * 60)

        except Exception as e:
            # Handle API or network errors without crashing the program.
            print(f"Something went wrong: {e}")

# Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()