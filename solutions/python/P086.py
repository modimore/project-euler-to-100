"""Project Euler Solutions
Problem 86: Cuboid route
Solved by: Quinn Mortimer (modimore)
"""
from math import sqrt

# The key insight here is that the optimal distance is
# reached by splitting travelling along the longest dimension
# equally between moving along the other two dimensions,
# which essentially means reducing the problem down to
# finding the hypotensuse of a triangle with side lengths
# of the maximum side length and the sum of the other two
# side lengths.
# If this doesn't make sense try "unfolding" the cuboid as if
# it were a paper cube.
# You can effectively combine the two smaller dimensions into
# one dimension at this point, and for every possible sum of
# these two values, add a the number of combinations of the
# lengths of the two smaller sides that will add up to it.
def solve(M=1000000):
    int_dists = 0
    l = 0
    while int_dists < M:
        l += 1
        for wh in range(2, 2*l+1):
            min_dist = sqrt(l**2 + (wh)**2)
            if abs(min_dist - int(min_dist)) < 1E-6:
                if wh > l:
                    int_dists += l - wh//2 + (0 if wh%2 == 1 else 1)
                else:
                    int_dists += wh // 2
    return l

if __name__ == "__main__":
    from sys import argv
    M = int(1E6)
    if len(argv) > 1:
        try:
            M = int(argv[1])
        except ValueError:
            pass
    print(solve(M))
