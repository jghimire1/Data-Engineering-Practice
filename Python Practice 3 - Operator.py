# Python Operator
# Python Arithmetic Operators
# +	Addition ---->	x + y
# -	Subtraction ---->	x - y
# *	Multiplication ---->	x * y
# /	Division ---->	x / y
# %	Modulus	---> x % y
# **	Exponentiation ---->	x ** y
# //	Floor division	----> x // y

print(" Python Assignment operators-------------")
# Assignment operators are used to assign the values to variables.
# Operator	Example	Same As
#assign or equal  =	 -->   x = 5	-->     x = 5
# add: += -->	x += 3  -->	    x = x + 3
# subtract: -= -->	x -= 3 -->	    x = x - 3
# multiply: *= -->	x *= 3 -->	    x = x * 3
# Divide: /= -->	x /= 3 -->	    x = x / 3
# Modules: %= -->	x %= 3	-->     x = x % 3
# floor divide: //= -->	x //= 3	-->     x = x // 3
# Exponent: **= -->	x **= 3 -->	    x = x ** 3
# BITWISE AND --> &= -->	x &= 3 -->	    x = x & 3 # SETS EACH BIT TO 1 IF BOTH BITS ARE 1
# BITWISE OR--> |= -->	x |= 3 -->	    x = x | 3 # sets each bit to 1 if at least one of the bits is 1.
# BITWISE XOR--> ^= -->	x ^= 3 -->	    x = x ^ 3 # SETS EACH BIT TO 1 IF ONLY ONE OF THE BITS IS 1.
# Right shift --> >>= -->	x >>= 3 -->	    x = x >> 3 #shifts the binary bits of the left variable to the right by the
                        #  number of positions specified on the right. This effectively halves the number for each shift.
# Left Shift --> <<= -->	x <<= 3 -->	    x = x << 3 # shifts the binary bits to the left, adding zeros on the
                                    # right. This effectively doubles the nuber for each shift.


print("Python comparison Operators------------------")
# Comparison Operators are used to compare two values

# Operator	Name	Example
# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y

x = 5
y = 3
print(x==y)


print()
print("Python Logical Operators-------------")
# Logical operators are used to combine conditional statements:
# Operator	Description	                                Example
# and -->	Returns True if both statements are true  -->	x < 5 and  x < 10
# or -->	Returns True if one of the statements is true -->	x < 5 or x < 4
# not -->	Reverse the result, returns False if the result is true	--> not(x < 5 and x < 10)
x = 5
print(x> 3 and x < 10)


print("Python Identity Operators ---------------------")
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the
# same object, with the same memory location:

# Operator	Description	                                                    Example
# is --->	Returns True if both variables are the same object	    ---->   x is y
# is not --->	Returns True if both variables are not the same object	 ---> x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print (x is z) # returns True because z is same object as x.

print(x is y ) # returns False because x is not the same object as y, even if they have the same content.

print (x ==y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) # returns False because z is the same object as x

print (x is not y ) # returns True because x is not the same object as y, even if they have the same content
print (x != y)

print ("Python Membership Operators------")
# Operator	Description	Example
# in --->	Returns True if a sequence with the specified value is present in the object	--> x in y
# not in --->	Returns True if a sequence with the specified value is not present in the object	---> x not in y





