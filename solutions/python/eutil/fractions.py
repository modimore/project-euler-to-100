from math import floor, sqrt

def sqrt_continued_fraction(n):
    sqrt_n = sqrt(n)
    whole_n = floor(sqrt_n)
    
    if whole_n == sqrt_n:
        return [whole_n]
    
    cf, seen = [], set()
    m, d, a = 0, 1, whole_n
    while (m,d,a) not in seen:
        cf.append(a)
        seen.add((m,d,a))
        
        m = d * a - m
        d = (n - m**2) // d
        a = floor((whole_n + m) // d)
    
    return cf
