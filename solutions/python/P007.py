"""Project Euler Solutions
Problem 7: 10001st prime
Solved by: Quinn Mortimer (modimore)
"""
from eutil.primes import primes

TARGET_INDEX = 10001

def solve(n):
    return primes[n-1]

if __name__ == "__main__":
    TARGET_INDEX = 10001
    import sys
    if len(sys.argv) > 1:
        try:
            TARGET_INDEX = int(sys.argv[1])
        except ValueError:
            print("Command line argument unparseable as integer:", sys.argv[1])
    
    print(solve(TARGET_INDEX))
