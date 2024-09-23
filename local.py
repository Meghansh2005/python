def sample_function():
    a = 10
    b = 20
    c = a + b
    d = 50

# Function to detect the number of local variables
def count_local_variables(func):
    return func.__code__.co_nlocals

# Example usage
print(f"Number of local variables: {count_local_variables(sample_function)}")
