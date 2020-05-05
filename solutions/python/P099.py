"""Project Euler Solutions
Problem 99: Largest exponential
Solved by: Quinn Mortimer (modimore)
"""
from math import log

# These numbers can be too big to be calculable quickly,
# so instead of comparing a^m and b^n this will compare
# m and n * log_a b to gague which number is larger.
def largest_exponential(pairs):
    largest_b, largest_e, largest_idx = 2, 0, None
    for index, (base, exp) in enumerate(pairs):
        exp_factor = log(base, largest_b)
        exp_relative = exp_factor * exp
        if exp_relative > largest_e:
            largest_b, largest_e = base, exp
            largest_idx = index
    return largest_b, largest_e, largest_idx

def solve(filename="P099_Input.txt"):
    pairs = []
    with open(filename, "r") as f:
        for line in f:
            pairs.append(map(int, line.split(",")))
    return largest_exponential(pairs)[2] + 1

if __name__ == "__main__":
    print(solve())
