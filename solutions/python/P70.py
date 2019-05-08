"""Project Euler Solutions
Problem 70: Totient Permutation
Solved by: Quinn Mortimer (modimore)
"""
from math import inf
# from eutil.number_theory import euler_totient as phi
from eutil.primes import primes_below

def is_permutation(m, n):
    s_m, s_n = str(m), str(n)
    if len(s_m) < len(s_n):
        s_m = s_m.ljust(len(s_n), "0")
    elif len(s_n) < len(s_m):
        s_n = s_n.ljust(len(s_m), "0")
    return sorted(s_m) == sorted(s_n)

# This is a brute force solution.
# It's much too slow, I've never seen it run to completion.
#def solve(limit=int(1e7)):
#    best_n, best_phi = 1, 1
#    best_ratio = inf
#    for n in range(2,limit+1):
#        phi_n = phi(n)
#        ratio_n = n / phi_n
#        if ratio_n < best_ratio:
#            if is_permutation(n, phi_n):
#                best_n, best_phi, best_ratio = n, phi_n, ratio_n
#    return best_n

# This gets the right answer, at least for the limit called for
# in the problem.
# Essentially it becomes more obvious if we use the following:
#   phi(n) = n * product((p-1) / p for p in primes_below(n) if n % p == 0)
# to define phi, that to minimise n / phi(n) we want n to have as few
# as possible prime factors that are each as large as possible.
# In this case I'm just hoping that two primes gives the right answer
# since I don't know what a definitive stop condition would be for
# searching through sets of factors.
def solve(limit=int(1e7)):
    best_n, best_ratio = 1, inf
    for p1 in primes_below(limit+1):
        for p2 in primes_below(p1):
            n, phi = p1 * p2, (p1-1) * (p2-1)
            if n > limit:
                break
            ratio = n / phi
            if ratio < best_ratio and is_permutation(n, phi):
                best_n, best_ratio = n, ratio
    return best_n

if __name__ == "__main__":
    from sys import argv
    N = int(1e7)
    try:
        N = int(argv[1])
    except:
        pass
    print(solve(N))
