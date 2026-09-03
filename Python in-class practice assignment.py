

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

# remove duplicates from a list
# Write a Python function to remove duplicates from a list while preserving the order.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]
print(" Removing Duplicates ------------")
input_list = [1, 2, 2, 3, 4, 4, 5]
removed_duplicates = []
for num in input_list:
     if num not in removed_duplicates:
         removed_duplicates.append(num)
print(removed_duplicates)

# Find the Intersection of Two Lists
# Write a Python function to find the intersection of two lists.
# Input: [1, 2, 3, 4], [3, 4, 5, 6]
# Output: [3, 4]
print(" Finding common elements of the two list...........")
input_list1 = [1, 2, 3, 4]
input_list2 = [3, 4, 5, 6]

common_value = []

for x in input_list1:
    if x in input_list2 and x not in common_value:
        common_value.append(x)
print(common_value)

# 09/02/2026 In class practice 
#Flatten a Nested List
#Write a Python function to flatten a nested list.
input_list: [[1, 2], [3, 4], [5]]
#Output: [1, 2, 3, 4, 5]

flat_list = []
for x in input_list:
    if isinstance(x, list):
        flat_list.extend(x) 
    else:
        flat_list.append(x)
print(flat_list)

#Merge Two Sorted Lists
#Write a Python function to merge two sorted lists into a single sorted list.
# Input: [1, 3, 5], [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

print("Using merged and sort ---------")

input1 = [1,3,5]
input2 = [2,4,6,]
merged_list1 = input1 + input2


merged_list1.sort()
print(merged_list)

#Find All Pairs in a List that Sum to a Specific Value
#Write a Python function to find all pairs in a list that sum to a specific value.
#Input: [1, 2, 3, 4, 5], Sum=6
#Output: [(1, 5), (2, 4)]

input_list4 = [1, 2, 3, 4, 5]
target = 6
pairs= []

# looping through each element
for i in range(len(input_list4)):
    for j in range(i+1, len(input_list4)):
        #looping through remaining elements to avoid duplicates and self pairing
        if input_list4[i] + input_list4[j] == target:
            pairs.append((input_list4[i], input_list4[j]))
print(pairs)
 
