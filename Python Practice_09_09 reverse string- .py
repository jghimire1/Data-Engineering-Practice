# Reverse a String
# Write a Python function to reverse a given string.
# Input: "hello"
# Output: "olleh"

input_str = "hello"
reversed_str = ''

for x in input_str:
    reversed_str = x + reversed_str
print(reversed_str)


