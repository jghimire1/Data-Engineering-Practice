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

print("Q5: Remove duplicate characters from a string while preserving order.")

org_str = "programming" #input ("Enter your string: ")

result = ""

for x in org_str:
    if x not in result:
        result += x
print(result)

print("Q6: Remove duplicates from a list without using set().")
input_list = [1,2,2,3,4,4]
removed_duplicates = []
for num in input_list:
     if num not in removed_duplicates:
         removed_duplicates.append(num)
print(removed_duplicates)

print("Q7: Find the second largest number in the list.")
number_list = [10,20,5,30,25]
max_value = number_list[0]

#finding max value
for num in number_list:
    if num > max_value:
        max_value = num

#finding second max value
second_max = None
for num in number_list:
    if num != max_value:
        if second_max is None or num > second_max:
            second_max = num
print(second_max)
