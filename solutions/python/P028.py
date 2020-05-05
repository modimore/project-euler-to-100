"""Project Euler Solutions
Problem 28: Number spiral diagonals
Solved by: Quinn Mortimer (modimore)
"""
MAX = (1001 // 2)
i = 0
diag_sum = 1
while i < MAX:
    sqr_i = (2*i+1)**2
    i += 1
    i_ = i + 1
    diag_sum += sqr_i + 2*i
    diag_sum += sqr_i + 4*i
    diag_sum += sqr_i + 6*i
    diag_sum += sqr_i + 8*i

print('Sum of diagonals:', diag_sum)
