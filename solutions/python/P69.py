"""Project Euler Solutions
Problem 69: Totient Maximum
Solved by: Quinn Mortimer (modimore)
"""
from math import gcd
from eutil.number_theory import euler_totient as phi

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
