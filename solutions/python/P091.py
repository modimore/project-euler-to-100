"""Project Euler Solutions
Problem 91: Right triangles with integer coordinates
Solved by: Quinn Mortimer (modimore)
"""
def is_right_triangle(p, q, r):
    if p == q or p == r or q == r:
        return False
    
    pq2 = (p[0]-q[0])**2 + (p[1]-q[1])**2
    qr2 = (q[0]-r[0])**2 + (q[1]-r[1])**2
    rp2 = (r[0]-p[0])**2 + (r[1]-p[1])**2
    
    c2 = max(pq2, max(qr2, rp2))
    
    if c2 == pq2:
        a2, b2 = qr2, rp2
    elif c2 == qr2:
        a2, b2 = pq2, rp2
    else:
        a2, b2 = pq2, qr2
    
    return a2 + b2 == c2

def solve(L=50):
    O = (0, 0)
    pts = [(x, y)
            for x in range(L+1)
            for y in range(L+1)
            if (x, y) != (0, 0)
          ]
    
    ct = 0
    for pi in range(len(pts)):
        p = pts[pi]
        for qi in range(pi, len(pts)):
            q = pts[qi]
            if is_right_triangle(p, q, O):
                ct += 1
    return ct

if __name__ == "__main__":
    from sys import argv
    N = 50
    
    if len(argv) > 1:
        try:
            N = int(argv[1])
        except ValueError:
            pass
    
    print(solve(N))
