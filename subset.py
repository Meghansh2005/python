
def is_subset(small_set, large_set):
    return small_set.issubset(large_set)

small_set = {1, 2}
large_set = {1, 2, 3, 4, 5}
result = is_subset(small_set, large_set)
print("Is small set a subset of large set?", result)
