"""Project Euler Solutions
Problem 20: Factorial digit sum
Solved by: Quinn Mortimer (modimore)
"""
from eutil.number_theory import factorial

def solve(n=100):
    return sum(int(c) for c in str(factorial(n)))

if __name__ == "__main__":
    print(solve())
