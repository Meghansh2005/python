def append_item(item, item_list=[]):
    item_list.append(item)
    return item_list

# Testing the function by calling it multiple times
print(append_item(1))  # Output: [1]
print(append_item(2))  # Output: [1, 2]
print(append_item(3))  # Output: [1, 2, 3]
