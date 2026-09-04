# Section A - Strings
print("Q1: Write a program to reverse a string without using slicing.")
# Example: Input: “python” Output: “nohtyp”

input_str = "python"

reversed_str = ""
for x in input_str:
    reversed_str = x + reversed_str
print(reversed_str)

print("Q2: Find the first non-repeating character in a string.")

char_str = "programming"

char_counts = {}
for x in char_str:
    if x in char_counts:
        char_counts[x] += 1
    else:
        char_counts[x] = 1
count_result = None
for x in char_str:
    if char_counts[x] == 1:
        count_result = x
        break
print(count_result)
