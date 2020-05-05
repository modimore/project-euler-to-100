"""Project Euler Solutions
Problem 18: Maximum path sum I
Solved by: Quinn Mortimer (modimore)
"""
infile_name = "P018_Input.txt"

def read_triangle(fname):
    rows = []
    with open(fname, "r") as f:
        for line in f:
            rows.append([int(n) for n in line.split()])
    return rows

def find_max_path(tri):
    tri_stack = tri[:]
    running = [0] * (len(tri) + 1)
    while len(tri_stack) > 0:
        current = tri_stack.pop()
        for i in range(len(current)):
            running[i] = max(running[i], running[i+1]) + current[i]
    
    return running[0]

tri = read_triangle(infile_name)
print(find_max_path(tri))
