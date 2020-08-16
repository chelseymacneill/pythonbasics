# Lists can contain any sort object.
# A list itself is a sort object so a list can contain a list (which can contain a list)
# A list that contains a list is a nested list.
# You can use nested lists to arrange data into hierarchical structures.

# How to create a nested list
#L = ['c', ['bb', ['ccc', 'ddd'], 'bb', 'ff'], 'g', 'h']

# Accessing items in a nested list via an index
# print(L[2])
# Expected output = ['bb',['ccc','ddd'],'bb','ff']

# print(L[1][2])
# Expected output = ['ccc',ddd']

# print(L[2][2][2])
# Expected output = N/A

# print(L[2][2][2])
# Expected output = ddd

# You can also access lists via a negative index which starts from the end of the list (-1 is the last element)

# print(L[-1])

# You can change the value of an item in a list via
#L[1][1] = 0
# print(L)


# Adding items to a nested list
# To add values to the END of a nested list, use the append() method
#L2 = ['a', [1, 2, 3], 'z']
# print(L2)
# L2[1].append('xx')
# print(L2)

# To add values to a specfic position in a list use the insert() method
#L3 = [1, 2, ['a', 'b', 'z'], 4]
#L3[2].insert(2, 'cc')
# print(L3)

# Merge to lists together using the extend method
#L4 = [1, 2]
#L5 = [3, 4]

# L4.extend(L5)
# print(L4)
# print(L5)

# Remove items from a nested list
# Remove by index value

# L7 = [1, 2, 3, [4, 5]]
# print(L7)
# x = L7.pop(3)
# print(L7)
# print(x)

# If you don't need the removed value use delete

# If you don't know the index but the actual value use the remove method
# Only removes first instance it finds
# L8 = ['a', 'b', ['c', 'd'], 'a']
# print(L8)
# L8.remove('a')
# print(L8)

# Finding the length of a nested list


# Iterate through a nested list
# Can be done with a simple for loop
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for list in L:
    for i in list:
        print(i, end=' ')
