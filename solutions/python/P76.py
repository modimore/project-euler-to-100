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

helper_cache = {}
def helper(n, x_max):
    if (n, x_max) in helper_cache:
        return helper_cache[(n, x_max)]
    
    x = x_max
    ct = 0
    
    while x > 0:
        if x == n:
            ct += 1
        elif x < n:
            ct += helper(n-x, x)
        x -= 1
    
    helper_cache[(n, x_max)] = ct
    return ct

def solve(n=100):
    return helper(n, n-1)

if __name__ == "__main__":
    from sys import argv
    
    N = 100
    if len(argv) > 1:
        try: N = int(argv[1])
        except ValueError: pass
    
    print(solve(N))
