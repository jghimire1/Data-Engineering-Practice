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
