from functools import reduce
from math import gcd
from .helpers import memoize_series, memoize_unary
from .primes import primes

def product(l):
    return reduce(lambda x, y: x * y, l, 1)

@memoize_unary
def euler_totient(n):
    """Counts the integers less than or equal to n are relatively prime to n"""
    if n == 1:
        return 1
    if n in primes:
        return n - 1
    
    for p in primes:
        if n % p == 0:
            x, y = p, n // p
            break
    
    if y % x == 0:
        return gcd(x, y) * euler_totient(y)
    else:
        return euler_totient(x) * euler_totient(y)
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
