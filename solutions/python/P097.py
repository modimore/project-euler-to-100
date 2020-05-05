"""Project Euler Solutions
Problem 97: Larges non-Mersenne prime
Solved by: Quinn Mortimer (modimore)
"""
# Convenient that Python uses bigintegers by default and
# the pow function has a mod argument ;)
def solve():
    return (28433 * pow(2, 7830457, int(1E10)) + 1) % int(1E10)

if __name__ == "__main__":
    print(solve())
