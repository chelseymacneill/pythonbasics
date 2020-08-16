# Lists can contain any sort object. 
# A list itself is a sort object so a list can contain a list (which can contain a list) 
# A list that contains a list is a nested list. 
# You can use nested lists to arrange data into hierarchical structures. 

# How to create a nested list 
L = ['c', ['bb',['ccc','ddd'],'bb','ff'], 'g', 'h']

# Accessing items in a nested list via an index
print(L[2]) 
# Expected output = ['bb',['ccc','ddd'],'bb','ff']

print(L[2][2])
#Expected output = ['ccc',ddd']

print(L[2][2][2])
#Expected output = N/A

print(L[2][2][2])
#Expected output = ddd
