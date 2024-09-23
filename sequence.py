
def find_missing_numbers(sequence):
    full_range = set(range(min(sequence), max(sequence) + 1))
    missing_numbers = full_range - set(sequence)
    return missing_numbers

sequence = [1, 2, 4, 5, 7, 8]
missing_numbers = find_missing_numbers(sequence)
print("Missing numbers:", missing_numbers)
