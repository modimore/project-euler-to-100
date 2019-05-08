"""Project Euler Solutions
Problem 2: Even Fibonacci numbers
Solved by: Quinn Mortimer (modimore)
"""
MAX = 4E6
# Just for reference
# def fib(n):
#     return 1 if n < 2 else fib(n-1) + fib(n-2)

def solve(LIMIT=int(4e6)):
    result = 0
    fib0, fib1 = 1, 1
    while fib1 < LIMIT:
        if fib1 % 2 == 0:
            result += fib1
        fib0, fib1 = fib1, fib0 + fib1
    
    return result

if __name__ == "__main__":
    print(solve())
