"""Project Euler Solutions
Problem 16: Power digit sum
Solved by: Quinn Mortimer (modimore)
"""
def power_digit_sum(exp):
    n = 2 ** exp
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

print("Digit-wise sum of 2^1000:", power_digit_sum(1000))
