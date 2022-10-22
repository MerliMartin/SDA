# create a new list_1
list_1 = [1, 2, 3, 4, 5, 6, 7]
print(list_1[0])  # output is 1, We are looking for object what is place in index 0
print(list_1[-1])  # finds a last object in the list
list_1[3] = 'alice has a cat'  # replaces 3rd object
print(list_1)  # prints list, what is modified

# ==========================================

# zip (tuple)
shopping_items = ['eggs', 'ham', 'cheese']
quantities = [4, 2, 3]
print(list(zip(shopping_items, quantities)))

longer_list = ['red', 'hot', 'chilli', 'peppers']
shorter_list = ['czerwone', 'gorace', 'czili']
print(list(zip(longer_list, shorter_list)))
