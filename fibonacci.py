def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Input from the user
n = int(input("Enter a number: "))

# Compute and print the Fibonacci value for the given n
print(f"Fibonacci of {n} is: {fibonacci(n)}")
