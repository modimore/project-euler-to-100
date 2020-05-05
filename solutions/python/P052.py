"""Project Euler Solutions
Problem 52: Permuted multiples
Solved by: Quinn Mortimer (modimore)
"""
# Project Euler Problem 52 Solution

def digit_counts(x):
    digits = [0 for x in range(10)]
    while x > 0:
        digits[x%10] += 1
        x //= 10
    return tuple(digits)

def solve(multiples=6):
    low = 1
    found = False
    x = None
    while not found:
        for n in range(low, 10*low // multiples):
            digit_counts_n = digit_counts(n)
            found = True
            for m in range(2, multiples+1):
                found = found and all(y == z for y, z in zip(digit_counts_n, digit_counts(m*n)))
            if found:
                x = n
                break
        low *= 10
    return x

if __name__ == "__main__":
    print("Solution:", solve())
