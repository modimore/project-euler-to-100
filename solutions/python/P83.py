"""Project Euler Solutions
Problem 83: Path sum: four ways
Solved by: Quinn Mortimer (modimore)
"""

def minimum_path_sum_4ways(grid):
    w, h = len(grid[0]), len(grid)
    sum_grid = [[0] * w for _ in range(h)]
    
    visited = {}
    to_visit = [(0, 0, 0)]
    
    while len(to_visit) > 0:
        i, j, cost = to_visit.pop(0)
        cost += grid[j][i]
        
        if (i, j) in visited and visited[(i, j)] <= cost:
            continue
        
        visited[(i, j)] = cost
        
        if i > 0:
            to_visit.append((i-1, j, cost))
        if i+1 < w:
            to_visit.append((i+1, j, cost))
        if j > 0:
            to_visit.append((i, j-1, cost))
        if j+1 < h:
            to_visit.append((i, j+1, cost))
        to_visit.sort()#key=lambda t: t[2])
    
    return visited[(w-1, h-1)]

def solve(fname="P81_Input.txt"):
    grid = []
    with open(fname, "r") as f:
        for line in f:
            grid.append(list(map(int, line.split(","))))
    return minimum_path_sum_4ways(grid)

if __name__ == "__main__":
    print(solve())
