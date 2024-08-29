
n = input("Enter a sequence of 4-digit comma-separated binary numbers: ")


binary_list = n.split(',')


divisible_by_5 = []


for binary in binary_list:
    
    d = int(binary, 2)
    
    
    if d % 5 == 0:
        divisible_by_5.append(binary)


output = ",".join(divisible_by_5)


print(output)
