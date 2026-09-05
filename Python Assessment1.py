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

print("Q8: Find all duplicate elements in a list.")
numbers = [1,2,3,2,4,5,1]
seen = []
duplicates = []

for element in numbers:
    if element in seen:
        if element not in duplicates:
            duplicates.append(element)
    else:
        seen.append(element)
print("Duplicates: ", duplicates)

print("Q9: Rotate a list by K positions.")
lst= [1,2,3,4,5]
k = 2

rotated_lst = lst[-k: ] + lst[: -k]
print(rotated_lst)

print("Q10: Find intersection of two lists.")
lst1 = [1,2,3,4]
lst2 = [3,4,5,6]

intersection_value = []
for n in lst1:
    if n in lst2 and n not in intersection_value:
        intersection_value.append(n)
print("Intersection of two list is: ", intersection_value)

print("Q11: Count the frequency of elements in a list using dictionary.")
lst_given = [1,2,2,3,3,3]

dict = {}
for x in lst_given:
    if x in dict:
        dict[x] = dict[x] + 1
    else:
        dict[x] = 1
print(dict)

print("Q12: Find the key having maximum value.")

dct = {"A":100,"B":500, "C":300}
max_key = None
max_value = None

for key, value in dct.items():
    if max_value is None:
        max_key = key
        max_value = value
    else:
        if value > max_value:
            max_key = key
            max_value = value
print(max_key)

print("Q13: Reverse a dictionary.")
dict = {"a": 1, "b":2}
reversed_dict = {}
for key, value in dict.items():
    reversed_dict[value] = key
print(reversed_dict)

print("Q14: Merge two dictionaries.")

dict1= {"a": 1}
dict2 = {"b": 2}

merge_dict = dict1 | dict2
print(merge_dict)
