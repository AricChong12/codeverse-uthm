# Control Flow: if / for / while

for number in [10, 20, 30, 40]:
    print(number)
print('*********************')

# A for loop repeats the code once for each item in the list.
for n in [1, 2, 3, 4]:
    # Check whether n is an even number.
    if n % 2 == 0:
        print(n, "is even")
    else:
        # continue skips the rest of the current loop
        # and moves to the next item.
        continue


# Start a counter at 0.
count = 0
# A while loop keeps running as long as the condition is True.
while count < 3:
    # Display the current value of count.
    print("count =", count)

    # Increase count by 1 each time the loop runs.
    count += 1

    # Stop the loop when count reaches 2.
    if count == 2:
        break # break out of the loop
