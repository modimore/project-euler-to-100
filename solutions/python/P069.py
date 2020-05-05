"""Project Euler Solutions
Problem 69: Totient Maximum
Solved by: Quinn Mortimer (modimore)
"""
from math import gcd
from eutil.primes import primes

# This is a brute force solution that's much too slow.
#def solve(limit=int(1e6)):
#    return max(range(2, limit+1), key=lambda n: n / phi(n))

# The goal for this problem is to maximise n / phi(n).
# Using this definition of phi(n):
#   phi(n) = n * product((p-1) / p for p in primes_below(n) if n % p == 0)
# we can say that
#   n / phi(n) = product(p/(p-1) for p in primes_below(n) if n % p == 0)
# Based on this we want as many and as primes factors as possible,
# which basically just means to take as many primes as possible until
# the product of those primes would be greater than the limit.
# Funnily enough we never have to calculte phi(n).
def solve(limit=int(1e6)):
    primes_iter = iter(primes)
    n = 1
    
    while True:
        n_ = n * next(primes_iter)
        if n_ > limit:
            break
        n = n_
    
    return n

if __name__ == "__main__":
    from sys import argv

    N = int(1e6) + 1
    try:
        N = int(argv[1])
    except:
        pass

    print(solve(N))
