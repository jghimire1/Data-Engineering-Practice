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

print("Q3: Check if a string is a palindrome.-------------")
string_pal = "madam"
is_palindrome = ""

for x in string_pal:
    is_palindrome = x + is_palindrome

is_palindrome = (string_pal == is_palindrome)
print(is_palindrome)

print("Q4:Count the frequency of each character in a string.")
given_str = "hello"
frequency = {}

for x in given_str:
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1
for x, frequency in frequency.items():
    print(x,":",frequency, end =",")

print()
