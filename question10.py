
def is_palindrome(number):
    
    str_number = str(number)
    
    return str_number == str_number[::-1]


def count_digit_occurrences(number):
    
    str_number = str(number)
    
    digit_count = {}
    
    for digit in str_number:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    return digit_count


number = input("Enter a number: ")


if is_palindrome(number):
    print("Palindrome")
else:
    print("Not Palindrome.")


digit_count = count_digit_occurrences(number)

for digit, count in digit_count.items():
    print(f" {digit} appears {count} times")
