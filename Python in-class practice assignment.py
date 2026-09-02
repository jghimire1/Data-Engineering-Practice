

# Find the Maximum and Minimum Elements in a List
# Write a Python function to find the maximum and minimum elements in a given list.
# Input: [3, 1, 4, 1, 5, 9]
# Output: (9, 1)
input_list = [3, 1, 4, 1, 5, 9]
min_value = input_list[0]
max_value = input_list[0]

for num in input_list:
    if num < min_value:
        min_value = num
    elif num > max_value:
        max_value = num
print(max_value,",", min_value)


