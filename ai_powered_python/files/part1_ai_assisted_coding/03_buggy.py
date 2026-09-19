# Demo 3 - Debug (Buggy Version)

# Give the LLM the code and the error message.
#
# Prompt:
# "Why am I getting this error?
# Explain the problem in simple terms and show me how to fix it.
# Do not change anything else in the code."


def average(nums):
    return sum(nums) / len(nums)


if __name__ == "__main__":
    print(average([10, 20, 30]))
