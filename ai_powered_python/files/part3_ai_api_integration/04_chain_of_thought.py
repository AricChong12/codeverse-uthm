# Technique 4 of 4 - Step-by-Step Prompting

# For problems involving multiple steps, we can ask the AI
# to solve the problem step by step.

from groq_client import client


response = client.chat.completions.create(

    model="openai/gpt-oss-120b",

    messages=[
        {
            "role": "user",
            "content": "A shop had 84 apples and sold 3 boxes of 12. "
                       "How many are left? "
                       "Give a short step-by-step solution."
        }
    ],

)


# Get the AI's response from the response object.
print(response.choices[0].message.content)

# -> 3 x 12 = 36 sold.
# -> 84 - 36 = 48 left.