"""Project Euler Solutions
Problem 82: Path sum: three ways
Solved by: Quinn Mortimer (modimore)
"""

def minimum_path_sum_3ways(grid):
    w, h = len(grid[0]), len(grid)
    sum_grid = [[0]*w for _ in range(h)]
    for j in range(0, h):
        sum_grid[j][0] = grid[j][0]
    for i in range(1, w):
        for j1 in range(0, h):
            dists = []
            for j2 in range(0, j1):
                dists.append(sum_grid[j2][i-1] + sum(grid[j][i] for j in range(j2, j1+1)))
                dists.append(sum_grid[j2][i-1] + sum(grid[j][i-1] for j in range(j2+1, j1+1)) + grid[j1][i])
            dists.append(sum_grid[j1][i-1] + grid[j1][i])
            for j2 in range(j1+1, h):
                dists.append(sum_grid[j2][i-1] + sum(grid[j][i] for j in range(j1, j2+1)))
                dists.append(sum_grid[j2][i-1] + sum(grid[j][i-1] for j in range(j1, j2)) + grid[j1][i])
            sum_grid[j1][i] = min(dists)
    return min(sum_grid[j][-1] for j in range(0, h))

def solve(fname="P81_Input.txt"):
    grid = []
    with open(fname, "r") as f:
        for line in f:
            grid.append(list(map(int, line.split(","))))
    return minimum_path_sum_3ways(grid)

if __name__ == "__main__":
    print(solve())
