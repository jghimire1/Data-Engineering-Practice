# Lambda Function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Addition
print("Add 10 to argument a, and return the result:")
x = lambda a:a+10
print(x(5))

# Multiplication
print("Multiply argument a with argument b and return the result.")
x = lambda a,b: a * b
print(x(5,6))

# Summarization
print("Summarise argument a,b, and c and return the result. ")
x = lambda a,b,c : a+b+c
print(x(5,6,2))
