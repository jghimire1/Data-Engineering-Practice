data = [10,20,20,30,31,39]
print(data)
print(len(data))

for x in data:
    print(x)
print("**************")

for x in data:
    if x >= 30:
        print(x)
print("***********")

for x in data:
    if x < 30:
        print(x)
print("***********")

# print even numbers
for x in data:
    if x % 2 == 0:
        print(x)

print("*****")
#print odd numbers
for x in data:
    if x % 2 == 1:
        print(x)
print("xxxxx")
# print odd numbers that are greater than 35
for x in data:
    if x % 2 == 1 and x > 35:
        print(x)

print("xxxxx----")
# print odd numbers that are greater than 35 -- alternate method

for x in data:
    if x % 2 == 1:
        if x > 35:
            print(x)

print("-------------")
#print odd numbers that are less than 20
for x in data:
    if x % 2 == 1 and x < 20:
            print(x)
print("-------------")
# count the repeated values
count = 0
for x in data:
    if x == 20:
        count = count+1
print(count)

print("------&-------")
# count the two value
count = 0
count1 = 0
for x in data:
    if x == 20 :
        count = count+1
        #print(count)
    if x == 30:
        count1 = count1+1
print(count, count1)
print(20, count, 30, count1)

print("------&&&-------")

# count the two value
count = 0
count1 = 0
occurance = []
for x in data:
    if x == 20 :
        count = count+1
        occurance.append(count)
        #print(count)
    if x == 30:
        count1 = count1+1
        occurance.append(count1)
print(count, count1)
print(20, count, 30, count1)
print(occurance)

print("------&&&-------")
dict = {}
dict[20] = 1
print(dict)
dict[30] = 1
print(dict)
dict[20] = dict[20]+1
print(dict)

dict[30] = dict[30] + 1
print(dict)

print(20 in dict)
print(50 in dict)

print("------&*-------")
#
data = [10,20,20,30,31,39]

dict1 = {}
for x in data:
    if x in dict1:
        dict1[x] =dict1[x] + 1 #{10:1, 20:1, 20:2, 30:1, 31:1,39:1}
    else:
        dict1[x] = 1
print(dict1)


# 08/31/2026 - Day 9
# List
list = [10,20,30,20,32,48]
d = {}
for x in list:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
print(d)

print("------&*-------")
print("------&*-max from the list------")
# find the max from the list
max = 0
list = [10,20,30,20,32,48]
d = {}
for x in list:
    if x > max:
        max = x
print(max)


