"""Project Euler Solutions
Problem 72: Counting Fractions
Solved by: Quinn Mortimer (modimore)
"""
from math import gcd
from eutil.number_theory import euler_totient as phi
from eutil.primes import primes

def solve(D=int(1e6)):
    count = 0
    for den in range(2, D+1):
        count += phi(den)
    return count

if __name__ == "__main__":
    from sys import argv
    D = int(1e6)
    if len(argv) > 1:
        try:
            D = int(argv[1])
        except ValueError:
            pass
    print(solve(D))
