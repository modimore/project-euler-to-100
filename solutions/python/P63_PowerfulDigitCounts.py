"""Project Euler Solutions
Problem 63: Powerful digit counts
Solved by: Quinn Mortimer (modimore)
"""
from math import log

def solve(base=10):
    count, i = 0, 1
    while True:
        old_count = count
        for j in range(1, 10):
            logx_j = log(j**i, base)
            if int(logx_j) == i-1:
                count += 1
        if count == old_count:
            break
        i += 1
    return count
    # return sum(1 for i in range(1, 10) for j in range(1, 10) if len(str(i**j)) == j)

if __name__ == "__main__":
    print("Solution:", solve())
