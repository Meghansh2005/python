def print_first_5_squares():
    # Generate a list of squares from 1 to 20
    squares = [i**2 for i in range(1, 21)]
    
    # Print the first 5 elements
    print(squares[:5])

# Call the function
print_first_5_squares()
