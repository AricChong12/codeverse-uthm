# Step 1 - The Prompt

# Build a structured prompt for the AI Study Assistant.
# The topic will be inserted into the prompt dynamically.


def build_prompt(topic: str) -> str:

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