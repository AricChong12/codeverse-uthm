# Demo 1 - Explain Code

# Ask an LLM to explain unfamiliar code.
#
# Prompt:
# "Explain this function line by line for a beginner.
# What does each part do, and what would I use it for
# in a real program?"


def mystery(nums):
    total = 0

    for n in nums:
        if n % 2 == 0:
            total += n

    return total


print(mystery([1, 2, 3, 4, 5, 6]))