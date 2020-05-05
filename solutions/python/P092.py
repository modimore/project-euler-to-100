"""Project Euler Solutions
Problem 92: Square digit chains
Solved by: Quinn Mortimer (modimore)
"""
def sum_square_digits(x):
    return sum(int(d)**2 for d in str(x))

def solve(L=int(1E7)):
    ct89 = 0
    
    for n in range(1, L):
        while n != 1 and n != 89:
            n = sum_square_digits(n)
        if n == 89:
            ct89 += 1
    
    return ct89

if __name__ == "__main__":
    from sys import argv
    L = int(1E7)
    
    if len(argv) > 1:
        try:
            L = int(argv[1])
        except ValueError:
            pass
    
    print(solve(L))
