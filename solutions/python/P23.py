"""Project Euler Solutions
Problem 23: Non-abundant sums
Solved by: Quinn Mortimer (modimore)
"""
from eutil.divisors import find_divisors

LIMIT = 28123

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            LIMIT = int(sys.argv[1])
        except ValueError:
            pass
    
    abundant_nums = set()
    for n in range(1, LIMIT+1):
        if sum(find_divisors(n)) > n:
            abundant_nums.add(n)
    
    two_added_abundants = set(range(1, LIMIT+1))
    for m in abundant_nums:
        for n in abundant_nums:
            if (m + n) in two_added_abundants:
                two_added_abundants.remove(m + n)
    
    print(sum(two_added_abundants))
