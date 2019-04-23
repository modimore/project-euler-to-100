"""Project Euler Solutions
Problem 45: Triangular, pentagonal, and hexagonal
Solved by: Quinn Mortimer (modimore)
"""
from eutil.numbers import triangle_numbers, pentagon_numbers, hexagon_numbers

tri_cat_nums = []
for t in triangle_numbers:
    if t in pentagon_numbers and (t in hexagon_numbers):
        tri_cat_nums.append(t)
        if len(tri_cat_nums) == 3:
            break

print("Triple category numbers:", ", ".join(str(t) for t in tri_cat_nums))
