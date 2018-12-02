"""Project Euler Solutions
Problem 12: Highly divisible triangular number
Solved by: Quinn Mortimer (modimore)
"""
from math import sqrt
def find_factors(n):
    factor = 1
    factors = {factor}
    sqrt_n = int(sqrt(n))
    while factor <= sqrt_n:
        factor += 1
        if n % factor == 0:
            factors.add(factor)

    for factor in list(factors):
        factors.add(n // factor)

    return factors

N = 500
i = 1
t = 1
factors = find_factors(t)
while len(factors) <= N:
    i += 1
    t += i
    factors = find_factors(t)
    # print(i, t, len(factors), sorted(factors))

print(t)
