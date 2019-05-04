"""Project Euler Solutions
Problem 71: Ordered Fractions
Solved by: Quinn Mortimer (modimore)
"""

def solve(target=3/7, D=int(1e6)):
    best_n, best_d = 0, 1
    best_f = best_n / best_d
    for d in range(1, D+1):
        n = int(d * target)
        f = n / d
        if f < target and f > best_f:
            best_n, best_d, best_f = n, d, f
    return best_n

if __name__ == "__main__":
    from sys import argv
    D_max = int(1e6)
    if len(argv) > 1:
        try:
            D_max = int(argv[1])
        except ValueError:
            pass
    
    print(solve(D=D_max))
