# set {] - not allow duplicate items
# x = set()
x = {2, 3, 7, 10}
print, (type(x))

y = {1, 2, 3, 4, 5}
print(type(y))

print(x.intersection(y))  # finds the same values
print(x.union(y))  # adds 2 sets together
print(x.difference(y))  # shows value's, that other list doesn't have
