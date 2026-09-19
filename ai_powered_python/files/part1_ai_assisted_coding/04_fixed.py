# Demo 3 - Debug (Fixed Version)

# The LLM suggested changing len(num) to len(nums).
# Review the change and test the code to make sure it works.
#
# Prompt:
# "Review this fixed code.
# Is the error fixed correctly?
# Explain what was changed and why."


def average(nums):
    return sum(nums) / len(nums)


if __name__ == "__main__":
    print(average([10, 20, 30]))
    # -> 20.0
