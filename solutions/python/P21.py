"""Project Euler Solutions
Problem 21: Amicable numbers
Solved by: Quinn Mortimer (modimore)
"""
from math import sqrt
from eutil.divisors import find_proper_divisors
N = 10000

def find_amicable_pair(n):
    m = sum(find_proper_divisors(n))
    if sum(find_proper_divisors(m)) == n:
        return m
    else:
        return None

def find_amicable_pairs(limit):
    amicable_numbers = set()
    amicable_pairs = []
    for n in range(1, limit):
        if n in amicable_numbers:
            continue
        
        p = find_amicable_pair(n)
        if p is not None and n != p:
            amicable_pairs.append((n, p))
            amicable_numbers.add(n)
            amicable_numbers.add(p)
    
    return amicable_pairs

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            N = int(sys.argv[1])
        except ValueError:
            print("Command line argument must be a number.")
    
    pairs = find_amicable_pairs(N)
    amicable_sum = sum(p[0] + p[1] for p in pairs)
    print("Amicable sum up to {}: {}".format(N, amicable_sum))
