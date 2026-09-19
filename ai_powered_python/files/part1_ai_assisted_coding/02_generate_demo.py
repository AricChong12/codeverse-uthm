# Demo 2 - Generate Code

# Ask an LLM to generate a Python function from a plain-English request.
#
# Prompt:
# "Write a Python function that takes a list of prices and
# returns the total after a given discount percent.
# Include a docstring and a type hint."


def discounted_total(prices: list[float], discount_percent: float) -> float:
    """Return the total price after applying a percentage discount."""
    total = sum(prices)
    return total * (1 - discount_percent / 100)



print( discounted_total([10, 20, 405, 67, 78], 10) )
