# Project Euler Problem 58 Solution

from math import ceil, exp
from eutil.primes import primes

def solve(ratio_limit=0.10):
    value, step = 1, 2
    n_primes, n_values = 0, 1
    
    factor = 100 * ratio_limit
    if factor == int(factor): factor = int(factor)
    primes.to(ceil(exp(1/ratio_limit)))
    
    while True:
        to_check = []
        for _ in range(4):
            value += step
            to_check.append(value)
            n_values += 1
        for corner in to_check[::-1]:
            if corner in primes:
                n_primes += 1
        if 100 * n_primes < factor * n_values:
            break
        # print(n_primes, n_values, step, value, factor, 100 * n_primes, factor * n_values)
        step += 2
    
    return step + 1

if __name__ == "__main__":
    from sys import argv
    ratio_limit = 0.10
    if len(argv) > 1:
        try:
            ratio_limit = float(argv[1])
        except ValueError:
            pass
    print("Solution:", solve(ratio_limit))
