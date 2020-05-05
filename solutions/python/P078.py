"""Project Euler Solutions
Problem 78: Coin Partitions
Solved by: Quinn Mortimer (modimore)
"""
from eutil.numbers import pentagon_number

# The implementation couldn't be used because
# finding p(n) requires previous partial
# calculations, so you need to know your n ahead
# of time, which is not the problem here.
# def num_partitions(n):
#     cs = [1] + [0] * n
#     
#     for i in range(1, n+1):
#         for j in range(i, n+1):
#             cs[j] += cs[j-i]
#     
#     return cs[-1]
#
# def solve(factor=int(1e6)):
#     n = 1
#     p = num_partitions(n)
#     while p % factor != 0:
#         p = num_partitions(n)
#         n += 1
#     return n

# Various sources directly show this optimization
# based on the pentagonal number theorem, which
# allows you to find the answer using previous
# complete results.
def solve(factor=int(1e6)):
    n = 0
    cs = [1]
    while cs[-1] % factor != 0:
        n += 1
        i = 0
        pent = pentagon_number(1)
        cn = 0
        while pent <= n:
            if i % 4 < 2:
                cn += cs[n-pent]
            else:
                cn -= cs[n-pent]
            i += 1
            j = (1 if i%2==0 else -1) * (1+i//2)
            pent = pentagon_number(j)
        cs.append(cn)
    return n

if __name__ == "__main__":
    from sys import argv
    
    F = int(1e6)
    if len(argv) > 1:
        try:
            F = int(argv[1])
        except ValueError:
            pass
    
    print(solve(F))
