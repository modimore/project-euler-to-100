"""Project Euler Solutions
Problem 80: Square root digital expansion
Solved by: Quinn Mortimer (modimore)
"""
from decimal import Decimal, Context, setcontext
from math import sqrt

varcontext = Context(prec=102)
setcontext(varcontext)

# Much less to do here if you have a high precision
# integer, or better, decimal, type.
# There is still a difference in result from a
# rounding error at a precision of 100 and 101 digits,
# so we need to use 102 digits here and truncate.
def solve():
    total = 0
    for n in range(1, 101):
        sqrt_n = sqrt(n)
        if sqrt_n == int(sqrt_n):
            continue
        sqrt_n_dec = Decimal(n).sqrt()
        total += sum(sqrt_n_dec.as_tuple().digits[:100])
    return total

if __name__ == "__main__":
    print(solve())
