"""Project Euler Solutions
Problem 37: Truncatable primes
Solved by: Quinn Mortimer (modimore)
"""
from eutil.numbers import primes

# Find the first 11 truncateable primes,
# meaning that all subsequences of digits starting at
# either the front or back are still prime.
# Reportedly there are only 11 of these.

def is_truncatable_prime(n):
    s_n = str(n)
    for sz in range(0, len(s_n)):
        if not int(s_n[:sz+1]) in primes:
            return False
        if not int(s_n[sz:]) in primes:
            return False
    return True

limit = 11

if __name__ == "__main__":
    result = []
    itr_primes= iter(primes)
    p = next(itr_primes)
    while p < 10:
        p = next(itr_primes)
    while True:
        if is_truncatable_prime(p):
            result.append(p)
            if len(result) == limit:
                break
        p = next(itr_primes)
    
    print(result)
    print(sum(result))
