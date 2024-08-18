def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get user input for conversion type
print("Choose the conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter 1 or 2: "))

# Perform the conversion based on user's choice
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")
