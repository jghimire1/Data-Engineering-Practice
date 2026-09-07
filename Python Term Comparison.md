
# Explain the difference between:
  ## List vs Tuple
    o List:
      ▪	Represented by square brackets []
      ▪	Mutable – can add, remove, and change its elements. 
      ▪	Uses more memory, i.e., stores extra buffer to support mutability. 
      ▪	Slower creation and iteration process 
      ▪	Unhashable – cannot be used as keys 
      ▪	More prone to errors and unexpected changes. 
      ▪	Useful for a homogeneous collection of items that will grow, shrink, or change over the course of the program. 
      ▪	Example – my_list = [1,2,3]
    o	Tuple 
      ▪	Represented by parentheses ()
      ▪	Immutable – fixed in size and its values 
      ▪	Use exact allocation of memory for the elements. 
      ▪	Faster processing and creation. 
      ▪	Can be used as keys if items are hashable. 
      ▪	Useful when data is fixed and structured and does not need to be changed in the future. 
      ▪	Useful when data integrity protection is needed to prevent accidental modification. 
      ▪	Example – my_tuple = (a,b,c)

## Dictionary vs Set
  	o Dictionary
      ▪	Stores key-value pairs 
      ▪	Indexing by key
      ▪	Key must be unique 
      ▪	Keys must be hashable and immutable 
      ▪	Does not support union or intersection directly 
      ▪	Represented by curly brackets {}
      ▪	For example d = {}
      ▪	Useful when you need to map relationships, to retrieve or update values based on the identifier (key)
      ▪	Use dictionary when:
      ●	Need to associate values with keys
      ●	Counting occurances
      ●	Mapping one thing to another 
      ●	Storing metadata with items 
    o	Set
      ▪	Set stores unique, standalone elements, no duplicates. 
      ▪	No indexing; must iterate or check in 
      ▪	All elements must be unique 
      ▪	Elements must be hashable and immutable 
      ▪	Supports (|, &, -, ^) 
      ▪	For example: s = set(); must use set constructor 
      ▪	Useful when 
      ●	Need to eliminate duplicates from a collection.
      ●	Need mathematical operations like intersections, union, and differences
      ●	Fast order of operations to check elements 
      ●	Need to track membership 
      ●	Order doesn’t matter 

  ## ●	Shallow Copy vs Deep Copy
    o	The core difference is how they handle nested (compound) objects. 
    o	Shallow Copy
        ▪	A shallow copy creates a new outer collection but leaves nested objects linked by reference 
        ▪	Nested objects are shared by reference
        ●	The outer list is a new container, but the nested list points to the same memory address. 
        ▪	Fast (O(n) outer elements only)
        ▪	Use when dealing with flat collections ((lists/dictionary of integers, strings, floats, Booleans) where no nested mutable structures exist.
    o	Deep copy
        ▪	Recursively clones both the outer collection and every object inside it.
        ●	Constructs a brand-new outer container and recursively copies every object nested inside.
        ▪	Nested objects are cloned independently 
        ▪	Slower (O(n) recursive traversal)
        ▪	Use when working with nested data structures. Like matrices, API JSON payloads with dictionaries inside lists, or complex class instances) and you must guarantee total isolation from mutations.

## is vs ==
    o	IS 
        ▪	It is an identity operator that compares the memory address
        ●	checks for object identity (whether two variables point to the exact same spot in computer memory.
        ▪	It identifies whether these two variables point to the exact same object in RAM.
        ▪	Checks against singletons like None, True, or False. 
        ▪	Use whenever exclusively checking for None, True, or False. 
    o	==
      ▪	It is an equality operator that compares the contents of the objects. 
      ▪	Identifies whether these two things look the same.
      ●	Checks for value equality (whether two variables hold the same data
      ▪	Compares numbers, strings, lists, etc. 
      ▪	Use whenever we want to know if two variables contain the same text, number, list items, or dictionary data. 

  ## Append () vs extend ()
  


