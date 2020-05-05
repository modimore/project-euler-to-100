"""Project Euler Solutions
Problem 81: Path sum: two ways
Solved by: Quinn Mortimer (modimore)
"""

def minimum_path_sum(grid):
    w, h = len(grid[0]), len(grid)
    sum_grid = [[0] * w for _ in range(h)]
    sum_grid[0][0] = grid[0][0]
    for i in range(1, w):
        sum_grid[0][i] = sum_grid[0][i-1] + grid[0][i]
    for j in range(1, h):
        sum_grid[j][0] = sum_grid[j-1][0] + grid[j][0]
    for j in range(1, h):
        for i in range(1, w):
            sum_grid[j][i] = grid[j][i] +\
                min(sum_grid[j-1][i], sum_grid[j][i-1])
    return sum_grid[-1][-1]

def solve(fname="P081_Input.txt"):
    grid = []
    with open(fname, "r") as f:
        for line in f:
            grid_row = list(map(int, line.split(",")))
            grid.append(grid_row)
    return minimum_path_sum(grid)

if __name__ == "__main__":
    print(solve())
