"""Project Euler Solutions
Problem 66: Diophantine Equation
Solved by: Quinn Mortimer (modimore)
"""

import itertools
from math import sqrt
from eutil.fractions import sqrt_continued_fraction

def is_square(x):
    sqrt_x = sqrt(x)
    return sqrt_x == int(sqrt_x)

def solve(D_max=1001):
    x_sol, y_sol, D_sol = 1, 0, None
    
    for D in filter(lambda d: not is_square(d), range(1, D_max)):
        cf = sqrt_continued_fraction(D)
        
        nump, denp = 1, 0
        num, den = cf[0], 1
        
        cf_iter = iter(itertools.cycle(cf[1:]))
        
        while num**2 - D*den**2 != 1:
            c = next(cf_iter)
            num, nump = c * num + nump, num
            den, denp = c * den + denp, den
        
        if num > x_sol:
            x_sol, y_sol, D_sol = num, den, D
    
    return D_sol

if __name__ == "__main__":
    from sys import argv
    D_max = 1001
    if len(argv) > 1:
        try: D_max = int(argv[1])
        except ValueError:
            pass
    print(solve(D_max+1))
