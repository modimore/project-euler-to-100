"""Project Euler Solutions
Problem 49: Prime permutations
Solved by: Quinn Mortimer (modimore)
"""
from eutil.primes import primes, primes_below

def problem49():
    possibilities = []
    for p in primes_below(10000-2*3330):
        if p + 3330 in primes and p + 2*3330 in primes:
            possibilities.append((p,p+3330,p+2*3330))
    possibilities = filter(lambda p: set(p[0]) == set(p[1]) and set(p[0]) == set(p[2]), map(lambda p: tuple(str(pi) for pi in p), possibilities))
    for p in possibilities:
        if p[0] != str(1487):
            return "".join(p)

if __name__ == "__main__":
    print("Solution:", problem49())
