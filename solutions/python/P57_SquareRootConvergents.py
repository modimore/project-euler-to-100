# Project Euler Problem 57 Solution

from math import floor, log

def log10(x):
    return log(x, 10)

def solve(iterations=1000):
    num, den = 3, 2
    count = 0
    while iterations > 0:
        if floor(log10(num)) > floor(log10(den)):
            count += 1
        num, den = 2 * den + num, num + den
        iterations -= 1
    return count

if __name__ == "__main__":
    print("Solution:", solve())
