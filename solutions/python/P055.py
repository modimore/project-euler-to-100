"""Project Euler Solutions
Problem 55: Lychrel numbers
Solved by: Quinn Mortimer (modimore)
"""
def reverse_digits(n):
    return int(str(n)[::-1])

def is_lychrel(n, iterations=50):
    if iterations == 0:
        return True
    
    s = n + reverse_digits(n)
    if s == reverse_digits(s):
        return False
    return is_lychrel(s, iterations-1)

def solve(limit=10000):
    count = 0
    for n in range(1, limit):
        if is_lychrel(n):
            count += 1
    return count

if __name__ == "__main__":
    print("Solution:",solve())
