
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
       
