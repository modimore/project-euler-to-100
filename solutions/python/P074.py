"""Project Euler Solutions
Problem 74: Digit factorial chains
Solved by: Quinn Mortimer (modimore)
"""
from eutil.helpers import memoize_unary
from eutil.numbers import digit_list as digits
from eutil.number_theory import factorial as fact

@memoize_unary
def sum_digit_factorials(n):
    return sum(fact(d) for d in digits(n))

def solve(limit=int(1e6), target_terms=60):
    ct = 0
    
    for n in range(limit):
        seen = set()
        n0 = n
        while n not in seen:
            seen.add(n)
            n = sum_digit_factorials(n)
        if len(seen) == target_terms:
            ct += 1
    
    return ct

if __name__ == "__main__":
    from sys import argv
    N = int(1e6)
    if len(argv) > 1:
        try:
            N = int(argv[1])
        except ValueError:
            pass
    print(solve(limit=N))
