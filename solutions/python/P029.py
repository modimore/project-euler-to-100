"""Project Euler Solutions
Problem 29: Distinct Powers
Solved by: Quinn Mortimer (modimore)
"""

def solve(A=100, B=100):
    s = set()
    for a in range(2, A+1):
        for b in range(2, B+1):
            s.add(a**b)
    return len(s)

if __name__ == "__main__":
    print(solve())
