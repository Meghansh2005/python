def append_item(item, item_list=None):
    if item_list is None:  # Create a new list if item_list is not provided
        item_list = []
    item_list.append(item)
    return item_list

# Testing the modified function
print(append_item(1))  # Output: [1]
print(append_item(2))  # Output: [2]
print(append_item(3))  # Output: [3]
