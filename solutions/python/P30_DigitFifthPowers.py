"""Project Euler Solutions
Problem 30: Digit fifth powers
Solved by: Quinn Mortimer (modimore)
"""
N = 5

def sum_digit_powers(n, exp):
    return sum(map(lambda d: d**exp, (int(c) for c in str(n))))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        try: N = int(sys.argv[1])
        except ValueError: pass
    
    print(sum(filter(lambda x: x==sum_digit_powers(x, N), range(10, 10**(N+1)))))
