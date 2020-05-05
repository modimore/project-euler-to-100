"""Project Euler Solutions
Problem 64: Odd period square roots
Solved by: Quinn Mortimer (modimore)
"""
from fractions import Fraction
from math import ceil, floor, log10, sqrt

def get_next_expansion(n, subtra, numer):
    denom = (n - subtra**2) / numer
    sqrt_n = sqrt(n)
    whole, fract = 0, (sqrt_n + subtra) / denom
    while fract >= 1:
        subtra -= denom
        fract -= 1
        whole += 1
    return whole, -1 * subtra, denom

def find_periodic_sqrt(n):
    sqrt_n = sqrt(n)
    sqrt_floor = floor(sqrt_n)
    seq = []
    
    if sqrt_n != sqrt_floor:
        cache = {}
        subtra, den = sqrt_floor, 1
        while (subtra, den) not in cache:
            expansion = get_next_expansion(n, subtra, den)
            cache[subtra, den] = expansion
            subtra, den = int(expansion[1]), int(expansion[2])
            seq.append(expansion[0])
    
    return sqrt_floor, seq

def solve(limit=10000):
    count = 0
    for n in range(1, limit+1):
        sqrt_base, sqrt_seq = find_periodic_sqrt(n)
        if len(sqrt_seq) % 2 == 1:
            count += 1
    return count

if __name__ == "__main__":
    from sys import argv
    N = 10000
    if len(argv) > 1:
        try:
            N = int(argv[1])
        except ValueError:
            pass
    print(solve(N))
