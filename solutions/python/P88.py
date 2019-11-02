"""Project Euler Solutions
Problem 88: Product-sum numbers
Solved by: Quinn Mortimer (modimore)
"""

def factors(n):
    if n == 0 or n == 1:
        return set()
    
    factors = set()
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            factors.add(i)
    
    return {1} | factors | {n // i for i in factors}

def min_psn(k):
    n = k
    while True:
        fs = sorted(factors(n))
        queue = [(n, n, k, len(fs)-1)]
        
        while len(queue) != 0:
            p, s, l, e = queue.pop()
            
            if p == 1:
                if l == 0 and s == 0:
                    return n
                if e == 0:
                    if s == l:
                        return n
                    else:
                        continue
            
            if l == 0 or s == 0:
                continue
            
            if e == 0 and p != 1:
                continue
            
            f = fs[e]
            if f <= p and p % f == 0:
                queue.append((p//f, s-f, l-1, e))
            if e > 0:
                queue.append((p, s, l, e-1))
        
        n += 1

def solve(n=12000):
    min_psns = set()
    for k in range(2,n+1):
        min_psns.add(min_psn(k))
    return sum(min_psns)

if __name__ == "__main__":
    from sys import argv
    N = 12000
    
    if len(argv) > 1:
        N = int(argv[1])
    
    print(solve(N))
