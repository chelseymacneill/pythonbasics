# A comprehension is a compact way of creating a Python data structure from iterators. Comprehensions can be used to combine loops and conditional tests
# Comprehension is very Pythonic and useful.

# Comprehension can be used to build a list by applying an expression to each item in an iterable
# Keeps for code neat and readable
# List comprehnsions are roughly twise as fast as manual for loops

# Basic example
# Task = Create a a list with all 0-4 squared

# First create an empty list
# L = []
# for x in range(5):
#     L.append(x**2)
# print(L)

# # list comprehension way
# L2 = [x**2 for x in range(5)]
# print(L2)

# List comprehension examples

# Example 1
# List comprehensions can iterate over any type of iterable such as lists, strings, files, and ranges (anything that supports the iteration protocol)

# x = [i*3 for i in 'RED']
# print(x)

# Example 2
# Convert list items to absolute values
# vec = [-4, 4, -2, 0, -100]

# abs_vec = [abs(i) for i in vec]

# print(vec)
# print(abs_vec)

# You can apply a method on each element in a list
# Remove whitespaces of list items
# colors = ['red ', 'blue', 'white ']
# colors_no_spaces = [colors.strip() for color in colors]
# # error: list has no attribute strip
# print(colors)
# print(colors_no_spaces)


# You can apply an optional if clause with a list comprehension
# This can be used to filter items out of a result.
# Follows [expression for var in iterbale if_clause]

# Filter list to exclude negative numbers
# vec = [-4, -5, 1, 3, 5]
# vec_no_neg = [i for i in vec if i >= 0]
# print(vec)
# print(vec_no_neg)

# Nested list comprehensions
# The initial expression in a list comprehension can be any expression, including another list comprehension

# Example of how to flatten a nested list into a single list of items
# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # For each number in a list in the vector
# L = [n for l in vector for n in l]
# print(vector)
# print(L)

# Above is equivalent to
# L2 = []
# for list in vector:
#     for number in list:
#         L2.append(number)
# print(L2)

# List comprehension vs. map() + lambda
# Map(f,L) is a faster way to run an already defined function on each element in a list

# List comprehension
# L = [i**2 for i in range(5)]
# print(L)

# # Map and Lamda
# L2 = list(map((lambda i: i**2), range(5)))
# print(L2)


# Creating a list of lists
x = 1
y = 1
z = 1

nested_list_min = [0, 0, 0]
nested_list_max = [x, y, z]

all_combos = [nested_list_min for i in range(3)]

print(nested_list_min)
print(nested_list_max)
print(all_combos)
