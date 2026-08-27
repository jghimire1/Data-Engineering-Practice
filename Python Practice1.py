 # Python practice
x = 5
y = "John"

print(x)
print(y)

# casting
# if you want to specify the data type of variable, this can be done with casting.

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

print (x)
print (y)
print(z)

# Get the type
print(type(x))
print(type(y))

# single or Double quotes?
x = "John"
# is the same.
x = 'John'

# Case Sensitivity
# Variable names are case-sensitive.

a = 4
A = "Sally" # A will not overwrite a
print(a, A)

# Many Values to Multiple variables
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables
# And you can assign the same value to multiple variables in one line:
x=y=z= "Orange"
print(x)
print(y)
print(z)
#Unpack collection
# If you have a collection of values in a list, tuple, etc. Python allows you to extract the values into variables. Thi is called unpacking.
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

#output variables
# The python print() function is often used to output variables
x = "Python is awesome."
print(x)

# in the print() function, you output multiple variables, separated by comma:
# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = "Python"
y = "is"
z = "awesome"
print(x,y,z)


