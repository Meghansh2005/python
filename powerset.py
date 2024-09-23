# Problem 10: Compute the power set of a given set
from itertools import chain, combinations

def power_set(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

s = {1, 2, 3}
powerset = power_set(s)
print("Power set of {}: {}".format(s, powerset))
