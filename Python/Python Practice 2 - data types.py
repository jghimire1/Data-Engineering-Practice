# Built in Data types
# Text type -- str
# Numeric type -- int, float
# sequence type -- list, tuple
# mapping type -- dict
# set type -- set
# boolean type -- bool

# Examples
x = "Hello World" # data type --> String
x = 20 #---> int
x = 20.5 # ---> float
x = 1j # datatype ----> complex, python uniquely uses the letter j (or J) to denote the imaginary unit,
        # # it is built in numeric type usd to represent complex numbers

x = ["apple", "banana", "cherry"] # ---> list
x = ("apple", "banana", "cherry") #---> tuple

x = range(6) #---> range
x = {"name": "John", "age": 36} #---> dict
x = {"apple", "banana", "cherry"} # ---> set
x = True # ---> boolean

#Multiline String
a = """My name is janardan. I am learning python. 
Practice makes perfect so keep practicing everyday. """

print(a)

print("-----------")
#python slicing strings
# We can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

#Get the characters from position 2 to position 5 (not included):
b = "Hello world!"
print(b[2:5])

print("------+-----")

# Get the characters from the start to position 5(not included):
print(b[:5])

print("------++-----")
#get the characters from position 2, and all the way to end:
print(b[2:])
print("------+++-----")

# Negative Indexing
#Use negative indexes to start the slice from the end of the string:
#Get characters from "o" in "World! (position -5)
# To, but not included: "d" in "World! (position -2) not included:

b = "Hello world!"
print(b[-5:-2])

print("------+++*-----")
#The Upper() method returns the string in upper case:
c = "Hello world!"
print(c.upper())

print(c.lower()) # the lower() method returns the string in lower case.

c = " Hello, World"
print(c.strip()) # the strip() method removes any whitespace from the beginning or the end:

print(c.replace("H", "J")) #the replace() method replaces a string with another string.

print(c.split(",")) # the split() method splits the string into substrings if it finds instances of the separator.

print("*************")
#String concatenation
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print (c)
# To add the space between a and b add a " ":
c = a + " " + b
print (c)

# we can not combine strings and numbers like this:
age = 36
txt = "My name is Janardan, I am " + age
print(txt)

# But we can combine strings and numbers by using the format() method!
# some values are false
print("some values are false----------------------")
# In fact, there are not many values that evaluate to False, except empty values, such as (), {},[], "",
# the number o, and the value none. And of course, the value evaluates to False.
# The following will return false:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])

#Numbers
print("Numbers----------------")
x = 1 # int
y = 2.8 # float


print(myorder.format(quantity, itemno, price))

print("******#******")

# Boolean Values
#In programming you often need to know if an expression is true or false
#We can evaluate any expression in Python, and get one of two answers, True or False.
# When we compare two values, the expression is evaluated and Python returns the boolean answer.
print(10>9)
print(10==9)
print( 10 < 9)


# Print a message based on whether the condition is true or false:
a = 200
b = 33

print()
print("******#******")

if b >a:
    print("b is greater than a.")
else:
    print("b is not greater than a.")

print()
print("******#******")
# Most Values are True
# ALmost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0
# Any list, tuple, set, and dictionary are True, except empty ones.
# The following will return true:

bool("abc")
print(bool("abc"))

bool(123)
print(bool(123))

bool(["apple", "cherry", "banana"])
print(bool(["apple", "cherry", "banana"]))


# some values are false
print("some values are false----------------------")
# In fact, there are not many values that evaluate to False, except empty values, such as (), {},[], "",
# the number o, and the value none. And of course, the value evaluates to False.
# The following will return false:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])

#Numbers
print("Numbers----------------")
x = 1 # int
y = 2.8 # float

# int
# x = 1
y = 3625633246511
z = - 3255522
print(type(x))
print(type(y))
print(type(z))

#float
print("Float----------------")
# Float, or "floating point number" is a number, positive or negative, contatining one or more decimals
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


# type conversion
print("type conversion................")
# we can convert from one type to another with the int(), float().
# Convert from one type to another.
x = 1 # int
y = 2.8 # float

#convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

print(a)
print(b)
print(type(a))
print(type(b))

#Random number
# Import the random module, and display a random number between 1 and9
import random
print(random.randrange(1,10))
