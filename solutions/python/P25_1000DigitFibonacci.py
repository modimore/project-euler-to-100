"""Project Euler Solutions
Problem 25: 1000-digit Fibonacci number
Solved by: Quinn Mortimer (modimore)
"""
DIGITS = 1000

from math import log

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        try: DIGITS = int(argv[1])
        except ValueError: pass
    
    #MAX_LOG = DIGITS-1
    MAX = 10**(DIGITS-1)
    a, b = 0, 1
    index = 1
    #while log(b, 10) < MAX_LOG:
    while b < MAX:
        a, b = b, a+b
        index += 1
    
    print("Index of first Fibonacci number with {0} digits: {1}".format(DIGITS, index))
