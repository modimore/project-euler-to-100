from math import ceil

N = 1000

# This solution just uses integer operations
def solve(n):
    return sum(x for x in range(n) if x%3 == 0 or x%5 == 0)

# This solutions is faster with large numbers
def solve_fast(n):
    return 3 * sum(range(ceil(n/3))) + 5 * sum(range(ceil(n/5))) - 15 * sum(range(ceil(n/15)))

if __name__ == '__main__':
    print(solve_fast(N))
