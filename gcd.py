import math

def compute_gcd(a, b):
    """Compute the Greatest Common Divisor (GCD) of two numbers."""
    return math.gcd(a, b)

def compute_lcm(a, b):
    """Compute the Least Common Multiple (LCM) of two numbers."""
    gcd = compute_gcd(a, b)
    return abs(a * b) // gcd

# Example usage
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))

gcd = compute_gcd(num1, num2)
lcm = compute_lcm(num1, num2)

print(f"GCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")
