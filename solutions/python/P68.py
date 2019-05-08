"""Project Euler Solutions
Problem 68: Magic 5-gon ring
Solved by: Quinn Mortimer (modimore)
"""
from itertools import permutations

def n_gon_rings(n=5):
    for p in permutations(range(1, 2*n+1)):
        seq, sums = [], set()
        for i in range(n):
            seq.append((p[i+n], p[i], p[(i+1)%n]))
            sums.add(sum(seq[-1]))
        if len(sums) == 1:
            yield seq

def solve_simple():
    m = 0
    for r in n_gon_rings(5):
        # Each ring should start with the line beginning with the lowest
        # number on the outside, so we'll find that one and cycle around
        # the list to begin at the correct line
        start = min(r, key=lambda t: t[0])
        start_index = next(i for i, l in enumerate(r) if l == start)
        r = r[start_index:] + r[:start_index]
        rs = "".join("".join(str(t) for t in s) for s in r)
        if len(rs) == 16:
            m = max(m, int(rs))
    return m

def solve():
    m = 0
    for p1 in permutations(range(1,6)):
        for p2 in permutations(range(7,11)):
            p = list(p1) + [6] + list(p2)
            r = ""
            magic = True
            s = p[5] + p[0] + p[1]
            for i in range(5):
                if p[i+5] + p[i] + p[(i+1)%5] != s:
                    magic = False
                    break
                r += str(p[i+5]) + str(p[i]) + str(p[(i+1)%5])
            if magic:
                m = max(m, int(r))
    return m

if __name__ == "__main__":
    print(solve())
