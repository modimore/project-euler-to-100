"""Project Euler Solutions
Problem 100: Arranged Probability
Solved by: Quinn Mortimer (modimore)
"""
# There's a recurrence relation with these variables,
# but I don't exactly know why.
# It's not too hard to find the coefficients on paper,
# you just need three consecutive pairs in the sequence,
# but under what circumstances there is guaranteed to
# be one I am not sure.
def solve(L=int(1e12)):
    n, b = 4, 3
    while n < L:
        np, bp = n, b
        b = 3 * bp + 2 * np - 2
        n = 4 * bp + 3 * np - 3
    return b

if __name__ == "__main__":
    from sys import argv
    
    L = int(1e12)
    if len(argv) > 1:
        try: L = int(argv[1])
        except ValueError: pass
    print(solve(L))
