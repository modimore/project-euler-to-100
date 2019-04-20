from math import gcd
from .helpers import memoize_series
from .primes import primes

def euler_totient(n):
    """Counts the integers less than or equal to n are relatively prime to n"""
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
            r *= euler_totient(p) * g // euler_totient(g)
        else:
            p = next(p_iter)

    return r
    #return sum(1 for x in range(1,n+1) if gcd(n, x) == 1)

@memoize_series
def factorial(n):
    """Calculates the factorial of a number"""
    if n == 0:
        return 1
    return n * factorial(n-1)

def gcd_euclidean(a, b):
    """Applies the Euclidean algorithm for finding the GCD of two numbers"""
    if b == 0:
        return a
    if a < b:
        return gcd_euclidean(b, a)

    return gcd_euclidean(b, a%b)
