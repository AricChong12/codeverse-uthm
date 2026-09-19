# Technique 3 of 4 - Few-Shot Prompting

# Few-shot prompting gives the AI a few examples
# before asking it to perform the task.

from groq_client import client


# The examples show the AI how we want the classification to work.
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": """Classify each review as Positive or Negative.

Example 1:
Review: "The camera quality is excellent."
Answer: Positive

Example 2:
Review: "The battery dies very quickly."
Answer: Negative

Now classify:
Review: "The screen is bright and clear."
Answer:"""
        }
    ],
)


# Get the AI's response.
print(response.choices[0].message.content)