def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Loop through numbers less than 20 and check if they are prime
for number in range(2, 20):
    if is_prime(number):
        print(number)
