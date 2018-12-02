"""Project Euler Solutions
Problem 41: Pandigital prime
Solved by: Quinn Mortimer (modimore)
"""
from itertools import permutations
from eutil.primes import get_primes_fast

MAX_INDEX = 7
digits = [1,2,3,4,5,6,7,8,9]
primes = get_primes_fast(10**MAX_INDEX)

max_pandigital_prime = 0
for i in range(1,MAX_INDEX+1):
    for p in permutations(digits[:i]):
        p = int("".join(str(d) for d in p))
        if p in primes:
            max_pandigital_prime = max(max_pandigital_prime, p)

print("Max Pandigital Prime:", max_pandigital_prime)
