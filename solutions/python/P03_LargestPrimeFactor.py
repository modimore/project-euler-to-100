import math
from eutil.primes import primes, primes_below

NUM = 600851475143

# This is very slow
def max_prime_factor_slow(n):
    best_prime = None
    for p in primes_below(n):
        if n % p == 0:
            best_prime = p
    return best_prime

# This one can be very fast.
# Any large prime will be a case where it is not,
# but that's unavoidable.
def max_prime_factor(n):
    best_prime = None
    for p in primes:
        if n < p:
            break
        while n % p == 0:
            n = n // p
            best_prime = p
    
    return best_prime

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        try: NUM = int(argv[1])
        except ValueError: pass
    
    print(max_prime_factor(NUM))
