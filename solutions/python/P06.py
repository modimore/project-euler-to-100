"""Project Euler Solutions
Problem 6: Sum square difference
Solved by: Quinn Mortimer (modimore)
"""
def solve(n=100):
    sum_of_squares = sum(x*x for x in range(1, n+1))
    square_of_sum = ((n*(n+1))//2)**2
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    print(solve())
