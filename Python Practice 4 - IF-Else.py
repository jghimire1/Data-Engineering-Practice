# Python Conditions and IF Statements
# Python Supports the usual logical conditions from mathematics:
#	Equals: a == b
#	Not Equals: a != b
#	Less than: a < b
#	Less than or equal to: a <= b
#	Greater than: a > b
#	Greater than or equal to: a >= b
print("IF--------------------")
a = 33
b = 200
if b > a:
    print("b is greater than b.")


print("Elif---------------")
# The elif keyword is python's way of saying
# "if previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal.")

