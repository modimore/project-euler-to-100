"""Project Euler Solutions
Problem 85: Counting rectangles
Solved by: Quinn Mortimer (modimore)
"""

def n_contained(w_outer, h_outer, w_inner, h_inner):
    return (1 + w_outer - w_inner) * (1 + h_outer - h_inner)

def solve(target=2000000):
    best, best_w, best_h = target, 0, 0
    queue = [(1, 1)]
    seen = set()
    
    while len(queue) > 0:
        w, h = queue.pop(0)
        if (w, h) in seen:
            continue
        
        seen.add((w, h))
        contained = 0
        for i in range(1, w+1):
            for j in range(1, h+1):
                contained += n_contained(w, h, i, j)
        score = abs(target-contained)
        if score < best:
            best, best_w, best_h = score, w, h
        if contained < target:
            queue.append((w+1, h))
            queue.append((w, h+1))
        if w * h > target:
            break
        
        queue.sort(key=lambda d: d[0]+d[1])
    return best_w * best_h

if __name__ == "__main__":
    from sys import argv
    target = 2000000
    if len(argv) > 1:
        try: target = int(argv[1])
        except ValueError: pass
    print(solve(target))
