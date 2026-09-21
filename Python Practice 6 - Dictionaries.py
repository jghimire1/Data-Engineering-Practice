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


# Get the keys
# the keys() method will return a list of all the keys in the dictionary.
print("Add a new item to the original dictionary, and see that the keys lists gets updated as well.")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
    }
x = car.keys()

print(x) # before change
car["color"] = "white"

print(x) # after the change

print("Get a list of values:")
x = this_dict.values()
print(x)

print("Make a change in the original dictionary, and see that the values list gets updated as well.")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) # before change

car["year"] = 2020
print(x) # after change

print("Get a list of the key: value pairs.")
x = this_dict.items()
print(x)

print("check if model is present in the dictionary.")
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in this_dict:
    print("Yes, 'model' is one of the keys in the this_dict dictionary.")

# The pop()
print("The pop() method removes the item with the specified key name.")
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
this_dict.pop("model")
print(this_dict)

# delete
print("The del keyword can also delete the dictionary completely.")
del this_dict
#print(this_dict)

# clear() method
print("The clear() method empties the dictionary.")
this_dict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
this_dict2.clear()
print(this_dict2)
this_dict2["color"] = "Red" # adding key value pair after clear
print(this_dict2)
