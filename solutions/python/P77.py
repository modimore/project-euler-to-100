"""Project Euler Solutions
Problem 77: Prime summations
Solved by: Quinn Mortimer (modimore)
"""
from eutil.primes import primes, primes_below

def helper(n, max_index):
    ct = 0
    
    index = max_index
    while index >= 0:
        p = primes[index]
        if p == n:
            ct += 1
        elif p < n:
            ct += helper(n - p, index)
        index -= 1
    
    return ct

def solve(target):
    n, n_primes = 1, 0
    primes_iter = iter(primes)
    p = next(primes_iter)
    while True:
        while p < n:
            p = next(primes_iter)
            n_primes += 1
        if helper(n, n_primes-1) > target:
            return n
        n += 1

if __name__ == "__main__":
    from sys import argv
    
    target = 5000
    if len(argv) > 1:
        try: target = int(argv[1])
        except ValueError: pass
    
    print(solve(target))
