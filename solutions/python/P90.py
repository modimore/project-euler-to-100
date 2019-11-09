"""Project Euler Solutions
Problem 90: Cube digit pairs
Solved by: Quinn Mortimer (modimore)
"""
from itertools import permutations

def solve():
    targets = set(x**2 for x in range(1,10))
    good = set()
    p_all = set(tuple(sorted(p[:6])) for p in permutations(range(0, 10)))
    for c1 in p_all:
        for c2 in p_all:
            if (c1, c2) in good or (c2, c1) in good:
                continue
            t = targets.copy()
            for f1 in c1:
                for f2 in c2:
                    if (f1 == 6 or f1 == 9) and (f2 == 6 or f2 == 9):
                        t -= {66, 69, 96, 99}
                    elif f1 == 6 or f1 == 9:
                        t.discard(90 + f2)
                        t.discard(60 + f2)
                        t.discard(f2 * 10 + 9)
                        t.discard(f2 * 10 + 6)
                    elif f2 == 6 or f2 == 9:
                        t.discard(90 + f1)
                        t.discard(60 + f1)
                        t.discard(f1 * 10 + 9)
                        t.discard(f1 * 10 + 6)
                    else:
                        t.discard(f1 * 10 + f2)
                        t.discard(f2 * 10 + f1)
                    
            if len(t) == 0:
                good.add((c1, c2))
    return len(good)

if __name__ == "__main__":
    print(solve())
