# Creating a tuple
my_tuple = (10, 20, 30, 40, 20)
# Accessing elements
print(my_tuple[0])     # Output: 10
print(my_tuple[-1])    # Output: 20
# Tuple length
print(len(my_tuple))   # Output: 5
# Count occurrences
print(my_tuple.count(20))  # Output: 2
# Find index of element
print(my_tuple.index(30))  # Output: 2
# Tuple with different data types
mixed_tuple = (1, "Hello", 3.14, True)
# Looping through a tuple
for item in my_tuple:
    print(item)
    
# Nested tuple
nested_tuple = (1, 2, (3, 4, 5))
print(nested_tuple[2][1])  # Output: 4
# Single-element tuple (needs a comma)
single_element = (10,)
print(type(single_element))  # Output: <class 'tuple'>
