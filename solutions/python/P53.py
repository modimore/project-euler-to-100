"""Project Euler Solutions
Problem 53: Combinatoric selections
Solved by: Quinn Mortimer (modimore)
"""
from eutil.number_theory import factorial as fact

def num_combinations(n, r):
    return fact(n) // (fact(r) * fact(n-r))

def solve(limit=100, threshold=10**6):
    num_values = 0
    for n in range(1, limit+1):
        for r in range(1, n+1):
            if num_combinations(n, r) > threshold:
                num_values += 1
    return num_values

if __name__ == "__main__":
    print("Solution:", solve())
