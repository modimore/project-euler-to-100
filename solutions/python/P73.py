"""Project Euler Solutions
Problem 73: Counting Fractions in a range
Solved by: Quinn Mortimer (modimore)
"""
from math import ceil, gcd

def solve(l=1/3, h=1/2, D=int(12e3)):
    count = 0
    for d in range(1, D+1):
        for x in range(d//3+1, ceil(d/2)):
            if gcd(d, x) == 1:
                count += 1
    return count

if __name__ == "__main__":
    from sys import argv
    D = int(12e3)
    if len(argv) > 1:
        try:
            D = int(argv[1])
        except ValueError:
            pass
    print(solve(D=D))
