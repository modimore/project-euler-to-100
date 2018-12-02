"""Project Euler Solutions
Problem 15: Lattice paths
Solved by: Quinn Mortimer (modimore)
"""
def count_grid_routes(m, n):
    _m, _n = m+1, n+1
    grid = [[None for x in range(_m)] for y in range(_n)]
    
    grid[0][0] = 0
    for i in range(0, _m):
        grid[0][i] = 1
    for j in range(0, _n):
        grid[j][0] = 1
    
    for j in range(1, _n):
        for i in range(1, _m):
            grid[j][i] = grid[j-1][i] + grid[j][i-1]
    
    return grid[_n-1][_m-1]

print("Paths in 20x20 lattice:", count_grid_routes(20, 20))
