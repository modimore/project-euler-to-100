"""Project Euler Solutions
Problem 75: Singular integer right triangles
Solved by: Quinn Mortimer (modimore)
"""
from math import gcd, sqrt

# Solution derived from the following facts:
# * For any two integers m > n > 0
#     a, b, c = m2 - n2, 2*m*n, m2 + n2
#   yields a Pythagorean triple a, b, c
# * All integer multiples of a Pythagorean triple
#   are themselved Pythagorean triples
# * c / gcd(a, b, c) must be odd, hence exactly
#   one of m and n must be odd
def solve(L=int(1.5e6)):
    seen, seen_twice = set(), set()
    
    for m in range(1, int(sqrt(L))+1):
        m2 = m ** 2
        
        for n in range(1 if m % 2 == 0 else 2, m, 2):
            if 2 * (m2 + m * n) > L:
                break
            if gcd(m, n) != 1:
                continue
            
            n2 = n ** 2
            
            a, b, c = m2 - n2, 2*m*n, m2 + n2
            
            l0 = a + b + c
            l = l0
            while l <= L:
                if l in seen:
                    seen_twice.add(l)
                seen.add(l)
                l += l0
    
    return len(seen - seen_twice)

if __name__ == "__main__":
    from sys import argv
    L = int(1.5e6)
    
    if len(argv) > 1:
        try:
            L = int(argv[1])
        except ValueError:
            pass
    
    print(solve(L))
