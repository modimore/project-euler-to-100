"""Project Euler Solutions
Problem 33: Digit cancelling fractions
Solved by: Quinn Mortimer (modimore)
"""
from functools import reduce

def digit_cancel(a, b):
    a = list(str(a))
    b = list(str(b))
    
    i = 0
    while i < len(a) and 0 < len(b):
        if a[i] in b:
            b.remove(a[i])
            a.pop(i)
        else:
            i += 1
    
    if len(a) == 0 or len(b) == 0:
        return None, None
    return int("".join(a)), int("".join(b))

def digit_cancel_nt(a, b):
    A, B = list(str(a)), list(str(b))
    if A[-1] == "0" and B[-1] == "0":
        return None, None
    
    _a, _b = digit_cancel(a, b)
    if a == _a and b == _b:
        return None, None
    return _a, _b

nums = []
denoms = []
for i in range(10, 100):
    for j in range(i, 100):
        if i != j:
            n, d = digit_cancel_nt(i, j)
            if n is not None and n != 0 and d != 0 and i/j == n/d:
                nums.append(n)
                denoms.append(d)

a, b = reduce(lambda acc, p: (acc[0] * p[0], acc[1] * p[1]), zip(nums, denoms), (1, 1))
print(a, b)
