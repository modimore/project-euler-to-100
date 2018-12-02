"""Project Euler Solutions
Problem 47: Distinct primes factors
Solved by: Quinn Mortimer (modimore)
"""
from eutil.primes import primes

def factor_(n):
    factors = set()
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                factors.add(i)
                n //= i
                break
    return factors

def factor(n):
    if n == 1:
        return { 1 }
    if n in primes:
        return { n }
    
    primes_iter = iter(primes)
    while n > 1:
        p = next(primes_iter)
        if n % p == 0:
            while n % p == 0:
                n //= p
            return { p } | factor(n)

def compose_from_prime_factors(num_factors, limit=None):
    if num_factors == 0:
        yield 1
    elif limit is None:
        for p in primes:
            for q in compose_from_prime_factors(num_factors-1, p):
                yield p * q
    else:
        for p in primes:
            if p < limit:
                for q in compose_from_prime_factors(num_factors-1, p):
                    yield p * q
            else:
                raise StopIteration

if __name__ == "__main__":
    import sys
    
    scope = 4
    if len(sys.argv) > 1:
        try:
            scope = int(sys.argv[1])
        except ValueError:
            pass
    
    n = 2
    run = 0
    while run < scope:
        if len(factor(n)) == scope:
            run += 1
        else:
            run = 0
        n += 1
    print(n-scope)
