# Dictionay items are ordered, changeable, and does not allow duplicates.
# Dictionary item sare presented in key:value pairs, and can be referred to by using the key name.

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict["brand"])

#print the item of the dictionary
print(len(this_dict))

print("Using the dict() method to make a dictionary.")

this_dict1 = dict(name = "John", age = 36, country = "Norway")

print(this_dict1)

print("Get the value of the model key. ")
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = this_dict["model"]
print(x)
