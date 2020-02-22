"""Project Euler Solutions
Problem 94: Almost equilateral triangles
Solved by: Quinn Mortimer (modimore)
"""
from math import sqrt

# An important observation, derived from Heron's formula,
# is that if you want the area to be even then the perimeter
# has to be even so them semi-permiter will be an integer.
# With that piece of information, we want two odd sides and
# one even side, and we can solve the problem over the range
# of possible values for the even side.
# To keep the equations, and the code, cleaner the even
# side length is represented as half of the loop variable.
# Where for each n, a triangle with side lengths
# a = 2 * n, b = c = 2*n +- 1 is constructed,
# the calcuation for x represents the area of the triangle
# as derived from Heron's formula.
def solve(L=int(1e9)):
    l = L//6
    s = 0
    n = 2
    while n <= l:
        n2 = 3*n**2
        n1 = 4*n
        
        x2 = n2 - n1 + 1
        x = int(sqrt(n2 - n1 + 1))
        if x**2 == x2:
            p = 6*n - 2
            s += p
        
        x2 = n2 + n1 + 1
        x = int(sqrt(x2))
        if x**2 == x2:
            p = 6*n + 2
            s += p
        
        n += 1
    
    if 6*n-2 <= L:
        n2 = 3*n**2
        n1 = 4*n
        
        x2 = n2 - n1 + 1
        x = int(sqrt(n2 - n1 + 1))
        if x**2 == x2:
            p = 6*n - 2
            s += p
    
    return s

if __name__ == "__main__":
    from sys import argv
    
    L = int(1e9)
    if len(argv) > 1:
        try: L = int(argv[1])
        except ValueError: pass
    
    print(solve(L))
