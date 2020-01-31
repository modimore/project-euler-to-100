"""Project Euler Solutions
Problem 93: Arithmetic expressions
Solved by: Quinn Mortimer (modimore)
"""
# Non-commutative operations have forward/backward variants
OPS = [
        lambda x, y: x + y, # +
        lambda x, y: x - y, # -
        lambda x, y: y - x, # -
        lambda x, y: x * y, # *
        lambda x, y: x / y, # /
        lambda x, y: y / x  # /
]

# This function is essentially generating the expression
# tree that you can get with these operations and these
# numbers with various groupings
def combine(ns, ops):
    if len(ns) == 1:
        n = ns.pop()
        return [n for op in ops]
    
    res = set()
    for n in ns:
        s = set(ns)
        s.remove(n)
        for r in combine(s, ops):
            for op in ops:
                try:
                    res.add(op(n, r))
                except ZeroDivisionError:
                    pass
    
    return res

def consec_len(ns):
    l = 1 if len(ns) > 1 else 0
    for a, b in zip(ns, ns[1:]):
        if a + 1 != b:
            break
        l += 1
    return l

def solve():
    L_max = 0
    abcd = None
    # Compared to itertools.permutations or similar,
    # this four-loops approach eliminates a lot of
    # duplicate work.
    for d in range(4, 10):
        for c in range(3, d):
            for b in range(2, c):
                for a in range(1, b):
                    vs = sorted(set(int(v) for v in combine({a,b,c,d}, OPS) if v > 0 and int(v) == v))
                    L = consec_len(vs)
                    # print(a, b, c, d, L, vs)
                    if L > L_max:
                        abcd = a, b, c, d
                        L_max = L
    return "".join(str(n) for n in abcd)
    
if __name__ == "__main__":
    print(solve())
