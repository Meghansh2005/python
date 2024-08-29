import math


C = 50
H = 30


input_sequence = input("Enter a sequence of comma-separated numbers: ")


D_values = [int(D) for D in input_sequence.split(',')]


Q_values = [round(math.sqrt((2 * C * D) / H)) for D in D_values]


print(",".join(map(str, Q_values)))
