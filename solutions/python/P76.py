"""Project Euler Solutions
Problem 76: Counting Summations
Solved by: Quinn Mortimer (modimore)
"""
# This is ultimately not fast enough but I like the idea
# def solve(n=100):
#     x = n-1
#     t, c, s = 0, 0, []
#
#     while x > 0:
#         s.append(x)
#         t += x
#
#         if t > n:
#             x = s.pop()
#             t -= x
#             x -= 1
#         elif t == n:
#             c += 1
#             x = 1
#             while len(s) > 0 and x == 1:
#                 x = s.pop()
#                 t -= x
#             x -= 1
#
#     return c

# Doable for small numbers and perhaps more suited to
# arbitrary minimum partition sizes,
# but it doesn't scale very well.
# helper_cache = {}
# def helper(n, x_max):
#     if (n, x_max) in helper_cache:
#         return helper_cache[(n, x_max)]
#
#     x = x_max
#     ct = 0
#
#     while x > 0:
#         if x == n:
#             ct += 1
#         elif x < n:
#             ct += helper(n-x, x)
#         x -= 1
#
#     helper_cache[(n, x_max)] = ct
#     return ct

# def solve(n=100):
#     # return num_partitions(n) - 1
#     return helper(n, n-1)

def num_partitions(n):
    cs = [1] + [0] * n
    
    for i in range(1, n+1):
        for j in range(i, n+1):
            cs[j] += cs[j-i]
    
    return cs[-1]

# Really fast, but not as flexible as the last solution
# Stumbled across this idea trying to optimize for P78
# Subtracting one has a pretty sound logical basis,
# given that the problem statement can be read as
# "discount the trivial summation/partition"
def solve(n=100):
    return num_partitions(n) - 1

if __name__ == "__main__":
    from sys import argv
    
    N = 100
    if len(argv) > 1:
        try: N = int(argv[1])
        except ValueError: pass
    
    print(solve(N))
