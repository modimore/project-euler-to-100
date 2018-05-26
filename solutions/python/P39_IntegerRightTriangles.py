best = (0, None)
for p in range(4, 1000):
    num_right_triangles = 0
    for c in range(p//3, p//2):
        c2 = c**2
        for b in range(p//4, c):
            a = p - c - b
            if a**2 + b**2 == c2:
                num_right_triangles += 1
    if num_right_triangles > best[0]:
        best = (num_right_triangles, p)

print(best[1])
