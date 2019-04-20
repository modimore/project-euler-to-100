"""Project Euler Solutions
Problem 69: Totient Maximum
Solved by: Quinn Mortimer (modimore)
"""

from math import gcd
from eutil.primes import primes

def phi(n):
    if n == 1:
        return 1
    if n in primes:
        return n - 1
    
    r = 1
    p_iter = iter(primes)
    p = next(p_iter)
    while p <= n:
        if n % p == 0:
            n //= p
            g = gcd(n, p)
            r *= phi(p) * g // phi(g)
        else:
            p = next(p_iter)
    
    return r
    #return 1 + sum(1 for x in range(2,n) if gcd(n, x) == 1)

def solve(limit=int(1e6)):
    return max(range(2, limit+1), key=lambda n: n / phi(n))

if __name__ == "__main__":
    from sys import argv
    
    N = int(1e6) + 1
    try:
        N = int(argv[1])
    except:
        pass
    
    print(solve(N))
