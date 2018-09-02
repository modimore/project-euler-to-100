# Project Euler Problem 56 Solution

from eutil.numbers import digit_list

def solve(A=100, B=100):
    best = 0
    for a in range(1, A):
        for b in range(0, B):
            best = max(sum(digit_list(a**b)), best)
    return best

if __name__ == "__main__":
    print("Solution:", solve())
