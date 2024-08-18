
def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[2]**2 == sides[0]**2 + sides[1]**2


a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if is_right_triangle(a, b, c):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
