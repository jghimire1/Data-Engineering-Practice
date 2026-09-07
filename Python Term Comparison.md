
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
