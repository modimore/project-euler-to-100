from fractions import Fraction
from math import floor, sqrt

# def continued_fraction(x, epsilon=1e-6):
#     c0 = floor(x)
#     if c0 == x:
#         return [c0]
#
#     eps_precision = -ceil(log10(epsilon))
#
#     cfs, f = [c0], round(x - c0, eps_precision)
#     print(f, cfs)
#     while epsilon <= abs(f):
#         f_inv = round(1 / f, eps_precision)
#         cf_n = floor(f_inv)
#         f = round(f_inv - cf_n, eps_precision)
#         cfs.append(cf_n)
#         print(f, cfs)
#
#     return cfs

def continued_fraction(x, epsilon=1e-6):
    c0 = floor(x)
    if c0 == x:
        return [c0]
    
    eps_precision = -ceil(log10(epsilon))
    
    cfs, f = [c0], Fraction(x-c0)
    while epsilon <= abs(f):
        f.limit_denominator(int(1/epsilon))
        f_inv = 1 / f
        cf_n = floor(f_inv)
        f = Fraction(f_inv - cf_n)
        cfs.append(cf_n)
    
    return cfs

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
