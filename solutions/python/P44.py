"""Project Euler Solutions
Problem 44: Pentagon numbers
Solved by: Quinn Mortimer (modimore)
"""
from __future__ import print_function
from eutil.numbers import pentagon_numbers

if __name__ == "__main__":
    try:
        from math import inf
    except:
        from sys import maxint
        inf = maxint
    best = (None, None, inf)
    found = False
    k = 1
    while not found:
        P_k = pentagon_numbers[k]
        j = k - 1
        while 0 <= j:
            P_j = pentagon_numbers[j]
            S, D = P_k + P_j, P_k - P_j
            if D > best[2]:
                break
            if D in pentagon_numbers and S in pentagon_numbers:
                best = min((j, k, D), best, key=lambda d: d[2])
            j -= 1
        if 3 * k + 1 > best[2]:
            found = True
        k += 1
    print("Minimum difference:", best[2])
