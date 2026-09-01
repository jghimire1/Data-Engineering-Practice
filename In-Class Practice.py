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
